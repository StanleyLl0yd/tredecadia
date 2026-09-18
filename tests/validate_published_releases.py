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
RC2 = {
    "version": "1.0.0-rc.2",
    "tag": "v1.0.0-rc.2",
    "commit": "b816d613618d51515d910e0d3bdb9d2f211b6d22",
    "publishedAt": "2026-09-16T09:44:59Z",
    "archive": "tredecadia-1.0.0-rc.2.tar.gz",
    "archiveSha256": "23e40180098c656c88aa4ba27c6989ac053d9ce8b8029c9ce2e3b16946bf32ec",
}
STABLE = {
    "version": "1.0.0",
    "tag": "v1.0.0",
    "commit": "8c272bf6a48b1b84a4b2ca8c1db43c6ffb9f5ce3",
    "publishedAt": "2026-09-17T12:53:29Z",
    "archive": "tredecadia-1.0.0.tar.gz",
    "archiveSha256": "2f14cc4fb2bcac2cfcce280ddbe948d4c65cab098ce23c1d385d220709f5c392",
}
V11_RC1 = {
    "version": "1.1.0-rc.1",
    "tag": "v1.1.0-rc.1",
    "commit": "8d1b5a0c05eab8875e95b9896fd1c386edfe1220",
    "publishedAt": "2026-09-18T08:01:59Z",
    "archive": "tredecadia-1.1.0-rc.1.tar.gz",
    "archiveSha256": "5b32dad3438572b67381ef5af05bf6fd915a2393fc69c8c132b7bef125ff876e",
}


def main() -> None:
    data = json.loads((ROOT / "release/published-releases.json").read_text(encoding="utf-8"))
    assert data["schemaVersion"] == 1
    releases = data["releases"]
    assert releases == [RC1, RC2, STABLE, V11_RC1]
    assert len({entry["version"] for entry in releases}) == 4
    assert len({entry["tag"] for entry in releases}) == 4

    plan = json.loads((ROOT / "release/stable-plan.json").read_text(encoding="utf-8"))
    active_observation = json.loads((ROOT / "release/rc-observation.json").read_text(encoding="utf-8"))
    rc1_observation = json.loads((ROOT / "release/rc1-observation.json").read_text(encoding="utf-8"))
    rc2_identity = json.loads((ROOT / "release/rc2-identity.json").read_text(encoding="utf-8"))

    predecessor = plan["predecessorRc"]
    assert predecessor["version"] == RC1["version"]
    assert predecessor["tag"] == RC1["tag"]
    assert predecessor["commit"] == RC1["commit"]
    assert predecessor["archiveSha256"] == RC1["archiveSha256"]
    assert predecessor["observationRecord"] == "release/rc1-observation.json"
    for key in ("version", "tag", "commit", "publishedAt", "archiveSha256"):
        assert rc1_observation["sourceRc"][key] == RC1[key]

    assert plan["sourceRc"]["publicationStatus"] == "published"
    assert active_observation["sourceRc"]["publicationStatus"] == "published"
    for key in ("version", "tag", "commit", "archiveSha256"):
        assert plan["sourceRc"][key] == RC2[key]
        assert active_observation["sourceRc"][key] == RC2[key]
    assert active_observation["sourceRc"]["publishedAt"] == RC2["publishedAt"]

    identity_release = rc2_identity["release"]
    assert identity_release["publicationStatus"] == "published"
    for key in ("version", "tag", "commit", "publishedAt", "archiveSha256"):
        assert identity_release[key] == RC2[key]

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
    # Historical RC identity remains visible in the public README. Stable
    # publication identity is recorded in the immutable ledger and roadmap;
    # it is additionally required here once public README synchronization lands.
    for release in (RC1, RC2):
        assert release["tag"] in readme
        assert release["commit"] in readme
        assert release["archiveSha256"] in readme
    assert RC2["publishedAt"] in readme

    # Observation timing is historical release evidence, not permanent
    # reader-facing copy. Keep it locked in the observation record while the
    # README is free to describe the current release line.
    assert active_observation["window"]["notBefore"] == "2026-09-17T09:44:59Z"

    # The current public README must still expose the immutable stable source
    # and deterministic archive identity even while a later RC is active.
    assert STABLE["tag"] in readme
    assert STABLE["commit"] in readme
    assert STABLE["archiveSha256"] in readme

    # The active published v1.1 RC is also public and immutable. Its later
    # observation/stable-promotion records may evolve, but this source/archive
    # identity must not.
    assert V11_RC1["tag"] in readme
    assert V11_RC1["commit"] in readme
    assert V11_RC1["archiveSha256"] in readme
    assert V11_RC1["publishedAt"] in readme

    print("Tredecadia published release source-lock validation: OK")


if __name__ == "__main__":
    main()
