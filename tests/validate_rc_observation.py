#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the active RC2 observation record and feedback intake."""

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
    predecessor = json.loads((ROOT / observation["predecessorRecord"]).read_text(encoding="utf-8"))
    form = FEEDBACK_FORM.read_text(encoding="utf-8")

    assert observation["schemaVersion"] == 2
    source = observation["sourceRc"]
    assert source["version"] == "1.0.0-rc.2"
    assert source["tag"] == "v1.0.0-rc.2"
    assert source["publicationStatus"] in {"awaiting-publication", "published"}
    assert observation["predecessorRecord"] == "release/rc1-observation.json"
    assert predecessor["sourceRc"]["version"] == "1.0.0-rc.1"
    assert predecessor["sourceRc"]["commit"] == "937d8d681fcce6095d6a4d196783136b908c1be5"

    assert plan["sourceRc"]["version"] == source["version"]
    assert plan["sourceRc"]["tag"] == source["tag"]
    assert plan["sourceRc"]["publicationStatus"] == source["publicationStatus"]
    assert plan["sourceRc"]["commit"] == source["commit"]
    assert plan["sourceRc"]["archiveSha256"] == source["archiveSha256"]

    window = observation["window"]
    assert window["minimumDays"] == 1
    if source["publicationStatus"] == "awaiting-publication":
        assert source["commit"] is None
        assert source["publishedAt"] is None
        assert source["archiveSha256"] is None
        assert window == {
            "status": "awaiting-publication",
            "minimumDays": 1,
            "notBefore": None,
            "completedAt": None,
        }
        assert plan["observation"]["status"] == "awaiting-publication"
    else:
        assert isinstance(source["commit"], str) and len(source["commit"]) == 40
        assert isinstance(source["archiveSha256"], str) and len(source["archiveSha256"]) == 64
        published = parse_utc(source["publishedAt"])
        not_before = parse_utc(window["notBefore"])
        assert (not_before - published).total_seconds() == 86400
        assert window["status"] in {"open", "complete"}

    assert set(observation["classifications"]) == CLASSIFICATIONS

    reports = observation["reports"]
    ids: set[str] = set()
    critical_found = critical_open = open_reports = 0
    for report in reports:
        assert set(report) == {"id", "area", "summary", "classification", "status", "compatibilityCritical", "evidence"}
        assert report["id"] not in ids
        ids.add(report["id"])
        assert report["classification"] in CLASSIFICATIONS
        assert report["status"] in REPORT_STATUSES
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
    # Finding a compatibility-critical defect invalidates this RC as the
    # stable baseline even after the individual report is resolved. The only
    # valid path is a new RC, so this observation must never approve stable.
    assert not (critical_found and summary["stableDecision"] == "approved"), (
        "an RC with compatibility-critical findings cannot be approved for stable; publish a new RC"
    )

    classified_prs: set[int] = set()
    for group in observation["postRcChangeGroups"]:
        assert set(group) == {"prs", "classification", "area", "summary"}
        assert isinstance(group["prs"], list) and group["prs"]
        assert all(isinstance(number, int) and number > 0 for number in group["prs"])
        assert len(group["prs"]) == len(set(group["prs"])), f"duplicate PR inside change group: {group['prs']}"
        overlap = classified_prs.intersection(group["prs"])
        assert not overlap, f"PR classified in multiple post-RC groups: {sorted(overlap)}"
        classified_prs.update(group["prs"])
        assert group["classification"] in CLASSIFICATIONS
        assert group["area"] and group["summary"]

    if window["status"] in {"awaiting-publication", "open"}:
        assert window["completedAt"] is None
        assert summary["stableDecision"] == "pending"
        assert plan["observation"]["status"] == window["status"]
        assert plan["observation"]["stableDecision"] == "pending"
    else:
        completed = parse_utc(window["completedAt"])
        assert completed >= parse_utc(window["notBefore"])
        assert open_reports == 0
        assert critical_open == 0
        assert summary["stableDecision"] in {"approved", "blocked"}
        assert plan["observation"]["status"] == "complete"
        assert plan["observation"]["stableDecision"] == summary["stableDecision"]

    assert plan["observation"]["record"] == "release/rc-observation.json"
    for needle in (
        "name: Tredecadia RC feedback",
        "v1.0.0-rc.2",
        "Calendar structure or date conversion",
        "Localization or writing system",
        "Accessibility or human presentation",
        "Packaging or release artifacts",
        "Documentation or translation",
    ):
        assert needle in form, f"RC feedback form missing {needle!r}"

    print("Tredecadia RC2 observation validation: OK")


if __name__ == "__main__":
    main()
