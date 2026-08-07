"""The Security Device Data Model -- one dataset, many deliverables.

WHY THIS EXISTS
---------------
On most projects, the same device exists in five places that drift apart:

    Revit model  ->  drawings  ->  Bluebeam markups  ->  Excel schedule
                                                     ->  network/IP plan
                                                     ->  commissioning tracker
                                                     ->  as-builts / O&M

Each is maintained by hand. By CD phase they disagree, and reconciling them is
days of tedium and the source of most coordination RFIs. Your software
background makes this fixable: define ONE schema, make every artifact a
projection of it, and validate the projections against each other.

This is the highest-leverage differentiator available to you in your first two
years. Nobody else on the team is going to build it.

DESIGN PRINCIPLES
-----------------
1. Plain stdlib. Runs on a locked-down laptop. No install, no approval needed.
2. CSV in, CSV out. Every engineer on the team can open it, and it diffs in git.
3. Validation is advisory, never silent mutation. The tool reports; a human
   decides. Automate the repetitive work, never the engineering judgment.
4. Every field is optional at early design phases and required later. The schema
   knows which phase requires what -- so a SD-phase device isn't flagged for a
   missing IP address it cannot possibly have yet.
5. Findings carry severity and a device ID so they can be triaged, assigned, and
   closed like any other defect.
"""

from __future__ import annotations

import csv
import re
from dataclasses import asdict, dataclass, field, fields
from enum import Enum
from pathlib import Path


class Phase(str, Enum):
    """Design phase. Determines which fields are required."""
    SD = "SD"    # schematic design -- location and type only
    DD = "DD"    # design development -- product basis, mounting, power
    CD = "CD"    # construction documents -- everything specifiable
    CX = "CX"    # commissioning -- as-installed addresses, serials, test status

    @property
    def order(self) -> int:
        return {"SD": 0, "DD": 1, "CD": 2, "CX": 3}[self.value]


class Severity(str, Enum):
    ERROR = "ERROR"      # will cause a construction problem; must fix
    WARNING = "WARNING"  # probably wrong; engineer must confirm
    INFO = "INFO"        # worth a look


@dataclass
class Finding:
    severity: Severity
    device_id: str
    field_name: str
    message: str

    def __str__(self) -> str:
        return f"[{self.severity.value:7s}] {self.device_id:16s} {self.field_name:18s} {self.message}"


# Device type -> (prefix, human name). The prefix drives ID validation and is the
# same abbreviation used on drawings, in the Bluebeam Tool Chest, and in the
# Revit family names. Keeping ONE list is the entire point.
DEVICE_TYPES: dict[str, tuple[str, str]] = {
    "CAM_FIXED":      ("CAM", "Fixed camera"),
    "CAM_DOME":       ("CAM", "Fixed dome camera"),
    "CAM_PTZ":        ("PTZ", "Pan-tilt-zoom camera"),
    "CAM_MULTI":      ("MSC", "Multisensor camera"),
    "CAM_PANO":       ("PAN", "Panoramic/fisheye camera"),
    "CAM_THERMAL":    ("THC", "Thermal camera"),
    "READER":         ("CR",  "Card reader"),
    "READER_KP":      ("CRK", "Card reader with keypad"),
    "READER_BIO":     ("CRB", "Biometric reader"),
    "DPS":            ("DPS", "Door position switch"),
    "REX":            ("REX", "Request to exit"),
    "STRIKE":         ("ES",  "Electric strike"),
    "MAGLOCK":        ("EM",  "Electromagnetic lock"),
    "ELEC_LOCKSET":   ("EL",  "Electrified lockset"),
    "ELEC_EXIT":      ("EPD", "Electrified exit device"),
    "CONTROLLER":     ("ACP", "Access control panel"),
    "SUB_CONTROLLER": ("ACM", "Downstream/door module"),
    "PIR":            ("MD",  "Motion detector"),
    "GBD":            ("GBD", "Glass break detector"),
    "DURESS":         ("DUR", "Duress button"),
    "CONTACT":        ("MC",  "Magnetic contact"),
    "INTERCOM":       ("IC",  "Intercom station"),
    "INTERCOM_MSTR":  ("ICM", "Intercom master station"),
    "TURNSTILE":      ("TS",  "Turnstile"),
    "PWR_SUPPLY":     ("PS",  "Power supply"),
    "SWITCH":         ("SW",  "Network switch"),
    "SERVER":         ("SRV", "Server"),
    "WORKSTATION":    ("WS",  "Workstation"),
    "RACK":           ("RK",  "Equipment rack"),
}

