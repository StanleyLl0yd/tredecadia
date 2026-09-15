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


def main() -> None:
    data = json.loads((ROOT / "release/published-releases.json").read_text(encoding="utf-8"))
    assert data["schemaVersion"] == 1
    assert len(data["releases"]) == 1

    rc = data["releases"][0]
    assert rc == {
        "version": "1.0.0-rc.1",
        "tag": "v1.0.0-rc.1",
        "commit": "937d8d681fcce6095d6a4d196783136b908c1be5",
        "publishedAt": "2026-09-15T20:21:58Z",
        "archive": "tredecadia-1.0.0-rc.1.tar.gz",
        "archiveSha256": "018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf",
    }

    plan = json.loads((ROOT / "release/stable-plan.json").read_text(encoding="utf-8"))
    observation = json.loads((ROOT / "release/rc-observation.json").read_text(encoding="utf-8"))
    assert plan["sourceRc"]["version"] == rc["version"]
    assert plan["sourceRc"]["tag"] == rc["tag"]
    assert plan["sourceRc"]["commit"] == rc["commit"]
    assert plan["sourceRc"]["archiveSha256"] == rc["archiveSha256"]
    assert observation["sourceRc"]["version"] == rc["version"]
    assert observation["sourceRc"]["tag"] == rc["tag"]
    assert observation["sourceRc"]["commit"] == rc["commit"]
    assert observation["sourceRc"]["publishedAt"] == rc["publishedAt"]
    assert observation["sourceRc"]["archiveSha256"] == rc["archiveSha256"]

    assert build_release.published_release(rc["version"]) == rc

    # On a post-RC default branch the source lock must reject rebuilding the
    # already-published version under the same name. When this test is run at
    # the historical release commit itself, the lock is expected to allow it.
    head = build_release.git_head()
    if head == rc["commit"]:
        build_release.assert_source_lock(rc["version"])
    else:
        try:
            build_release.assert_source_lock(rc["version"])
        except RuntimeError as exc:
            message = str(exc)
            assert rc["tag"] in message
            assert rc["commit"] in message
        else:
            raise AssertionError("published RC source lock accepted a different or unverifiable source tree")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "check out the published tag" in readme
    assert rc["tag"] in readme
    assert rc["archiveSha256"] in readme

    print("Tredecadia published release source-lock validation: OK")


if __name__ == "__main__":
    main()
