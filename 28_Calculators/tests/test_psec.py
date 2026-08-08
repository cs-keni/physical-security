"""Tests for the psec calculators.

Run:  python3 -m unittest discover -s 28_Calculators -v
  or: python3 28_Calculators/tests/test_psec.py

Expected values are hand-computed in the corresponding 32_Engineering_Math
lessons. If a test fails after you change a formula, work the hand calculation
again before you change the test -- the test is the record of the derivation.
"""

import math
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from psec import optics, power, pps, video  # noqa: E402


class TestOptics(unittest.TestCase):

    def test_angle_of_view_known_case(self):
        # 1/2.8" sensor (5.37 mm wide), 4 mm lens.
        # AOV = 2*atan(5.37 / 8) = 2*atan(0.67125) = 2*33.87 = 67.7 deg
        aov = optics.angle_of_view_deg(5.37, 4.0)
        self.assertAlmostEqual(aov, 67.74, places=1)

    def test_fov_width_similar_triangles(self):
        # W = D * w / f = 50 * 5.37 / 4 = 67.125 ft
        w = optics.fov_width_ft(50.0, 5.37, 4.0)
        self.assertAlmostEqual(w, 67.125, places=3)

    def test_focal_length_inverts_fov_width(self):
        f = optics.focal_length_for_width_mm(50.0, 67.125, 5.37)
        self.assertAlmostEqual(f, 4.0, places=6)

    def test_pixel_density(self):
        # 1920 px across 67.125 ft = 28.6 PPF
        ppf = optics.pixel_density_ppf(1920, 67.125)
        self.assertAlmostEqual(ppf, 28.604, places=2)

    def test_ppf_ppm_round_trip(self):
        self.assertAlmostEqual(optics.ppm_to_ppf(optics.ppf_to_ppm(40.0)), 40.0, places=9)

    def test_dori_table_matches_iec_conversion(self):
        # The per-foot table must be the px/m figures converted, within rounding.
        for key in ("detect", "observe", "identify"):
            converted = optics.DORI_PPM[key] / optics.FEET_PER_METRE
            self.assertLess(abs(optics.DORI_PPF[key] - converted), 0.5,
                            f"{key}: {optics.DORI_PPF[key]} vs {converted:.2f}")

    def test_max_range_for_ppf(self):
        # D = px*f / (ppf * w) = 1920*4 / (38 * 5.37) = 7680 / 204.06 = 37.64 ft
        d = optics.max_range_for_ppf_ft(1920, 38.0, 5.37, 4.0)
        self.assertAlmostEqual(d, 37.636, places=2)

    def test_max_range_is_consistent_with_forward_calc(self):
        d = optics.max_range_for_ppf_ft(1920, 38.0, 5.37, 4.0)
        ppf = optics.pixel_density_ppf(1920, optics.fov_width_ft(d, 5.37, 4.0))
        self.assertAlmostEqual(ppf, 38.0, places=6)

    def test_classify_ppf_boundaries(self):
        self.assertEqual(optics.classify_ppf(80), "identify")
        self.assertEqual(optics.classify_ppf(76), "identify")
        self.assertEqual(optics.classify_ppf(75.9), "recognise")
        self.assertEqual(optics.classify_ppf(38), "recognise")
        self.assertEqual(optics.classify_ppf(19), "observe")
        self.assertEqual(optics.classify_ppf(8), "detect")
        self.assertEqual(optics.classify_ppf(7.9), "below detect")

    def test_slant_range(self):
        # 9 ft mount, 5 ft target plane, 30 ft away: hypot(30, 4) = 30.265
        self.assertAlmostEqual(optics.slant_range_ft(30, 9, 5), 30.2655, places=3)

    def test_slant_range_never_less_than_horizontal(self):
        for d in (1, 5, 20, 100):
            self.assertGreaterEqual(optics.slant_range_ft(d, 12, 5), d)

    def test_depression_angle(self):
        # atan((20-5)/30) = atan(0.5) = 26.57 deg
        self.assertAlmostEqual(optics.depression_angle_deg(30, 20, 5), 26.565, places=2)

    def test_depression_directly_below_is_90(self):
        self.assertEqual(optics.depression_angle_deg(0, 20, 5), 90.0)

    def test_camera_spec_report(self):
        cam = optics.CameraSpec("CAM-1", 1920, 1080, "1/2.8", 4.0, mount_height_ft=9.0)
        self.assertAlmostEqual(cam.megapixels, 2.0736, places=4)
        rows = cam.coverage_report([10.0, 30.0, 60.0])
        self.assertEqual(len(rows), 3)
        # PPF must fall monotonically with distance.
        self.assertGreater(rows[0]["ppf"], rows[1]["ppf"])
        self.assertGreater(rows[1]["ppf"], rows[2]["ppf"])

    def test_unknown_sensor_format_raises_with_help(self):
        cam = optics.CameraSpec("bad", 1920, 1080, "1/9.9", 4.0)
        with self.assertRaises(ValueError) as ctx:
            _ = cam.sensor_wh_mm
        self.assertIn("Known:", str(ctx.exception))

    def test_rejects_nonpositive_inputs(self):
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                optics.fov_width_ft(bad, 5.37, 4.0)
            with self.assertRaises(ValueError):
                optics.angle_of_view_deg(5.37, bad)


