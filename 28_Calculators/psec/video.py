"""Video bandwidth, storage and retention calculations.

Derivations in ../../32_Engineering_Math/03_bandwidth.md and 04_storage.md.

THE MOST IMPORTANT THING ON THIS PAGE
-------------------------------------
Every number this module produces is an ESTIMATE built on an assumed bitrate,
and real bitrate depends on scene content, motion, noise, lighting, codec
implementation, and encoder tuning -- none of which you know at design time.
Two vendors' calculators will disagree by 2x on the same camera. That is not a
bug in either; it reflects genuine uncertainty.

Therefore:
  * Always present storage as a RANGE, not a value.
  * Always state your assumed bitrate and where it came from.
  * Always add explicit headroom (see ``DEFAULT_HEADROOM``) and say so.
  * Never let a vendor calculator's precision fool you or your client.

A design that is 30% short on storage silently shortens retention, and nobody
finds out until they need day-28 video and it is gone.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Bits/bytes. Network rates are decimal (Mbps = 10^6 bits/s); storage vendors
# sell decimal TB but operating systems report binary TiB. Mixing these is a
# classic ~10% error at the TB scale. This module is explicit about both.
BITS_PER_BYTE = 8
SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

# Decimal (SI) vs binary (IEC) conversion.
#
# A bitrate is decimal, so the "megabytes" that fall out of a bitrate
# calculation are 10^6 bytes each. Converting THOSE to gibibytes is a division
# by 2^30 / 10^6 = 1073.741824 -- NOT by 1024.
#
# Dividing decimal megabytes by 1024 is a common and subtle error: it produces a
# number that is neither GB nor GiB, and it understates the decimal/binary gap
# at the TB scale as ~4.9% instead of the true ~9.95%. Derivation and the
# corrected worked values are in ../../32_Engineering_Math/04_storage.md.
MB_TO_GB_DECIMAL = 1000.0            # 10^6 bytes -> 10^9 bytes
MB_TO_GIB_BINARY = 2 ** 30 / 1e6     # 10^6 bytes -> 2^30 bytes = 1073.741824
GB_TO_TB_DECIMAL = 1000.0            # 10^9 bytes -> 10^12 bytes
GIB_TO_TIB_BINARY = 1024.0           # 2^30 bytes -> 2^40 bytes

DEFAULT_HEADROOM = 0.20  # 20% -- covers estimate error, growth, and filesystem overhead

# Rough per-stream bitrate references in Mbps for H.264, moderate motion,
# good lighting, VBR with a quality target. [PRACTICE] -- starting points only.
# ALWAYS prefer the actual camera datasheet or a measured stream from a pilot.
# H.265 typically achieves the same subjective quality at roughly 40-50% of the
# H.264 bitrate; smart/zipstream-type codecs can go far lower on static scenes
# and much higher on busy ones.
TYPICAL_H264_MBPS: dict[str, float] = {
    "1MP_30fps": 4.0,
    "2MP_30fps": 6.0,     # 1080p
    "4MP_30fps": 10.0,
    "5MP_30fps": 12.0,
    "8MP_30fps": 18.0,    # 4K
    "12MP_30fps": 25.0,
}

H265_FACTOR = 0.5        # [PRACTICE] conservative; vendors claim 0.4-0.6
SMART_CODEC_FACTOR = 0.5  # [PRACTICE] highly scene-dependent; 0.2-0.8 in reality


# ---------------------------------------------------------------------------
# Bitrate
# ---------------------------------------------------------------------------

def scale_bitrate_mbps(base_mbps: float, *, from_fps: float = 30.0,
                       to_fps: float = 30.0, codec: str = "h264",
                       smart_codec: bool = False) -> float:
    """Adjust a reference bitrate for frame rate and codec.

    Frame-rate scaling is deliberately SUB-LINEAR. Halving frame rate does not
    halve bitrate, because inter-frame prediction gets less efficient when
    successive frames differ more, and because I-frames and overhead do not
    scale. A square-root-ish relationship matches observed behaviour better than
    a linear one. [PRACTICE] -- this is a modelling choice, documented here so
    you can challenge it rather than inherit it silently.
    """
    _positive("base_mbps", base_mbps)
    _positive("from_fps", from_fps)
    _positive("to_fps", to_fps)

    ratio = to_fps / from_fps
    rate = base_mbps * (ratio ** 0.7)

    codec = codec.lower()
    if codec in ("h265", "hevc", "h.265"):
        rate *= H265_FACTOR
    elif codec not in ("h264", "avc", "h.264"):
        raise ValueError(f"Unsupported codec {codec!r}; use 'h264' or 'h265'")

    if smart_codec:
        rate *= SMART_CODEC_FACTOR
    return rate


def stream_gb_per_day(bitrate_mbps: float, hours_per_day: float = 24.0,
                      *, decimal_gb: bool = True) -> float:
    """Storage consumed by one continuously recording stream, per day.

        GB/day = Mbps * 3600 * hours / 8 / 1000   (decimal GB)

    ``decimal_gb=False`` returns true GiB -- the intermediate megabytes are
    decimal (10^6 bytes), so the conversion divides by 2^30/10^6, not by 1024.
    GiB is what an operating system will report.
    """
    _positive("bitrate_mbps", bitrate_mbps)
    _nonneg("hours_per_day", hours_per_day)
    megabits = bitrate_mbps * SECONDS_PER_HOUR * hours_per_day
    megabytes = megabits / BITS_PER_BYTE
    return megabytes / (MB_TO_GB_DECIMAL if decimal_gb else MB_TO_GIB_BINARY)


def stream_tb_for_retention(bitrate_mbps: float, retention_days: float,
                            hours_per_day: float = 24.0,
                            *, decimal_tb: bool = True) -> float:
    """Storage for one stream held for ``retention_days``.

    ``decimal_tb=False`` returns TiB. Note the two conversion steps use
    different divisors: decimal MB -> GiB is 2^30/10^6, but GiB -> TiB is a
    clean 1024, because both are already binary.
    """
    _positive("retention_days", retention_days)
    per_day = stream_gb_per_day(bitrate_mbps, hours_per_day, decimal_gb=decimal_tb)
    return per_day * retention_days / (GB_TO_TB_DECIMAL if decimal_tb else GIB_TO_TIB_BINARY)


# ---------------------------------------------------------------------------
# Camera groups and systems
# ---------------------------------------------------------------------------

@dataclass
class CameraGroup:
    """A set of identically configured cameras.

    ``motion_duty_cycle`` models motion-triggered or motion-boosted recording:
    the fraction of the day the camera records at full bitrate. Use 1.0 for
    continuous recording. Anything below 1.0 is a RISK you should name explicitly
    to the client -- motion recording that misses the event is worthless, and
    poorly tuned motion detection misses events routinely.
    """
    name: str
    count: int
    bitrate_mbps: float
    hours_per_day: float = 24.0
    motion_duty_cycle: float = 1.0
    retention_days: float = 30.0

    def __post_init__(self) -> None:
        _positive("count", self.count)
        _positive("bitrate_mbps", self.bitrate_mbps)
        if not 0 < self.motion_duty_cycle <= 1.0:
            raise ValueError("motion_duty_cycle must be in (0, 1]")

    @property
    def effective_hours_per_day(self) -> float:
        return self.hours_per_day * self.motion_duty_cycle

    @property
    def peak_bandwidth_mbps(self) -> float:
        """All cameras streaming simultaneously at full rate.

        Size network links on PEAK, not average: motion events correlate (a car
        driving through a lot triggers six cameras at once), so the statistical
        smoothing you might hope for does not materialise when it matters.
        """
        return self.count * self.bitrate_mbps

    @property
    def average_bandwidth_mbps(self) -> float:
        return self.count * self.bitrate_mbps * self.motion_duty_cycle

    def storage_tb(self, *, decimal_tb: bool = True) -> float:
        per_cam = stream_tb_for_retention(
            self.bitrate_mbps, self.retention_days,
            self.effective_hours_per_day, decimal_tb=decimal_tb)
        return per_cam * self.count


@dataclass
class VideoSystem:
    """A whole video system, made of camera groups."""
    groups: list[CameraGroup] = field(default_factory=list)
    headroom: float = DEFAULT_HEADROOM

    def add(self, group: CameraGroup) -> "VideoSystem":
        self.groups.append(group)
        return self

    @property
    def camera_count(self) -> int:
        return sum(g.count for g in self.groups)

    @property
    def peak_bandwidth_mbps(self) -> float:
        return sum(g.peak_bandwidth_mbps for g in self.groups)

    @property
    def average_bandwidth_mbps(self) -> float:
        return sum(g.average_bandwidth_mbps for g in self.groups)

    def raw_storage_tb(self, *, decimal_tb: bool = True) -> float:
        return sum(g.storage_tb(decimal_tb=decimal_tb) for g in self.groups)

    def storage_with_headroom_tb(self, *, decimal_tb: bool = True) -> float:
        return self.raw_storage_tb(decimal_tb=decimal_tb) * (1 + self.headroom)

    def storage_range_tb(self, low: float = 0.7, high: float = 1.6,
                         *, decimal_tb: bool = True) -> tuple[float, float]:
        """Honest bounds on storage given bitrate uncertainty.

        The default multipliers reflect the real spread between an optimistic
        smart-codec estimate and a busy, noisy, low-light scene. Present THIS to
        clients, with the point estimate inside it.
        """
        base = self.storage_with_headroom_tb(decimal_tb=decimal_tb)
        return (base * low, base * high)

    def raid_raw_capacity_tb(self, usable_tb: float, raid_level: str,
                             disks_per_group: int) -> float:
        """Raw disk capacity needed for a usable capacity at a RAID level.

        RAID protects against DISK failure. It is not a backup, it does not
        protect against controller failure, chassis loss, fire, ransomware, or
        deletion, and during a rebuild the array is both slower and more
        vulnerable. Large-capacity drives take a long time to rebuild.
        """
        _positive("usable_tb", usable_tb)
        _positive("disks_per_group", disks_per_group)
        n = disks_per_group
        level = raid_level.lower().replace("raid", "").replace("-", "").strip()
        if level == "0":
            efficiency = 1.0
        elif level == "1":
            if n % 2:
                raise ValueError("RAID 1 needs an even disk count")
            efficiency = 0.5
        elif level == "5":
            if n < 3:
                raise ValueError("RAID 5 needs at least 3 disks")
            efficiency = (n - 1) / n
        elif level == "6":
            if n < 4:
                raise ValueError("RAID 6 needs at least 4 disks")
            efficiency = (n - 2) / n
        elif level == "10":
            if n < 4 or n % 2:
                raise ValueError("RAID 10 needs an even disk count >= 4")
            efficiency = 0.5
        else:
            raise ValueError(f"Unsupported RAID level {raid_level!r}")
        return usable_tb / efficiency

    def summary(self) -> dict:
        lo, hi = self.storage_range_tb()
        return {
            "camera_count": self.camera_count,
            "peak_bandwidth_mbps": round(self.peak_bandwidth_mbps, 1),
            "average_bandwidth_mbps": round(self.average_bandwidth_mbps, 1),
            "raw_storage_tb": round(self.raw_storage_tb(), 1),
            "storage_with_headroom_tb": round(self.storage_with_headroom_tb(), 1),
            "storage_range_tb": (round(lo, 1), round(hi, 1)),
            "headroom_pct": round(self.headroom * 100, 1),
        }


def retention_days_achievable(available_tb: float, groups: list[CameraGroup],
                              *, decimal_tb: bool = True) -> float:
    """Inverse problem: given the storage they already bought, how many days?

    This is the question you get asked most often on retrofit projects, and the
    answer is frequently much smaller than the client believes.
    """
    _positive("available_tb", available_tb)
    if not groups:
        raise ValueError("no camera groups supplied")
    tb_per_day = sum(
        stream_tb_for_retention(g.bitrate_mbps, 1.0, g.effective_hours_per_day,
                                decimal_tb=decimal_tb) * g.count
        for g in groups
    )
    if tb_per_day <= 0:
        raise ValueError("computed zero consumption; check inputs")
    return available_tb / tb_per_day


def _positive(name: str, value: float) -> None:
    if value is None or value <= 0:
        raise ValueError(f"{name} must be > 0 (got {value!r})")


def _nonneg(name: str, value: float) -> None:
    if value is None or value < 0:
        raise ValueError(f"{name} must be >= 0 (got {value!r})")