IP_DEVICE_TYPES = {
    "CAM_FIXED", "CAM_DOME", "CAM_PTZ", "CAM_MULTI", "CAM_PANO", "CAM_THERMAL",
    "CONTROLLER", "INTERCOM", "INTERCOM_MSTR", "SWITCH", "SERVER", "WORKSTATION",
}
POE_DEVICE_TYPES = IP_DEVICE_TYPES - {"SWITCH", "SERVER", "WORKSTATION"}
CAMERA_TYPES = {t for t in DEVICE_TYPES if t.startswith("CAM_")}
DOOR_HARDWARE_TYPES = {"STRIKE", "MAGLOCK", "ELEC_LOCKSET", "ELEC_EXIT"}

# field name -> earliest phase at which it must be populated
REQUIRED_BY_PHASE: dict[str, Phase] = {
    "device_id": Phase.SD, "device_type": Phase.SD, "level": Phase.SD,
    "room": Phase.SD, "drawing": Phase.SD,
    "manufacturer": Phase.DD, "model": Phase.DD, "mount_type": Phase.DD,
    "mount_height_ft": Phase.DD, "spec_section": Phase.DD,
    "cable_id": Phase.CD, "cable_type": Phase.CD, "panel": Phase.CD,
    "ip_address": Phase.CX, "mac_address": Phase.CX, "switch": Phase.CX,
    "switch_port": Phase.CX, "serial_number": Phase.CX,
}

# <PREFIX>-<LEVEL>-<ROOM>[SUFFIX]
# ROOM is alphanumeric because head-end equipment legitimately lives in rooms
# designated MDF, IDF-2, SOC rather than by number. Requiring digits there was
# an early mistake in this schema and it flagged every controller and switch.
ID_PATTERN = re.compile(r"^([A-Z]{2,4})-([0-9]{1,2}|[BGRPM]{1,2})-([A-Z0-9]{2,6})([A-Z]?)$")
IP_PATTERN = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
MAC_PATTERN = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$")


@dataclass
class SecurityDevice:
    """One physical device. Every field is a column in the exported schedule.

    ID convention:  <PREFIX>-<LEVEL>-<ROOM/SEQ>[<SUFFIX>]
    e.g. CAM-2-214, CR-1-101A, ACP-4-MDF is NOT valid (room must be numeric).

    The suffix letter distinguishes multiple devices of the same type in one
    room (CR-1-101A on the public side, CR-1-101B on the secure side).
    """
    # --- identity (SD) ---
    device_id: str = ""
    device_type: str = ""
    description: str = ""

    # --- location (SD) ---
    level: str = ""
    room: str = ""
    room_name: str = ""
    zone: str = ""              # security zone 0-5
    drawing: str = ""

    # --- product (DD) ---
    manufacturer: str = ""
    model: str = ""
    spec_section: str = ""      # e.g. 28 23 00
    mount_type: str = ""        # pendant / surface / recessed / pole / wall
    mount_height_ft: str = ""

    # --- camera-specific ---
    resolution_mp: str = ""
    lens_mm: str = ""
    frame_rate: str = ""
    retention_days: str = ""
    ppf_target: str = ""        # design pixel density target
    ppf_actual: str = ""        # calculated at the target plane

    # --- access-control-specific ---
    controller: str = ""        # parent ACP device_id
    controller_input: str = ""
    controller_output: str = ""
    reader_interface: str = ""  # OSDP / Wiegand
    fail_state: str = ""        # SAFE / SECURE
    door_number: str = ""

    # --- power (DD/CD) ---
    poe_class: str = ""         # af / at / bt_t3 / bt_t4 / none
    power_source: str = ""      # PoE / local 12VDC / local 24VDC
    power_supply: str = ""      # PS device_id
    current_draw_a: str = ""

    # --- network (CX) ---
    ip_address: str = ""
    mac_address: str = ""
    vlan: str = ""
    switch: str = ""
    switch_port: str = ""

    # --- cabling (CD) ---
    cable_id: str = ""
    cable_type: str = ""
    cable_length_ft: str = ""
    panel: str = ""

    # --- lifecycle ---
    status: str = "NEW"         # NEW / EXISTING / RELOCATE / REMOVE
    serial_number: str = ""
    install_date: str = ""
    cx_status: str = ""         # PENDING / PASS / FAIL
    requirement_ids: str = ""   # semicolon-separated RTM trace -- "why is this here?"
    notes: str = ""

    @property
    def type_prefix(self) -> str:
        return DEVICE_TYPES.get(self.device_type, ("", ""))[0]

    @property
    def is_camera(self) -> bool:
        return self.device_type in CAMERA_TYPES

    @property
    def is_ip_device(self) -> bool:
        return self.device_type in IP_DEVICE_TYPES

    @property
    def expects_poe(self) -> bool:
        return self.device_type in POE_DEVICE_TYPES

    def to_row(self) -> dict[str, str]:
        return {k: ("" if v is None else str(v)) for k, v in asdict(self).items()}

    @classmethod
    def field_names(cls) -> list[str]:
        return [f.name for f in fields(cls)]

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "SecurityDevice":
        known = cls.field_names()
        return cls(**{k: (row.get(k) or "").strip() for k in known})