class TestVideo(unittest.TestCase):

    def test_gb_per_day_decimal(self):
        # 4 Mbps * 3600 * 24 / 8 / 1000 = 43.2 GB/day
        self.assertAlmostEqual(video.stream_gb_per_day(4.0), 43.2, places=6)

    def test_gb_per_day_binary_is_smaller_number(self):
        self.assertLess(video.stream_gb_per_day(4.0, decimal_gb=False),
                        video.stream_gb_per_day(4.0, decimal_gb=True))

    def test_binary_units_are_true_gibibytes(self):
        # A bitrate is decimal, so the intermediate megabytes are 10^6 bytes.
        # 4 Mbps * 3600 * 24 / 8 = 43 200 MB = 4.32e10 bytes.
        # GiB = 4.32e10 / 2^30 = 40.2331 GiB.
        # Dividing 43 200 by 1024 instead gives 42.1875, which is 4.86% high and
        # is neither GB nor GiB. See 32_Engineering_Math/04_storage.md.
        self.assertAlmostEqual(video.stream_gb_per_day(4.0, decimal_gb=False),
                               40.2331, places=3)

    def test_decimal_binary_gap_at_tb_scale_is_about_ten_percent(self):
        # 1 TB = 10^12 bytes, 1 TiB = 2^40 bytes; the ratio is 2^40/10^12
        # = 1.099511627776. This is the "classic ~10% error" the module warns
        # about, and the binary path must actually reproduce it.
        dec = video.stream_tb_for_retention(4.0, 30, decimal_tb=True)
        binr = video.stream_tb_for_retention(4.0, 30, decimal_tb=False)
        self.assertAlmostEqual(dec, 1.296, places=6)
        self.assertAlmostEqual(binr, 1.178705, places=5)
        self.assertAlmostEqual(dec / binr, 2 ** 40 / 1e12, places=9)

    def test_tb_for_retention(self):
        # 43.2 GB/day * 30 = 1296 GB = 1.296 TB
        self.assertAlmostEqual(video.stream_tb_for_retention(4.0, 30), 1.296, places=6)

    def test_h265_halves_bitrate(self):
        h264 = video.scale_bitrate_mbps(10.0, codec="h264")
        h265 = video.scale_bitrate_mbps(10.0, codec="h265")
        self.assertAlmostEqual(h265, h264 * video.H265_FACTOR, places=9)

    def test_frame_rate_scaling_is_sublinear(self):
        """Halving fps must reduce bitrate by LESS than half."""
        full = video.scale_bitrate_mbps(10.0, from_fps=30, to_fps=30)
        half = video.scale_bitrate_mbps(10.0, from_fps=30, to_fps=15)
        self.assertLess(half, full)
        self.assertGreater(half, full * 0.5)

    def test_unsupported_codec_raises(self):
        with self.assertRaises(ValueError):
            video.scale_bitrate_mbps(10.0, codec="mjpeg")

    def test_camera_group_peak_vs_average(self):
        g = video.CameraGroup("lot", count=10, bitrate_mbps=6.0, motion_duty_cycle=0.25)
        self.assertAlmostEqual(g.peak_bandwidth_mbps, 60.0)
        self.assertAlmostEqual(g.average_bandwidth_mbps, 15.0)

    def test_motion_duty_cycle_validated(self):
        with self.assertRaises(ValueError):
            video.CameraGroup("x", 1, 4.0, motion_duty_cycle=0.0)
        with self.assertRaises(ValueError):
            video.CameraGroup("x", 1, 4.0, motion_duty_cycle=1.5)

    def test_system_totals(self):
        sysm = video.VideoSystem()
        sysm.add(video.CameraGroup("indoor", 50, 6.0, retention_days=30))
        sysm.add(video.CameraGroup("outdoor", 30, 10.0, retention_days=30))
        s = sysm.summary()
        self.assertEqual(s["camera_count"], 80)
        self.assertAlmostEqual(s["peak_bandwidth_mbps"], 600.0, places=1)
        # 50 * 1.944 TB + 30 * 3.24 TB = 97.2 + 97.2 = 194.4 TB
        self.assertAlmostEqual(s["raw_storage_tb"], 194.4, places=1)

    def test_headroom_applied(self):
        sysm = video.VideoSystem(headroom=0.20)
        sysm.add(video.CameraGroup("g", 10, 4.0, retention_days=30))
        self.assertAlmostEqual(sysm.storage_with_headroom_tb(),
                               sysm.raw_storage_tb() * 1.2, places=9)

    def test_storage_range_brackets_point_estimate(self):
        sysm = video.VideoSystem()
        sysm.add(video.CameraGroup("g", 10, 4.0))
        lo, hi = sysm.storage_range_tb()
        point = sysm.storage_with_headroom_tb()
        self.assertLess(lo, point)
        self.assertGreater(hi, point)

    def test_retention_inverse_round_trips(self):
        groups = [video.CameraGroup("g", 20, 8.0, retention_days=45)]
        sysm = video.VideoSystem(groups=list(groups), headroom=0.0)
        needed = sysm.raw_storage_tb()
        days = video.retention_days_achievable(needed, groups)
        self.assertAlmostEqual(days, 45.0, places=6)

    def test_raid_efficiencies(self):
        sysm = video.VideoSystem()
        # RAID 5, 8 disks -> efficiency 7/8 -> raw = 100 / 0.875 = 114.29
        self.assertAlmostEqual(sysm.raid_raw_capacity_tb(100, "raid5", 8), 114.2857, places=3)
        # RAID 6, 8 disks -> 6/8 -> 133.33
        self.assertAlmostEqual(sysm.raid_raw_capacity_tb(100, "raid6", 8), 133.3333, places=3)
        # RAID 10 -> 0.5 -> 200
        self.assertAlmostEqual(sysm.raid_raw_capacity_tb(100, "raid10", 8), 200.0, places=6)

    def test_raid_disk_count_validation(self):
        sysm = video.VideoSystem()
        with self.assertRaises(ValueError):
            sysm.raid_raw_capacity_tb(100, "raid5", 2)
        with self.assertRaises(ValueError):
            sysm.raid_raw_capacity_tb(100, "raid6", 3)
        with self.assertRaises(ValueError):
            sysm.raid_raw_capacity_tb(100, "raid10", 5)


