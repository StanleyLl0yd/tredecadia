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
    # Deterministic point after RC2 publication but before the one-full-day
    # minimum observation interval has elapsed. Localization decisions are
    # already resolved independently of the time gate.
    as_of = datetime(2026, 9, 16, 12, 0, 0, tzinfo=timezone.utc)
    result = stable_preflight.evaluate(as_of)

    assert result["sourceRc"] == "v1.0.0-rc.2"
    assert result["target"] == "v1.0.0"
    assert result["ready"] is False
    assert result["compatibilityCriticalDefectsFound"] == 0
    assert result["compatibilityCriticalDefectsOpen"] == 0

    blockers = {entry["code"]: entry["detail"] for entry in result["blockers"]}
    expected = {
        "rc-observation-open",
        "minimum-observation-time-not-reached",
        "stable-decision-not-approved",
        "publication-gate-closed",
    }
    assert set(blockers) == expected, blockers
    assert "2026-09-17T09:44:59Z" in blockers["minimum-observation-time-not-reached"]
    assert "pending-localization-decisions" not in blockers
    assert "rc2-not-published" not in blockers
    assert "open-rc-reports" not in blockers
    assert "pages-external-enablement-required" not in blockers

    # After one full day only the time blocker disappears. The observation
    # still has to be explicitly completed and approved before publication.
    later = stable_preflight.evaluate(datetime(2026, 9, 17, 12, 0, 0, tzinfo=timezone.utc))
    later_codes = {entry["code"] for entry in later["blockers"]}
    assert "minimum-observation-time-not-reached" not in later_codes
    assert "rc-observation-open" in later_codes
    assert "pending-localization-decisions" not in later_codes
    assert "stable-decision-not-approved" in later_codes
    assert "publication-gate-closed" in later_codes
    assert later["ready"] is False

    print("Tredecadia published RC2 stable preflight validation: OK")


if __name__ == "__main__":
    main()
