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
    as_of = datetime(2026, 9, 16, 12, 0, 0, tzinfo=timezone.utc)
    result = stable_preflight.evaluate(as_of)

    assert result["sourceRc"] == "v1.0.0-rc.2"
    assert result["target"] == "v1.0.0"
    assert result["ready"] is False
    assert result["compatibilityCriticalDefectsFound"] == 0
    assert result["compatibilityCriticalDefectsOpen"] == 0

    blockers = {entry["code"]: entry["detail"] for entry in result["blockers"]}
    expected = {
        "rc2-not-published",
        "pending-localization-decisions",
        "stable-decision-not-approved",
        "publication-gate-closed",
    }
    assert set(blockers) == expected, blockers
    assert blockers["pending-localization-decisions"] == "ja-Kana, ko-Hang, ru-Cyrl"
    assert "v1.0.0-rc.2" in blockers["rc2-not-published"]
    assert "minimum-observation-time-not-reached" not in blockers
    assert "rc-observation-open" not in blockers
    assert "open-rc-reports" not in blockers
    assert "pages-external-enablement-required" not in blockers

    # Wall-clock time cannot satisfy an observation that has not started.
    much_later = stable_preflight.evaluate(datetime(2030, 1, 1, 0, 0, 0, tzinfo=timezone.utc))
    later_codes = {entry["code"] for entry in much_later["blockers"]}
    assert "rc2-not-published" in later_codes
    assert "minimum-observation-time-not-reached" not in later_codes
    assert much_later["ready"] is False

    print("Tredecadia RC2 prepublication stable preflight validation: OK")


if __name__ == "__main__":
    main()