class TestPower(unittest.TestCase):

    def test_poe_budget_uses_class_allocation_by_default(self):
        d = power.PoEDevice("dome", 10, "at")
        self.assertAlmostEqual(d.budget_w_each, 30.0)
        self.assertAlmostEqual(d.total_w, 300.0)

    def test_poe_actual_draw_overrides_class(self):
        d = power.PoEDevice("dome", 10, "at", actual_draw_w=8.5)
        self.assertAlmostEqual(d.total_w, 85.0)

    def test_unknown_poe_class_raises(self):
        with self.assertRaises(ValueError):
            power.PoEDevice("x", 1, "poe5")

    def test_switch_detects_budget_exceeded(self):
        sw = power.PoESwitch("SW-1", port_count=24, poe_budget_w=370.0)
        sw.add(power.PoEDevice("ptz", 8, "bt_t3"))    # 8 * 60 = 480 W
        findings = sw.check()
        self.assertTrue(any("POE BUDGET EXCEEDED" in f for f in findings))

    def test_switch_detects_port_oversubscription(self):
        sw = power.PoESwitch("SW-2", port_count=8, poe_budget_w=1000.0)
        sw.add(power.PoEDevice("cam", 12, "af"))
        self.assertTrue(any("OVERSUBSCRIBED PORTS" in f for f in sw.check()))

    def test_switch_detects_insufficient_spare_ports(self):
        sw = power.PoESwitch("SW-3", port_count=24, poe_budget_w=1000.0,
                             spare_port_pct=0.20)
        sw.add(power.PoEDevice("cam", 22, "af"))   # 2 free, need ceil(4.8)=5
        self.assertTrue(any("INSUFFICIENT SPARE PORTS" in f for f in sw.check()))

    def test_clean_switch_has_no_findings(self):
        sw = power.PoESwitch("SW-4", port_count=48, poe_budget_w=740.0)
        sw.add(power.PoEDevice("cam", 24, "af"))   # 24 * 15.4 = 369.6 W, 50% util
        self.assertEqual(sw.check(), [])

    def test_voltage_drop_includes_round_trip_factor(self):
        # 2 * 12.9 * 0.5 A * 200 ft / 1624 CM (18 AWG) = 2580/1624 = 1.588 V
        vd = power.voltage_drop_v(0.5, 200, "18")
        self.assertAlmostEqual(vd, 1.5887, places=3)

    def test_voltage_drop_scales_linearly_with_length_and_current(self):
        base = power.voltage_drop_v(0.5, 100, "18")
        self.assertAlmostEqual(power.voltage_drop_v(0.5, 200, "18"), base * 2, places=9)
        self.assertAlmostEqual(power.voltage_drop_v(1.0, 100, "18"), base * 2, places=9)

    def test_heavier_conductor_drops_less(self):
        self.assertLess(power.voltage_drop_v(1.0, 200, "14"),
                        power.voltage_drop_v(1.0, 200, "18"))

    def test_voltage_at_load(self):
        v = power.voltage_at_load_v(24.0, 0.5, 200, "18")
        self.assertAlmostEqual(v, 24.0 - 1.5887, places=3)

    def test_max_run_length_is_self_consistent(self):
        L = power.max_run_length_ft(24.0, 0.5, "18", 21.6)
        v = power.voltage_at_load_v(24.0, 0.5, L, "18")
        self.assertAlmostEqual(v, 21.6, places=6)

    def test_max_run_rejects_impossible_target(self):
        with self.assertRaises(ValueError):
            power.max_run_length_ft(12.0, 1.0, "18", 12.0)

    def test_smallest_awg_selection(self):
        awg = power.smallest_awg_for_run(24.0, 1.0, 300, 21.6)
        # Verify the choice actually works and the next size smaller does not.
        self.assertGreaterEqual(power.voltage_at_load_v(24.0, 1.0, 300, awg), 21.6)
        smaller = [a for a in power.AWG_CIRCULAR_MILS
                   if power.AWG_CIRCULAR_MILS[a] < power.AWG_CIRCULAR_MILS[awg]]
        for a in smaller:
            self.assertLess(power.voltage_at_load_v(24.0, 1.0, 300, a), 21.6)

    def test_smallest_awg_raises_when_impossible(self):
        with self.assertRaises(ValueError):
            power.smallest_awg_for_run(12.0, 5.0, 5000, 11.0)

    def test_unknown_awg_raises(self):
        with self.assertRaises(ValueError):
            power.voltage_drop_v(1.0, 100, "42")

    def test_battery_sizing(self):
        loads = [power.Load("readers", 8, 0.10), power.Load("locks", 8, 0.25)]
        # standby = 0.8 + 2.0 = 2.8 A; 4 h -> 11.2 Ah; *1.25*1.25 = 17.5 Ah
        r = power.battery_ah_required(loads, standby_hours=4.0)
        self.assertAlmostEqual(r["standby_current_a"], 2.8, places=6)
        self.assertAlmostEqual(r["ah_raw"], 11.2, places=6)
        self.assertAlmostEqual(r["ah_required"], 17.5, places=4)

    def test_battery_alarm_component(self):
        loads = [power.Load("horn", 2, 0.05, alarm_a_each=0.90)]
        r = power.battery_ah_required(loads, standby_hours=24.0, alarm_minutes=5.0)
        self.assertAlmostEqual(r["alarm_current_a"], 1.8, places=6)
        self.assertGreater(r["ah_required"], r["ah_standby"])

    def test_battery_requires_loads(self):
        with self.assertRaises(ValueError):
            power.battery_ah_required([], standby_hours=4.0)

    def test_runtime_uses_usable_fraction(self):
        # 12 Ah * 0.8 / 2 A = 4.8 h
        self.assertAlmostEqual(power.runtime_hours(12.0, 2.0), 4.8, places=6)

    def test_power_supply_sizing_uses_worst_case(self):
        loads = [power.Load("locks", 10, 0.25, alarm_a_each=0.50)]
        r = power.power_supply_sizing(loads, headroom=0.25)
        self.assertAlmostEqual(r["design_current_a"], 5.0, places=6)
        self.assertAlmostEqual(r["recommended_supply_a"], 6.25, places=6)


