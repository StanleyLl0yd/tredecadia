#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the read-only M4 stable preflight reporter across release states."""

from __future__ import annotations

import copy
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import stable_preflight  # noqa: E402


def evaluate_with_state(plan: dict, observation: dict, as_of: datetime) -> dict:
    """Evaluate one synthetic gate state without mutating repository files."""
    original_load = stable_preflight.load

    def synthetic_load(path: str) -> dict:
        if path == "release/stable-plan.json":
            return plan
        if path == plan["observation"]["record"]:
            return observation
        return original_load(path)

    stable_preflight.load = synthetic_load
    try:
        return stable_preflight.evaluate(as_of)
    finally:
        stable_preflight.load = original_load


def main() -> None:
    original_load = stable_preflight.load
    base_plan = copy.deepcopy(original_load("release/stable-plan.json"))
    base_observation = copy.deepcopy(original_load(base_plan["observation"]["record"]))

    assert base_plan["sourceRc"]["version"] == "1.0.0-rc.2"
    assert base_plan["sourceRc"]["publicationStatus"] == "published"
    assert base_plan["targetVersion"] == "1.0.0"
    assert base_observation["window"]["notBefore"] == "2026-09-17T09:44:59Z"

    before_gate = datetime(2026, 9, 16, 12, 0, 0, tzinfo=timezone.utc)
    after_gate = datetime(2026, 9, 17, 12, 0, 0, tzinfo=timezone.utc)

    # State 1: published RC2, observation open, before the one-full-day gate.
    open_plan = copy.deepcopy(base_plan)
    open_observation = copy.deepcopy(base_observation)
    open_observation["window"]["status"] = "open"
    open_observation["window"]["completedAt"] = None
    open_observation["reports"] = []
    open_observation["summary"] = {
        "compatibilityCriticalDefectsFound": 0,
        "compatibilityCriticalDefectsOpen": 0,
        "openReports": 0,
        "stableDecision": "pending",
    }
    open_plan["observation"] = {
        "status": "open",
        "stableDecision": "pending",
        "record": "release/rc-observation.json",
        "evidence": [],
    }
    open_plan["publication"]["allowed"] = False

    result = evaluate_with_state(open_plan, open_observation, before_gate)
    assert result["sourceRc"] == "v1.0.0-rc.2"
    assert result["target"] == "v1.0.0"
    assert result["ready"] is False
    assert result["compatibilityCriticalDefectsFound"] == 0
    assert result["compatibilityCriticalDefectsOpen"] == 0

    blockers = {entry["code"]: entry["detail"] for entry in result["blockers"]}
    assert set(blockers) == {
        "rc-observation-open",
        "minimum-observation-time-not-reached",
        "stable-decision-not-approved",
        "publication-gate-closed",
    }, blockers
    assert "2026-09-17T09:44:59Z" in blockers["minimum-observation-time-not-reached"]
    assert "pending-localization-decisions" not in blockers
    assert "rc2-not-published" not in blockers
    assert "open-rc-reports" not in blockers
    assert "pages-external-enablement-required" not in blockers

    # State 2: time gate elapsed but observation still explicitly open.
    later = evaluate_with_state(open_plan, open_observation, after_gate)
    later_codes = {entry["code"] for entry in later["blockers"]}
    assert later_codes == {
        "rc-observation-open",
        "stable-decision-not-approved",
        "publication-gate-closed",
    }, later["blockers"]
    assert later["ready"] is False

    # State 3: clean observation completed and approved, publication gate open.
    ready_plan = copy.deepcopy(base_plan)
    ready_observation = copy.deepcopy(base_observation)
    ready_observation["window"]["status"] = "complete"
    ready_observation["window"]["completedAt"] = ready_observation["window"]["notBefore"]
    ready_observation["reports"] = []
    ready_observation["summary"] = {
        "compatibilityCriticalDefectsFound": 0,
        "compatibilityCriticalDefectsOpen": 0,
        "openReports": 0,
        "stableDecision": "approved",
    }
    ready_plan["observation"] = {
        "status": "complete",
        "stableDecision": "approved",
        "record": "release/rc-observation.json",
        "evidence": ["synthetic-clean-review"],
    }
    ready_plan["publication"]["allowed"] = True

    ready = evaluate_with_state(ready_plan, ready_observation, after_gate)
    assert ready["blockers"] == [], ready["blockers"]
    assert ready["ready"] is True

    # State 4: a compatibility-critical finding invalidates this RC as a
    # stable baseline even if its individual report was later resolved.
    critical_plan = copy.deepcopy(ready_plan)
    critical_observation = copy.deepcopy(ready_observation)
    critical_observation["reports"] = [
        {
            "id": "synthetic-critical",
            "area": "calendar-identity",
            "summary": "synthetic compatibility-critical regression test",
            "classification": "compatibility-critical-defect",
            "status": "resolved",
            "compatibilityCritical": True,
            "evidence": ["synthetic-test"],
        }
    ]
    critical_observation["summary"] = {
        "compatibilityCriticalDefectsFound": 1,
        "compatibilityCriticalDefectsOpen": 0,
        "openReports": 0,
        "stableDecision": "approved",
    }

    critical = evaluate_with_state(critical_plan, critical_observation, after_gate)
    critical_blockers = {entry["code"]: entry["detail"] for entry in critical["blockers"]}
    assert set(critical_blockers) == {"compatibility-critical-defects-found"}, critical_blockers
    assert "synthetic-critical" in critical_blockers["compatibility-critical-defects-found"]
    assert critical["ready"] is False

    print("Tredecadia RC2/stable preflight state-machine validation: OK")


if __name__ == "__main__":
    main()
