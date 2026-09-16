#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Report the current Tredecadia v1 stable-release blockers.

This tool is read-only. It summarizes the machine-readable M4 gates; it never
changes a decision or authorizes publication.
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
    plan = load("release/stable-plan.json")
    observation = load(plan["observation"]["record"])
    profile_readiness = load("release/profile-readiness.json")
    pages_text = (ROOT / "release/pages-deployment.md").read_text(encoding="utf-8")

    blockers: list[dict] = []

    window = observation["window"]
    not_before = parse_utc(window["notBefore"])
    if window["status"] != "complete":
        blockers.append({
            "code": "rc-observation-open",
            "detail": f"RC observation status is {window['status']}",
        })
    if as_of < not_before:
        blockers.append({
            "code": "minimum-observation-time-not-reached",
            "detail": f"earliest completion is {window['notBefore']}",
        })

    open_reports = [report["id"] for report in observation["reports"] if report["status"] == "open"]
    if open_reports:
        blockers.append({
            "code": "open-rc-reports",
            "detail": ", ".join(open_reports),
        })

    critical_open = [
        report["id"]
        for report in observation["reports"]
        if report["compatibilityCritical"] and report["status"] == "open"
    ]
    if critical_open:
        blockers.append({
            "code": "open-compatibility-critical-defects",
            "detail": ", ".join(critical_open),
        })

    plan_profiles = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    packet_profiles = {entry["id"]: entry for entry in profile_readiness["profiles"]}
    pending_profiles: list[str] = []
    for profile_id, plan_entry in sorted(plan_profiles.items()):
        packet = packet_profiles[profile_id]
        if plan_entry["stableDecision"] == "pending" or packet["decision"] == "pending":
            pending_profiles.append(profile_id)
    if pending_profiles:
        blockers.append({
            "code": "pending-localization-decisions",
            "detail": ", ".join(pending_profiles),
        })

    if "Status: **external-enable-required**" in pages_text:
        blockers.append({
            "code": "pages-external-enablement-required",
            "detail": "Settings → Pages → Build and deployment → Source → GitHub Actions",
        })

    if plan["observation"]["stableDecision"] != "approved":
        blockers.append({
            "code": "stable-decision-not-approved",
            "detail": plan["observation"]["stableDecision"],
        })

    if plan["publication"]["allowed"] is not True:
        blockers.append({
            "code": "publication-gate-closed",
            "detail": "release/stable-plan.json publication.allowed is false",
        })

    return {
        "asOf": as_of.isoformat().replace("+00:00", "Z"),
        "sourceRc": observation["sourceRc"]["tag"],
        "target": plan["publication"]["targetTag"],
        "ready": len(blockers) == 0,
        "compatibilityCriticalDefectsFound": observation["summary"]["compatibilityCriticalDefectsFound"],
        "compatibilityCriticalDefectsOpen": observation["summary"]["compatibilityCriticalDefectsOpen"],
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
        print(f"Tredecadia stable preflight: {state}")
        print(f"source: {result['sourceRc']}  target: {result['target']}")
        print(
            "compatibility-critical defects: "
            f"{result['compatibilityCriticalDefectsOpen']} open / "
            f"{result['compatibilityCriticalDefectsFound']} found"
        )
        for blocker in result["blockers"]:
            print(f"- {blocker['code']}: {blocker['detail']}")

    return 0 if result["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
