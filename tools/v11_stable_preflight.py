#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Report blockers for the Tredecadia v1.1 RC -> stable transition.

This tool is read-only. It summarizes the machine-readable M5 gates and never
changes observation state, localization decisions, or publication metadata.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def parse_utc(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError(f"timestamp must be timezone-aware: {value}")
    return dt.astimezone(timezone.utc)


def evaluate(as_of: datetime) -> dict:
    as_of = as_of.astimezone(timezone.utc)
    plan = load("release/v1.1-stable-plan.json")
    observation = load(plan["observation"]["record"])
    stable_decisions = load("rationale/v1.1-stable-profile-decisions.json")

    blockers: list[dict] = []
    source = observation["sourceRc"]
    window = observation["window"]
    summary = observation["summary"]

    if source["publicationStatus"] != "published":
        blockers.append({
            "code": "v11-rc-not-published",
            "detail": f"{source['tag']} publication status is {source['publicationStatus']}",
        })
    else:
        not_before = parse_utc(window["notBefore"])
        if as_of < not_before:
            blockers.append({
                "code": "minimum-observation-time-not-reached",
                "detail": f"earliest completion is {window['notBefore']}",
            })

    if window["status"] != "complete":
        blockers.append({
            "code": "rc-observation-open",
            "detail": f"RC observation status is {window['status']}",
        })

    open_reports = [report["id"] for report in observation["reports"] if report["status"] == "open"]
    if open_reports:
        blockers.append({"code": "open-rc-reports", "detail": ", ".join(open_reports)})

    critical_found = [
        report["id"] for report in observation["reports"]
        if report["compatibilityCritical"]
    ]
    if critical_found:
        blockers.append({
            "code": "compatibility-critical-defects-found",
            "detail": "new RC required: " + ", ".join(critical_found),
        })

    critical_open = [
        report["id"] for report in observation["reports"]
        if report["compatibilityCritical"] and report["status"] == "open"
    ]
    if critical_open:
        blockers.append({
            "code": "open-compatibility-critical-defects",
            "detail": ", ".join(critical_open),
        })

    plan_profiles = {item["id"]: item for item in plan["localizationProfiles"]}
    recorded_profiles = {item["id"]: item for item in stable_decisions["decisions"]}
    assert set(plan_profiles) == set(recorded_profiles)
    pending = sorted(
        profile_id
        for profile_id, item in plan_profiles.items()
        if item["stableDecision"] == "pending"
        or recorded_profiles[profile_id]["stableDecision"] == "pending"
    )
    if pending:
        blockers.append({
            "code": "pending-localization-decisions",
            "detail": ", ".join(pending),
        })

    mismatched = sorted(
        profile_id
        for profile_id, item in plan_profiles.items()
        if item["stableDecision"] != recorded_profiles[profile_id]["stableDecision"]
    )
    if mismatched:
        blockers.append({
            "code": "localization-decision-mismatch",
            "detail": ", ".join(mismatched),
        })

    if summary["stableDecision"] != "approved":
        blockers.append({
            "code": "stable-decision-not-approved",
            "detail": summary["stableDecision"],
        })

    if summary["compatibilityCriticalDefectsFound"] != 0:
        blockers.append({
            "code": "summary-critical-findings-nonzero",
            "detail": str(summary["compatibilityCriticalDefectsFound"]),
        })
    if summary["compatibilityCriticalDefectsOpen"] != 0:
        blockers.append({
            "code": "summary-critical-open-nonzero",
            "detail": str(summary["compatibilityCriticalDefectsOpen"]),
        })
    if summary["openReports"] != 0:
        blockers.append({
            "code": "summary-open-reports-nonzero",
            "detail": str(summary["openReports"]),
        })

    if plan["publication"]["allowed"] is not True:
        blockers.append({
            "code": "publication-gate-closed",
            "detail": "release/v1.1-stable-plan.json publication.allowed is false",
        })

    return {
        "asOf": as_of.isoformat().replace("+00:00", "Z"),
        "sourceRc": source["tag"],
        "target": plan["publication"]["targetTag"],
        "ready": len(blockers) == 0,
        "compatibilityCriticalDefectsFound": summary["compatibilityCriticalDefectsFound"],
        "compatibilityCriticalDefectsOpen": summary["compatibilityCriticalDefectsOpen"],
        "openReports": summary["openReports"],
        "profileDecisions": {
            profile_id: item["stableDecision"]
            for profile_id, item in sorted(plan_profiles.items())
        },
        "blockers": blockers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--as-of",
        help="UTC/offset-aware ISO timestamp for a reproducible preflight; defaults to current UTC time",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    as_of = parse_utc(args.as_of) if args.as_of else datetime.now(timezone.utc)
    result = evaluate(as_of)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        state = "READY" if result["ready"] else "BLOCKED"
        print(f"Tredecadia v1.1 stable preflight: {state}")
        print(f"source: {result['sourceRc']}  target: {result['target']}")
        print(
            "compatibility-critical defects: "
            f"{result['compatibilityCriticalDefectsOpen']} open / "
            f"{result['compatibilityCriticalDefectsFound']} found"
        )
        print(f"open reports: {result['openReports']}")
        for profile_id, decision in result["profileDecisions"].items():
            print(f"- profile {profile_id}: {decision}")
        for blocker in result["blockers"]:
            print(f"- {blocker['code']}: {blocker['detail']}")

    return 0 if result["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
