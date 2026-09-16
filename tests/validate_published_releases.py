#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate immutable metadata and source locks for already-published releases."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build_release  # noqa: E402

RC1 = {
    "version": "1.0.0-rc.1",
    "tag": "v1.0.0-rc.1",
    "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
    "publishedAt": "2026-09-15T20:21:58Z",
    "archive": "tredecadia-1.0.0-rc.1.tar.gz",
    "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
}


def main() -> None:
    data = json.loads((ROOT / "release/published-releases.json").read_text(encoding="utf-8"))
    assert data["schemaVersion"] == 1
    releases = data["releases"]
    assert releases and releases[0] == RC1
    assert len({entry["version"] for entry in releases}) == len(releases)
    assert len({entry["tag"] for entry in releases}) == len(releases)

    plan = json.loads((ROOT / "release/stable-plan.json").read_text(encoding="utf-8"))
    active_observation = json.loads((ROOT / "release/rc-observation.json").read_text(encoding="utf-8"))
    rc1_observation = json.loads((ROOT / "release/rc1-observation.json").read_text(encoding="utf-8"))

    predecessor = plan["predecessorRc"]
    assert predecessor["version"] == RC1["version"]
    assert predecessor["tag"] == RC1["tag"]
    assert predecessor["commit"] == RC1["commit"]
    assert predecessor["archiveSha256"] == RC1["archiveSha256"]
    assert predecessor["observationRecord"] == "release/rc1-observation.json"
    for key in ("version", "tag", "commit", "publishedAt", "archiveSha256"):
        assert rc1_observation["sourceRc"][key] == RC1[key]

    rc2_entries = [entry for entry in releases if entry["version"] == "1.0.0-rc.2"]
    assert len(rc2_entries) <= 1
    if rc2_entries:
        rc2 = rc2_entries[0]
        assert rc2["tag"] == "v1.0.0-rc.2"
        assert rc2["archive"] == "tredecadia-1.0.0-rc.2.tar.gz"
        assert len(rc2["commit"]) == 40
        assert len(rc2["archiveSha256"]) == 64
        assert plan["sourceRc"]["publicationStatus"] == "published"
        assert active_observation["sourceRc"]["publicationStatus"] == "published"
        for key in ("version", "tag", "commit", "archiveSha256"):
            assert plan["sourceRc"][key] == rc2[key]
            assert active_observation["sourceRc"][key] == rc2[key]
        assert active_observation["sourceRc"]["publishedAt"] == rc2["publishedAt"]
    else:
        assert plan["sourceRc"] == {
            "version": "1.0.0-rc.2",
            "tag": "v1.0.0-rc.2",
            "publicationStatus": "awaiting-publication",
            "commit": None,
            "archiveSha256": None,
        }
        assert active_observation["sourceRc"]["publicationStatus"] == "awaiting-publication"
        assert active_observation["sourceRc"]["commit"] is None
        assert active_observation["sourceRc"]["publishedAt"] is None
        assert active_observation["sourceRc"]["archiveSha256"] is None

    # Every ledger entry is immutable and recognized by the release builder.
    head = build_release.git_head()
    for release in releases:
        assert build_release.published_release(release["version"]) == release
        if head == release["commit"]:
            build_release.assert_source_lock(release["version"])
        else:
            try:
                build_release.assert_source_lock(release["version"])
            except RuntimeError as exc:
                message = str(exc)
                assert release["tag"] in message
                assert release["commit"] in message
            else:
                raise AssertionError(f"published source lock accepted a different source tree for {release['version']}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert RC1["tag"] in readme
    assert RC1["archiveSha256"] in readme
    assert "v1.0.0-rc.2" in readme

    print("Tredecadia published release source-lock validation: OK")


if __name__ == "__main__":
    main()
