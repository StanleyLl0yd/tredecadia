#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the M4 release-candidate observation record and feedback intake."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OBSERVATION = ROOT / "release" / "rc-observation.json"
STABLE_PLAN = ROOT / "release" / "stable-plan.json"
FEEDBACK_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "rc-feedback.yml"

CLASSIFICATIONS = {
    "compatibility-critical-defect",
    "compatible-correction",
    "editorial-issue",
    "non-blocking-future-work",
}
REPORT_STATUSES = {"open", "resolved", "deferred"}


def parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed.astimezone(timezone.utc)


def main() -> None:
    observation = json.loads(OBSERVATION.read_text(encoding="utf-8"))
    plan = json.loads(STABLE_PLAN.read_text(encoding="utf-8"))
    form = FEEDBACK_FORM.read_text(encoding="utf-8")

    assert observation["schemaVersion"] == 1
    assert observation["sourceRc"] == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "publishedAt": "2026-09-15T20:21:58Z",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
    }
    assert plan["sourceRc"]["version"] == observation["sourceRc"]["version"]
    assert plan["sourceRc"]["tag"] == observation["sourceRc"]["tag"]
    assert plan["sourceRc"]["commit"] == observation["sourceRc"]["commit"]
    assert plan["sourceRc"]["archiveSha256"] == observation["sourceRc"]["archiveSha256"]

    window = observation["window"]
    assert window["status"] in {"open", "complete"}
    assert window["minimumDays"] == 1
    published = parse_utc(observation["sourceRc"]["publishedAt"])
    not_before = parse_utc(window["notBefore"])
    assert (not_before - published).total_seconds() == 86400

    assert set(observation["classifications"]) == CLASSIFICATIONS

    reports = observation["reports"]
    assert isinstance(reports, list)
    ids: set[str] = set()
    critical_found = 0
    critical_open = 0
    open_reports = 0
    for report in reports:
        assert set(report) == {
            "id",
            "area",
            "summary",
            "classification",
            "status",
            "compatibilityCritical",
            "evidence",
        }
        assert report["id"] not in ids
        ids.add(report["id"])
        assert report["classification"] in CLASSIFICATIONS
        assert report["status"] in REPORT_STATUSES
        assert isinstance(report["compatibilityCritical"], bool)
        assert isinstance(report["evidence"], list) and report["evidence"]
        expected_critical = report["classification"] == "compatibility-critical-defect"
        assert report["compatibilityCritical"] is expected_critical
        if expected_critical:
            critical_found += 1
            if report["status"] == "open":
                critical_open += 1
        if report["status"] == "open":
            open_reports += 1

    summary = observation["summary"]
    assert summary["compatibilityCriticalDefectsFound"] == critical_found
    assert summary["compatibilityCriticalDefectsOpen"] == critical_open
    assert summary["openReports"] == open_reports
    assert summary["stableDecision"] in {"pending", "approved", "blocked"}

    for group in observation["postRcChangeGroups"]:
        assert isinstance(group["prs"], list) and group["prs"]
        assert all(isinstance(number, int) and number > 0 for number in group["prs"])
        assert group["classification"] in CLASSIFICATIONS
        assert group["area"] and group["summary"]

    if window["status"] == "open":
        assert window["completedAt"] is None
        assert summary["stableDecision"] == "pending"
        assert plan["observation"]["status"] == "open"
        assert plan["observation"]["stableDecision"] == "pending"
    else:
        assert isinstance(window["completedAt"], str)
        completed = parse_utc(window["completedAt"])
        assert completed >= not_before, "RC observation cannot complete before its minimum window"
        assert open_reports == 0, "completed RC observation may not have unresolved reports"
        assert critical_open == 0
        assert summary["stableDecision"] in {"approved", "blocked"}
        assert plan["observation"]["status"] == "complete"
        assert plan["observation"]["stableDecision"] == summary["stableDecision"]

    assert plan["observation"]["record"] == "release/rc-observation.json"

    # Keep feedback intake available and anchored to the actual RC.
    for needle in (
        "name: Tredecadia RC feedback",
        "v1.0.0-rc.1",
        "Calendar structure or date conversion",
        "Localization or writing system",
        "Accessibility or human presentation",
        "Packaging or release artifacts",
        "Documentation or translation",
    ):
        assert needle in form, f"RC feedback form missing {needle!r}"

    print("Tredecadia RC observation validation: OK")


if __name__ == "__main__":
    main()
