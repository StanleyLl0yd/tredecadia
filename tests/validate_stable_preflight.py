#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the read-only M4 stable preflight reporter."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import stable_preflight  # noqa: E402


def main() -> None:
    # Freeze the test timestamp inside the active observation window so CI is
    # deterministic even after the real wall clock passes the minimum date.
    as_of = datetime(2026, 9, 16, 0, 0, 0, tzinfo=timezone.utc)
    result = stable_preflight.evaluate(as_of)

    assert result["sourceRc"] == "v1.0.0-rc.1"
    assert result["target"] == "v1.0.0"
    assert result["ready"] is False
    assert result["compatibilityCriticalDefectsFound"] == 0
    assert result["compatibilityCriticalDefectsOpen"] == 0

    blockers = {entry["code"]: entry["detail"] for entry in result["blockers"]}
    expected = {
        "rc-observation-open",
        "minimum-observation-time-not-reached",
        "open-rc-reports",
        "pending-localization-decisions",
        "pages-external-enablement-required",
        "stable-decision-not-approved",
        "publication-gate-closed",
    }
    assert set(blockers) == expected, blockers
    assert blockers["open-rc-reports"] == "obs-002"
    assert blockers["pending-localization-decisions"] == "ja-Kana, ko-Hang, ru-Cyrl"
    assert "2026-09-29T20:21:58Z" in blockers["minimum-observation-time-not-reached"]
    assert "GitHub Actions" in blockers["pages-external-enablement-required"]

    # The reporter must also preserve the temporal distinction: after the
    # minimum date the time blocker disappears, while the actual observation,
    # profile decisions, Pages prerequisite, and publication decision remain.
    later = stable_preflight.evaluate(datetime(2026, 9, 30, 0, 0, 0, tzinfo=timezone.utc))
    later_codes = {entry["code"] for entry in later["blockers"]}
    assert "minimum-observation-time-not-reached" not in later_codes
    assert later["ready"] is False
    assert "rc-observation-open" in later_codes
    assert "pending-localization-decisions" in later_codes
    assert "pages-external-enablement-required" in later_codes
    assert "publication-gate-closed" in later_codes

    print("Tredecadia stable preflight validation: OK")


if __name__ == "__main__":
    main()
