#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the v1.1.0-rc.1 observation record and localization scope."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OBS = ROOT / "release" / "v1.1-rc1-observation.json"

BASELINE = {"ru-Cyrl", "ja-Kana", "ko-Hang"}
CANDIDATES = {"ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"}
CLASSIFICATIONS = {
    "compatibility-critical-defect",
    "compatible-correction",
    "editorial-issue",
    "non-blocking-future-work",
}
REPORT_STATUSES = {"open", "resolved", "deferred"}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    assert parsed.tzinfo is not None
    return parsed.astimezone(timezone.utc)


def main() -> None:
    observation = load("release/v1.1-rc1-observation.json")
    ledger = load("release/published-releases.json")
    localizations = load("registry/localizations.json")
    publish = load("release/publish.json")

    assert observation["schemaVersion"] == 1
    source = observation["sourceRc"]
    assert source["version"] == "1.1.0-rc.1"
    assert source["tag"] == "v1.1.0-rc.1"
    assert source["publicationStatus"] == "published"
    assert source["commit"] == "8d1b5a0c05eab8875e95b9896fd1c386edfe1220"
    assert source["publishedAt"] == "2026-09-18T08:01:59Z"
    assert source["archive"] == "tredecadia-1.1.0-rc.1.tar.gz"
    assert source["archiveSha256"] == "5b32dad3438572b67381ef5af05bf6fd915a2393fc69c8c132b7bef125ff876e"

    ledger_entry = next(item for item in ledger["releases"] if item["version"] == source["version"])
    for key in ("version", "tag", "commit", "publishedAt", "archive", "archiveSha256"):
        assert ledger_entry[key] == source[key]

    assert observation["stableTarget"] == "1.1.0"
    window = observation["window"]
    assert window["minimumDays"] == 1
    assert window["status"] in {"open", "complete"}
    assert (parse_utc(window["notBefore"]) - parse_utc(source["publishedAt"])).total_seconds() == 86400
    if window["status"] == "open":
        assert window["completedAt"] is None
    else:
        assert parse_utc(window["completedAt"]) >= parse_utc(window["notBefore"])

    assert set(observation["classifications"]) == CLASSIFICATIONS
    scope = observation["scope"]
    assert set(scope["stableBaselineProfiles"]) == BASELINE
    assert set(scope["reviewedCandidateProfiles"]) == CANDIDATES
    assert scope["weekdayAliasesIncluded"] is False
    assert scope["canonicalIdentityChanged"] is False

    reports = observation["reports"]
    critical_found = critical_open = open_reports = 0
    seen: set[str] = set()
    for report in reports:
        assert set(report) == {
            "id", "area", "summary", "classification", "status",
            "compatibilityCritical", "evidence",
        }
        assert report["id"] not in seen
        seen.add(report["id"])
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
    assert not (critical_found and summary["stableDecision"] == "approved")
    if window["status"] == "open":
        assert summary["stableDecision"] == "pending"
    elif summary["stableDecision"] == "approved":
        assert critical_found == critical_open == open_reports == 0

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == BASELINE | CANDIDATES
    for profile_id in BASELINE:
        assert profiles[profile_id]["review"]["status"] == "stable"
    for profile_id in CANDIDATES:
        assert profiles[profile_id]["review"]["status"] == "reviewed"

    assert publish == {
        "version": "1.1.0-rc.1",
        "tag": "v1.1.0-rc.1",
        "prerelease": True,
        "notes": "release/notes/1.1.0-rc.1.md",
    }

    print("Tredecadia v1.1.0-rc.1 observation validation: OK")


if __name__ == "__main__":
    main()
