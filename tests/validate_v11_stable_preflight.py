#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the read-only v1.1 stable preflight reporter."""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import v11_stable_preflight as preflight  # noqa: E402


def codes(result: dict) -> set[str]:
    return {item["code"] for item in result["blockers"]}


def main() -> None:
    before = preflight.evaluate(preflight.parse_utc("2026-09-18T12:00:00Z"))
    before_codes = codes(before)
    assert before["ready"] is False
    assert before["sourceRc"] == "v1.1.0-rc.1"
    assert before["target"] == "v1.1.0"
    assert before["compatibilityCriticalDefectsFound"] == 0
    assert before["compatibilityCriticalDefectsOpen"] == 0
    assert before["openReports"] == 0
    assert set(before["profileDecisions"].values()) == {"accepted"}
    assert "pending-localization-decisions" not in before_codes
    assert "localization-decision-mismatch" not in before_codes
    assert "minimum-observation-time-not-reached" in before_codes
    assert "rc-observation-open" in before_codes
    assert "stable-decision-not-approved" in before_codes
    assert "publication-gate-closed" in before_codes

    after_minimum = preflight.evaluate(preflight.parse_utc("2026-09-19T08:02:00Z"))
    after_codes = codes(after_minimum)
    assert after_minimum["ready"] is False
    assert "minimum-observation-time-not-reached" not in after_codes
    assert "rc-observation-open" in after_codes
    assert "stable-decision-not-approved" in after_codes
    assert "publication-gate-closed" in after_codes
    assert "pending-localization-decisions" not in after_codes

    # The preflight is reproducible and always reports an offset-aware UTC
    # timestamp regardless of the caller's offset.
    offset = preflight.evaluate(
        datetime.fromisoformat("2026-09-19T11:02:00+03:00")
    )
    assert offset["asOf"] == "2026-09-19T08:02:00Z"

    print("Tredecadia v1.1 stable preflight validation: OK")


if __name__ == "__main__":
    main()
