"""Camera optics and coverage calculations.

All formulas are derived in ../../32_Engineering_Math/01_camera_fov.md and
02_pixel_density.md. Do the derivations by hand before relying on this module.

Sign conventions and units
--------------------------
* Distances are in FEET unless a function name ends in ``_m`` (metres).
* Focal length and sensor dimensions are in MILLIMETRES.
* Angles are in DEGREES at the API boundary; radians internally.
* "Horizontal" is the default axis; vertical variants are provided explicitly.

Assumptions and limits
----------------------
* Thin-lens, rectilinear (undistorted) projection. Wide-angle lenses below roughly
  2.8 mm on a 1/2.8" sensor exhibit barrel distortion that this model does NOT
  capture; real coverage at the frame edge will differ. Fisheye lenses use an
  entirely different projection and must not be modelled with these functions.
* Pixel density is computed at a single target plane perpendicular to the optical
  axis. A real scene is oblique: density varies across the image. Use
  ``pixel_density_at_range`` per target distance, not once per camera.
* No allowance for lens MTF, focus error, motion blur, or compression loss. Those
  reduce *usable* detail below the geometric pixel count. Treat geometric pixel
  density as a necessary, not sufficient, condition.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Common sensor formats. Width x height of the imaging area in millimetres.
#
# NOTE: sensor "type" designations (1/2.8", 1/1.8", ...) are a legacy vidicon
# convention and do NOT equal the diagonal in inches. Values below are typical
# industry figures and vary by manufacturer -- for a real design, take the
# imager dimensions from the camera datasheet. [VERIFY per datasheet]
# ---------------------------------------------------------------------------
SENSOR_FORMATS_MM: dict[str, tuple[float, float]] = {
    "1/4": (3.60, 2.70),
    "1/3": (4.80, 3.60),
    "1/2.9": (5.02, 2.82),   # common 16:9 imager
    "1/2.8": (5.37, 3.02),   # very common 16:9 imager
    "1/2.7": (5.37, 3.02),
    "1/2.5": (5.76, 4.29),
    "1/2": (6.40, 4.80),
    "1/1.8": (7.20, 5.40),
    "1/1.7": (7.60, 5.70),
    "1/1.2": (10.67, 6.00),
    "2/3": (8.80, 6.60),
    "1": (13.20, 8.80),
}

# Common DORI-style pixel density targets, in pixels per FOOT (horizontal).
#
# [STANDARD] IEC 62676-4 defines DORI criteria in pixels per metre:
#   Detect 25 px/m, Observe 62.5 px/m, Recognise 125 px/m, Identify 250 px/m.
# [VERIFY current edition.] The per-foot values below are those figures converted
# (1 m = 3.28084 ft) and rounded to the values used in common practice.
#
# These are MINIMA for the stated task under good conditions. Many practitioners
# design above them; see ../../03_Video_Surveillance/04_dori_and_pixel_density.md
# for when to exceed them and why.
DORI_PPF: dict[str, float] = {
    "detect": 8.0,        # ~25 px/m   -- "is something there?"
    "observe": 19.0,      # ~62.5 px/m -- "what is it doing?"
    "recognise": 38.0,    # ~125 px/m  -- "is that someone I know?"
    "recognize": 38.0,    # US spelling alias
    "identify": 76.0,     # ~250 px/m  -- "who is that, to an unfamiliar viewer?"
}

DORI_PPM: dict[str, float] = {
    "detect": 25.0,
    "observe": 62.5,
    "recognise": 125.0,
    "recognize": 125.0,
    "identify": 250.0,
}

FEET_PER_METRE = 3.280839895013123


# ---------------------------------------------------------------------------
# Field of view
# ---------------------------------------------------------------------------

def angle_of_view_deg(sensor_dim_mm: float, focal_length_mm: float) -> float:
    """Angle of view for one sensor axis.

        AOV = 2 * arctan( d / (2 * f) )

    ``sensor_dim_mm`` is the sensor width for horizontal AOV, height for vertical.
    """
    _positive("sensor_dim_mm", sensor_dim_mm)
    _positive("focal_length_mm", focal_length_mm)
    return math.degrees(2.0 * math.atan(sensor_dim_mm / (2.0 * focal_length_mm)))


def fov_width_ft(distance_ft: float, sensor_width_mm: float,
                 focal_length_mm: float) -> float:
    """Horizontal scene width captured at ``distance_ft`` from the camera.

    Similar triangles:  W / D = w_sensor / f   =>   W = D * w_sensor / f

    Note this is the width on a plane perpendicular to the optical axis at that
    distance -- i.e. slant range, not floor distance. For a downward-tilted
    camera, convert first (see ``slant_range_ft``).
    """
    _positive("distance_ft", distance_ft)
    _positive("sensor_width_mm", sensor_width_mm)
    _positive("focal_length_mm", focal_length_mm)
    return distance_ft * sensor_width_mm / focal_length_mm


def focal_length_for_width_mm(distance_ft: float, desired_width_ft: float,
                              sensor_width_mm: float) -> float:
    """Focal length needed to capture ``desired_width_ft`` at ``distance_ft``.

    The inverse of :func:`fov_width_ft`. This is the function you actually use
    when designing: you know the scene you must cover and the distance you can
    mount at, and you need the lens.
    """
    _positive("distance_ft", distance_ft)
    _positive("desired_width_ft", desired_width_ft)
    _positive("sensor_width_mm", sensor_width_mm)
    return distance_ft * sensor_width_mm / desired_width_ft


def slant_range_ft(horizontal_distance_ft: float, mount_height_ft: float,
                   target_height_ft: float = 5.0) -> float:
    """Straight-line distance from the camera to a target's feature plane.

    ``target_height_ft`` defaults to 5.0 ft -- roughly face height for an adult,
    which is the plane that matters for recognition and identification. Use 0.0
    for a target at grade (e.g. a licence plate on a low-mounted plate).
    """
    _nonneg("horizontal_distance_ft", horizontal_distance_ft)
    _nonneg("mount_height_ft", mount_height_ft)
    _nonneg("target_height_ft", target_height_ft)
    dv = mount_height_ft - target_height_ft
    return math.hypot(horizontal_distance_ft, dv)


def depression_angle_deg(horizontal_distance_ft: float, mount_height_ft: float,
                         target_height_ft: float = 5.0) -> float:
    """Downward tilt from horizontal to the target's feature plane, in degrees.

    Design heuristic [PRACTICE], not a rule: depression angles beyond roughly
    30 deg increasingly foreshorten faces and make identification unreliable, no
    matter how many pixels are on target. High mounts defeat facial capture --
    which is exactly why identification cameras at doors are mounted low and
    aimed near-level, and why a 20 ft parking-lot pole camera will never identify
    anyone directly beneath it.
    """
    _nonneg("horizontal_distance_ft", horizontal_distance_ft)
    if horizontal_distance_ft == 0:
        return 90.0
    return math.degrees(math.atan((mount_height_ft - target_height_ft)
                                  / horizontal_distance_ft))


# ---------------------------------------------------------------------------
# Pixel density
# ---------------------------------------------------------------------------

def pixel_density_ppf(horizontal_pixels: int, fov_width_ft_value: float) -> float:
    """Horizontal pixels per foot across the scene.

        PPF = horizontal_pixels / scene_width_ft
    """
    _positive("horizontal_pixels", horizontal_pixels)
    _positive("fov_width_ft_value", fov_width_ft_value)
    return horizontal_pixels / fov_width_ft_value


def pixel_density_ppm(horizontal_pixels: int, fov_width_m: float) -> float:
    """Horizontal pixels per metre across the scene."""
    _positive("horizontal_pixels", horizontal_pixels)
    _positive("fov_width_m", fov_width_m)
    return horizontal_pixels / fov_width_m


def ppf_to_ppm(ppf: float) -> float:
    return ppf * FEET_PER_METRE


def ppm_to_ppf(ppm: float) -> float:
    return ppm / FEET_PER_METRE


def max_range_for_ppf_ft(horizontal_pixels: int, target_ppf: float,
                         sensor_width_mm: float, focal_length_mm: float) -> float:
    """Greatest distance at which ``target_ppf`` is still met.

    Combining PPF = px / W and W = D * w / f:

        D_max = (px * f) / (target_ppf * w_sensor)

    This is the number to put on a coverage diagram: beyond it, the camera no
    longer supports the task you specified.
    """
    _positive("horizontal_pixels", horizontal_pixels)
    _positive("target_ppf", target_ppf)
    _positive("sensor_width_mm", sensor_width_mm)
    _positive("focal_length_mm", focal_length_mm)
    return (horizontal_pixels * focal_length_mm) / (target_ppf * sensor_width_mm)


def classify_ppf(ppf: float) -> str:
    """Return the highest DORI class met at this pixel density."""
    if ppf >= DORI_PPF["identify"]:
        return "identify"
    if ppf >= DORI_PPF["recognise"]:
        return "recognise"
    if ppf >= DORI_PPF["observe"]:
        return "observe"
    if ppf >= DORI_PPF["detect"]:
        return "detect"
    return "below detect"


# ---------------------------------------------------------------------------
# Combined camera model
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CameraSpec:
    """A camera + lens + mounting configuration."""
    name: str
    horizontal_pixels: int
    vertical_pixels: int
    sensor_format: str                 # key into SENSOR_FORMATS_MM
    focal_length_mm: float
    mount_height_ft: float = 9.0

    @property
    def sensor_wh_mm(self) -> tuple[float, float]:
        try:
            return SENSOR_FORMATS_MM[self.sensor_format]
        except KeyError:
            raise ValueError(
                f"Unknown sensor format {self.sensor_format!r}. "
                f"Known: {sorted(SENSOR_FORMATS_MM)}. Add yours from the datasheet."
            ) from None

    @property
    def megapixels(self) -> float:
        return self.horizontal_pixels * self.vertical_pixels / 1_000_000

    @property
    def hfov_deg(self) -> float:
        return angle_of_view_deg(self.sensor_wh_mm[0], self.focal_length_mm)

    @property
    def vfov_deg(self) -> float:
        return angle_of_view_deg(self.sensor_wh_mm[1], self.focal_length_mm)

    def fov_width_ft_at(self, distance_ft: float) -> float:
        return fov_width_ft(distance_ft, self.sensor_wh_mm[0], self.focal_length_mm)

    def ppf_at(self, distance_ft: float) -> float:
        return pixel_density_ppf(self.horizontal_pixels,
                                 self.fov_width_ft_at(distance_ft))

    def max_range_ft(self, target: str | float) -> float:
        """Max distance meeting a DORI class name or a numeric PPF target."""
        ppf = DORI_PPF[target.lower()] if isinstance(target, str) else float(target)
        return max_range_for_ppf_ft(self.horizontal_pixels, ppf,
                                    self.sensor_wh_mm[0], self.focal_length_mm)

    def coverage_report(self, distances_ft: list[float],
                        target_height_ft: float = 5.0) -> list[dict]:
        """Per-distance coverage table, accounting for camera tilt.

        Uses slant range rather than floor distance, which matters as soon as the
        mount height is a meaningful fraction of the target distance -- i.e. for
        every indoor camera. Ignoring it overstates PPF for near targets.
        """
        rows = []
        for d in distances_ft:
            sr = slant_range_ft(d, self.mount_height_ft, target_height_ft)
            width = self.fov_width_ft_at(sr)
            ppf = pixel_density_ppf(self.horizontal_pixels, width)
            rows.append({
                "floor_distance_ft": round(d, 1),
                "slant_range_ft": round(sr, 1),
                "scene_width_ft": round(width, 1),
                "ppf": round(ppf, 1),
                "ppm": round(ppf_to_ppm(ppf), 1),
                "class": classify_ppf(ppf),
                "depression_deg": round(
                    depression_angle_deg(d, self.mount_height_ft, target_height_ft), 1),
            })
        return rows


# ---------------------------------------------------------------------------
# Guards
# ---------------------------------------------------------------------------

def _positive(name: str, value: float) -> None:
    if value is None or value <= 0:
        raise ValueError(f"{name} must be > 0 (got {value!r})")


def _nonneg(name: str, value: float) -> None:
    if value is None or value < 0:
        raise ValueError(f"{name} must be >= 0 (got {value!r})")