class TestPPS(unittest.TestCase):

    def _warehouse_path(self):
        p = pps.AdversaryPath(
            "north dock",
            assessment_delay_s=20.0,
            adversary_description="two persons, hand tools, willing to be seen briefly",
        )
        p.add(pps.Task("climb fence", 20))
        p.add(pps.Task("cross yard", 40))
        p.add(pps.Task("force dock door", 150, detected_here=True,
                       detection_note="DPS + camera"))
        p.add(pps.Task("traverse floor", 60))
        p.add(pps.Task("cut cage", 200))
        p.add(pps.Task("load goods", 240))
        return p

    def test_total_task_time(self):
        self.assertAlmostEqual(self._warehouse_path().total_task_time_s, 710.0)

    def test_detection_time_includes_assessment(self):
        # 20 + 40 + 150 = 210, + 20 assessment = 230
        self.assertAlmostEqual(self._warehouse_path().detection_time_s, 230.0)

    def test_time_remaining(self):
        self.assertAlmostEqual(self._warehouse_path().time_remaining_s, 480.0)

    def test_timely_with_onsite_guard(self):
        r = self._warehouse_path().evaluate(response_time_s=300.0)
        self.assertTrue(r["timely"])
        self.assertAlmostEqual(r["margin_s"], 180.0)

    def test_not_timely_with_contract_patrol(self):
        r = self._warehouse_path().evaluate(response_time_s=1800.0)
        self.assertFalse(r["timely"])
        self.assertAlmostEqual(r["margin_s"], -1320.0)
        self.assertIn("NOT TIMELY", r["verdict"])

    def test_marginal_is_treated_as_not_timely(self):
        r = self._warehouse_path().evaluate(response_time_s=420.0,
                                            required_margin_s=120.0)
        self.assertFalse(r["timely"])
        self.assertIn("MARGINAL", r["verdict"])

    def test_no_detection_path(self):
        p = pps.AdversaryPath("blind path")
        p.add(pps.Task("walk in", 30))
        p.add(pps.Task("take it", 60))
        r = p.evaluate(response_time_s=60.0)
        self.assertFalse(r["timely"])
        self.assertIsNone(r["detection_time_s"])
        self.assertIn("NO DETECTION", r["verdict"])

    def test_required_detection_point(self):
        # T_T 710 - T_R 300 - margin 60 = 350 s
        p = self._warehouse_path()
        self.assertAlmostEqual(p.required_detection_point_s(300.0, 60.0), 350.0)

    def test_detection_before_required_point_is_timely(self):
        p = self._warehouse_path()
        cutoff = p.required_detection_point_s(300.0, 60.0)
        self.assertLess(p.detection_time_s, cutoff)
        self.assertTrue(p.evaluate(300.0, 60.0)["timely"])

    def test_timeline_is_cumulative_and_complete(self):
        rows = self._warehouse_path().timeline()
        self.assertEqual(len(rows), 6)
        self.assertAlmostEqual(rows[0]["start_s"], 0.0)
        self.assertAlmostEqual(rows[-1]["end_s"], 710.0)
        for a, b in zip(rows, rows[1:]):
            self.assertAlmostEqual(a["end_s"], b["start_s"])

    def test_compare_interventions_offers_all_four_levers(self):
        out = compare = pps.compare_interventions(self._warehouse_path(), 1800.0)
        self.assertFalse(out["already_timely"])
        self.assertAlmostEqual(out["deficit_s"], 1320.0)
        for lever in ("earlier_detection", "more_delay_after_detection",
                      "faster_response", "reduce_consequence"):
            self.assertIn(lever, compare["levers"])

    def test_compare_flags_infeasible_detection_lever(self):
        """When the deficit exceeds the whole path, say so instead of emitting
        a negative detection time."""
        out = pps.compare_interventions(self._warehouse_path(), 1800.0,
                                        required_margin_s=60.0)
        self.assertFalse(out["detection_lever_feasible"])
        self.assertLess(out["required_detection_point_s"], 0)
        self.assertIn("NOT ACHIEVABLE", out["levers"]["earlier_detection"])

    def test_compare_gives_actionable_detection_target_when_feasible(self):
        p = self._warehouse_path()
        # Response of 400 s: cutoff = 710 - 400 - 60 = 250 s, which is > 0 and
        # earlier than the current T_D of 230 s... so already timely. Use 500 s:
        # cutoff = 150 s, T_D = 230 s -> feasible but must move earlier.
        out = pps.compare_interventions(p, 500.0, required_margin_s=60.0)
        self.assertTrue(out["detection_lever_feasible"])
        self.assertAlmostEqual(out["required_detection_point_s"], 150.0)
        self.assertIn("150", out["levers"]["earlier_detection"])

    def test_compare_short_circuits_when_already_timely(self):
        out = pps.compare_interventions(self._warehouse_path(), 300.0)
        self.assertTrue(out["already_timely"])

    def test_negative_delay_rejected(self):
        with self.assertRaises(ValueError):
            pps.Task("bad", -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
