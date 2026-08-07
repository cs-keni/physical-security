"""Validation rules for the Security Device Register.

PHILOSOPHY
----------
These checks find the mistakes that are TEDIOUS for a human and TRIVIAL for a
computer: duplicate IDs, orphaned references, ID/type mismatches, missing
fields, IP collisions, doors missing a required component. That is the correct
division of labour.

They deliberately do NOT check whether a camera is in the right place, whether
the pixel density target is appropriate, or whether a door should be fail safe.
Those are engineering judgment and they stay with you.

Every rule returns Findings. Nothing is auto-corrected. A tool that silently
"fixes" your data will eventually silently break it, and you will not notice
until it is in a construction document.

    python3 16_Automation/data_model/validate.py <devices.csv> [PHASE]
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schema import (  # noqa: E402
    CAMERA_TYPES, DEVICE_TYPES, DOOR_HARDWARE_TYPES, ID_PATTERN, IP_PATTERN,
    IP_DEVICE_TYPES, MAC_PATTERN, REQUIRED_BY_PHASE, DeviceRegister, Finding,
    Phase, Severity,
)


# ---------------------------------------------------------------------------
# Individual rules. Each takes the register and yields Findings.
# ---------------------------------------------------------------------------

def check_duplicate_ids(reg: DeviceRegister) -> list[Finding]:
    """Duplicate device IDs. The classic copy-paste error on a device plan.

    Consequence if missed: two devices share an ID, the contractor installs
    one, commissioning tests one, and the second is discovered at closeout --
    or never.
    """
    counts = Counter(d.device_id for d in reg.devices if d.device_id)
    return [
        Finding(Severity.ERROR, did, "device_id",
                f"Duplicate device ID -- appears {n} times")
        for did, n in sorted(counts.items()) if n > 1
    ]


def check_id_format(reg: DeviceRegister) -> list[Finding]:
    """ID matches the naming convention, and its prefix matches its type."""
    out: list[Finding] = []
    for d in reg.devices:
        if not d.device_id:
            out.append(Finding(Severity.ERROR, "(blank)", "device_id",
                               "Device has no ID"))
            continue
        m = ID_PATTERN.match(d.device_id)
        if not m:
            out.append(Finding(Severity.ERROR, d.device_id, "device_id",
                               "Does not match <PREFIX>-<LEVEL>-<ROOM>[SUFFIX]"))
            continue
        prefix, level, _room, _sfx = m.groups()
        expected = d.type_prefix
        if expected and prefix != expected:
            out.append(Finding(
                Severity.ERROR, d.device_id, "device_id",
                f"Prefix '{prefix}' does not match device_type "
                f"'{d.device_type}' (expected '{expected}')"))
        if d.level and level != d.level:
            out.append(Finding(
                Severity.WARNING, d.device_id, "level",
                f"ID level '{level}' disagrees with level column '{d.level}'"))
    return out


def check_unknown_types(reg: DeviceRegister) -> list[Finding]:
    return [
        Finding(Severity.ERROR, d.device_id, "device_type",
                f"Unknown device_type '{d.device_type}' -- "
                f"add it to DEVICE_TYPES or correct the entry")
        for d in reg.devices
        if d.device_type and d.device_type not in DEVICE_TYPES
    ]


# Rack-mounted head-end equipment is fed by rack power and patch cords, not by
# a scheduled field cable, so the cable columns legitimately stay blank for it.
# Without this exemption every switch and power supply generates noise, and a
# validator that cries wolf gets ignored -- which is worse than no validator.
HEADEND_TYPES = {"PWR_SUPPLY", "SWITCH", "SERVER", "WORKSTATION", "RACK"}
CABLE_FIELDS = {"cable_id", "cable_type", "cable_length_ft"}
NETWORK_FIELDS = {"ip_address", "mac_address", "switch", "switch_port"}


def check_required_fields(reg: DeviceRegister) -> list[Finding]:
    """Fields required at or before the current design phase."""
    out: list[Finding] = []
    for d in reg.devices:
        for fname, req_phase in REQUIRED_BY_PHASE.items():
            if req_phase.order > reg.phase.order:
                continue  # not required yet at this phase
            if fname in CABLE_FIELDS and d.device_type in HEADEND_TYPES:
                continue  # rack-fed, no scheduled field cable
            if fname in NETWORK_FIELDS and not d.is_ip_device:
                continue  # non-IP devices have no address
            if not getattr(d, fname, ""):
                out.append(Finding(
                    Severity.ERROR, d.device_id or "(blank)", fname,
                    f"Required at {req_phase.value} phase but empty"))
    return out


def check_orphan_references(reg: DeviceRegister) -> list[Finding]:
    """Every controller / power_supply / switch reference must resolve.

    Orphaned references are how a device ends up with nothing feeding it. This
    is a graph-integrity check and it is exactly the kind of thing a spreadsheet
    cannot do for you.
    """
    ids = {d.device_id for d in reg.devices if d.device_id}
    out: list[Finding] = []
    for d in reg.devices:
        for fname in ("controller", "power_supply", "switch"):
            ref = getattr(d, fname, "")
            if ref and ref not in ids:
                out.append(Finding(
                    Severity.ERROR, d.device_id, fname,
                    f"References '{ref}', which is not in the register"))
    return out


def check_ip_addresses(reg: DeviceRegister) -> list[Finding]:
    """Valid format, no duplicates, and present on devices that need one."""
    out: list[Finding] = []
    seen: dict[str, list[str]] = defaultdict(list)
    for d in reg.devices:
        if d.ip_address:
            if not IP_PATTERN.match(d.ip_address):
                out.append(Finding(Severity.ERROR, d.device_id, "ip_address",
                                   f"Malformed IP '{d.ip_address}'"))
            elif any(int(o) > 255 for o in d.ip_address.split(".")):
                out.append(Finding(Severity.ERROR, d.device_id, "ip_address",
                                   f"Octet out of range in '{d.ip_address}'"))
            else:
                seen[d.ip_address].append(d.device_id)
            if not d.is_ip_device:
                out.append(Finding(
                    Severity.WARNING, d.device_id, "ip_address",
                    f"Non-IP device type '{d.device_type}' has an IP address"))
        if d.mac_address and not MAC_PATTERN.match(d.mac_address):
            out.append(Finding(Severity.ERROR, d.device_id, "mac_address",
                               f"Malformed MAC '{d.mac_address}'"))
    for ip, owners in sorted(seen.items()):
        if len(owners) > 1:
            out.append(Finding(
                Severity.ERROR, ", ".join(sorted(owners)), "ip_address",
                f"DUPLICATE IP {ip} -- will cause an address conflict in the field"))
    return out


def check_switch_ports(reg: DeviceRegister) -> list[Finding]:
    """No two devices on the same switch port."""
    seen: dict[tuple[str, str], list[str]] = defaultdict(list)
    for d in reg.devices:
        if d.switch and d.switch_port:
            seen[(d.switch, d.switch_port)].append(d.device_id)
    return [
        Finding(Severity.ERROR, ", ".join(sorted(owners)), "switch_port",
                f"Two devices assigned to {sw} port {port}")
        for (sw, port), owners in sorted(seen.items()) if len(owners) > 1
    ]


def check_door_completeness(reg: DeviceRegister) -> list[Finding]:
    """Every controlled door needs a coherent set of devices.

    This rule encodes real engineering rules-of-thumb, so its findings are
    WARNINGS, not errors -- there are legitimate exceptions and the engineer
    decides. But an unexplained exception is almost always a mistake.
    """
    out: list[Finding] = []
    for row in reg.door_schedule():
        dn = row["door_number"]
        if row["reader"] and not row["lock"]:
            out.append(Finding(Severity.ERROR, dn, "door",
                               "Reader with no locking device -- the door cannot lock"))
        if row["lock"] and not row["dps"]:
            out.append(Finding(
                Severity.ERROR, dn, "door",
                "Locking device with no DPS -- forced and held-open conditions "
                "cannot be detected, and the door's state is unknown"))
        if row["reader"] and not row["rex"]:
            out.append(Finding(
                Severity.WARNING, dn, "door",
                "Reader and no REX -- confirm egress does not generate a "
                "forced-door alarm. Justify in the SOO if intentional"))
        if row["lock"] and not row["fail_state"]:
            out.append(Finding(
                Severity.ERROR, dn, "door",
                "Locking device with no fail_state (SAFE/SECURE) declared"))
        if row["lock_type"] == "MAGLOCK" and row["fail_state"] == "SECURE":
            out.append(Finding(
                Severity.ERROR, dn, "door",
                "Maglock declared FAIL SECURE -- a maglock is inherently fail "
                "SAFE (it releases on power loss). Correct the entry"))
        if row["lock"] and not row["controller"]:
            out.append(Finding(Severity.ERROR, dn, "door",
                               "Locking device with no controller assigned"))
    return out


def check_camera_fields(reg: DeviceRegister) -> list[Finding]:
    out: list[Finding] = []
    for d in reg.devices:
        if d.device_type not in CAMERA_TYPES:
            continue
        if reg.phase.order >= Phase.DD.order:
            if not d.resolution_mp:
                out.append(Finding(Severity.ERROR, d.device_id, "resolution_mp",
                                   "Camera with no resolution specified"))
            if not d.lens_mm and d.device_type not in ("CAM_PANO", "CAM_PTZ"):
                out.append(Finding(Severity.WARNING, d.device_id, "lens_mm",
                                   "Fixed camera with no lens specified"))
            if not d.ppf_target:
                out.append(Finding(
                    Severity.WARNING, d.device_id, "ppf_target",
                    "No pixel-density target -- you cannot commission a camera "
                    "against an unstated requirement"))
        if d.ppf_target and d.ppf_actual:
            try:
                if float(d.ppf_actual) < float(d.ppf_target):
                    out.append(Finding(
                        Severity.ERROR, d.device_id, "ppf_actual",
                        f"Calculated {d.ppf_actual} PPF is below the "
                        f"{d.ppf_target} PPF target"))
            except ValueError:
                out.append(Finding(Severity.WARNING, d.device_id, "ppf_actual",
                                   "Non-numeric pixel density value"))
    return out


def check_power_coherence(reg: DeviceRegister) -> list[Finding]:
    """PoE class and power source must agree, and locally powered devices need
    a power supply assigned."""
    out: list[Finding] = []
    for d in reg.devices:
        src = (d.power_source or "").upper()
        if d.poe_class and d.poe_class.lower() != "none":
            if not d.expects_poe:
                out.append(Finding(
                    Severity.WARNING, d.device_id, "poe_class",
                    f"PoE class on '{d.device_type}', which is not normally "
                    f"PoE powered"))
            if src and "POE" not in src:
                out.append(Finding(Severity.ERROR, d.device_id, "power_source",
                                   f"PoE class set but power_source is '{d.power_source}'"))
        if src.startswith("LOCAL") and not d.power_supply and reg.phase.order >= Phase.CD.order:
            out.append(Finding(Severity.ERROR, d.device_id, "power_supply",
                               "Locally powered device with no power supply assigned"))
    return out


def check_requirement_traceability(reg: DeviceRegister) -> list[Finding]:
    """Every device should trace to a requirement.

    An untraced device is either a gap in your RTM or a device nobody needs.
    Both are worth knowing about, which is why this is INFO rather than an
    error -- it's a prompt to think, not a defect.
    """
    return [
        Finding(Severity.INFO, d.device_id, "requirement_ids",
                "No requirement traced -- can you answer 'why is this here?'")
        for d in reg.devices if not d.requirement_ids and d.status != "REMOVE"
    ]


ALL_RULES = [
    check_duplicate_ids, check_id_format, check_unknown_types,
    check_required_fields, check_orphan_references, check_ip_addresses,
    check_switch_ports, check_door_completeness, check_camera_fields,
    check_power_coherence, check_requirement_traceability,
]


def validate(reg: DeviceRegister, rules=None) -> list[Finding]:
    findings: list[Finding] = []
    for rule in (rules or ALL_RULES):
        findings.extend(rule(reg))
    order = {Severity.ERROR: 0, Severity.WARNING: 1, Severity.INFO: 2}
    return sorted(findings, key=lambda f: (order[f.severity], f.device_id, f.field_name))


def report(findings: list[Finding], show_info: bool = False) -> str:
    counts = Counter(f.severity for f in findings)
    lines = ["", "=" * 92,
             f"DEVICE REGISTER VALIDATION -- "
             f"{counts[Severity.ERROR]} error(s), "
             f"{counts[Severity.WARNING]} warning(s), "
             f"{counts[Severity.INFO]} info",
             "=" * 92]
    shown = [f for f in findings
             if show_info or f.severity is not Severity.INFO]
    if not shown:
        lines.append("No findings at this severity. "
                     "(This does not mean the design is correct -- "
                     "only that the data is internally consistent.)")
    else:
        lines.extend(str(f) for f in shown)
    if counts[Severity.INFO] and not show_info:
        lines.append(f"\n({counts[Severity.INFO]} INFO findings hidden; "
                     f"pass --info to show)")
    lines.append("=" * 92)
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    show_info = "--info" in argv
    if not args:
        print(__doc__)
        return 2
    path = args[0]
    phase = Phase(args[1].upper()) if len(args) > 1 else Phase.CD
    reg = DeviceRegister.from_csv(path, phase=phase)
    findings = validate(reg)
    print(f"\nLoaded {len(reg.devices)} devices from {path} (phase {phase.value})")
    print(report(findings, show_info=show_info))
    return 1 if any(f.severity is Severity.ERROR for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