class DeviceRegister:
    """A collection of devices, with validation and export.

    This is the single source of truth. Drawings, schedules, the IP plan, the
    cable schedule, and the commissioning tracker are all PROJECTIONS of it.
    """

    def __init__(self, devices: list[SecurityDevice] | None = None,
                 phase: Phase = Phase.CD) -> None:
        self.devices: list[SecurityDevice] = devices or []
        self.phase = phase

    # ---------------- I/O ----------------

    @classmethod
    def from_csv(cls, path: str | Path, phase: Phase = Phase.CD) -> "DeviceRegister":
        with open(path, newline="", encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
        return cls([SecurityDevice.from_row(r) for r in rows], phase=phase)

    def to_csv(self, path: str | Path, columns: list[str] | None = None) -> None:
        cols = columns or SecurityDevice.field_names()
        with open(path, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            for d in sorted(self.devices, key=lambda x: x.device_id):
                w.writerow(d.to_row())

    # ---------------- projections ----------------

    def camera_schedule(self) -> list[dict]:
        cols = ["device_id", "level", "room", "room_name", "drawing", "manufacturer",
                "model", "resolution_mp", "lens_mm", "mount_type", "mount_height_ft",
                "ppf_target", "ppf_actual", "frame_rate", "retention_days",
                "poe_class", "switch", "switch_port", "ip_address", "status"]
        return [{c: getattr(d, c) for c in cols}
                for d in sorted(self.devices, key=lambda x: x.device_id) if d.is_camera]

    def door_schedule(self) -> list[dict]:
        """One row per door, assembling the devices that serve it.

        This is the projection that saves the most time in practice: door
        schedules are normally maintained by hand and drift from the device
        plans immediately.
        """
        doors: dict[str, dict] = {}
        for d in self.devices:
            if not d.door_number:
                continue
            row = doors.setdefault(d.door_number, {
                "door_number": d.door_number, "level": d.level, "room": d.room,
                "room_name": d.room_name, "zone": d.zone, "controller": d.controller,
                "reader": "", "reader_type": "", "dps": "", "rex": "",
                "lock": "", "lock_type": "", "fail_state": "", "devices": [],
            })
            row["devices"].append(d.device_id)
            if d.device_type.startswith("READER"):
                row["reader"], row["reader_type"] = d.device_id, d.device_type
            elif d.device_type == "DPS":
                row["dps"] = d.device_id
            elif d.device_type == "REX":
                row["rex"] = d.device_id
            elif d.device_type in DOOR_HARDWARE_TYPES:
                row["lock"], row["lock_type"] = d.device_id, d.device_type
                row["fail_state"] = d.fail_state
        for r in doors.values():
            r["device_count"] = len(r["devices"])
            r["devices"] = ";".join(sorted(r["devices"]))
        return [doors[k] for k in sorted(doors)]

    def ip_plan(self) -> list[dict]:
        cols = ["device_id", "device_type", "level", "room", "ip_address",
                "mac_address", "vlan", "switch", "switch_port", "poe_class"]
        return [{c: getattr(d, c) for c in cols}
                for d in sorted(self.devices, key=lambda x: x.device_id)
                if d.is_ip_device]

    def cable_schedule(self) -> list[dict]:
        cols = ["cable_id", "device_id", "device_type", "level", "room",
                "cable_type", "cable_length_ft", "panel", "switch", "switch_port"]
        return [{c: getattr(d, c) for c in cols}
                for d in sorted(self.devices, key=lambda x: x.cable_id or x.device_id)
                if d.cable_id]

    def counts_by_type(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for d in self.devices:
            out[d.device_type] = out.get(d.device_type, 0) + 1
        return dict(sorted(out.items()))

    def counts_by_drawing(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for d in self.devices:
            out[d.drawing or "(none)"] = out.get(d.drawing or "(none)", 0) + 1
        return dict(sorted(out.items()))
