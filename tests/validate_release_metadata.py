#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the explicit GitHub release-publication trigger."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META_PATH = ROOT / "release" / "publish.json"
META = json.loads(META_PATH.read_text(encoding="utf-8"))


def citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    assert match is not None
    return match.group(1)


def main() -> None:
    assert set(META) == {"version", "tag", "prerelease", "notes"}
    version = META["version"]
    tag = META["tag"]
    notes = META["notes"]

    assert isinstance(version, str) and re.fullmatch(r"[0-9A-Za-z][0-9A-Za-z.-]*", version)
    assert tag == f"v{version}"
    assert re.fullmatch(r"v[0-9A-Za-z][0-9A-Za-z.-]*", tag)
    assert isinstance(META["prerelease"], bool)
    assert META["prerelease"] is ("-rc." in version)

    assert isinstance(notes, str) and notes == f"release/notes/{version}.md"
    notes_path = (ROOT / notes).resolve()
    assert notes_path.is_relative_to((ROOT / "release" / "notes").resolve())
    assert notes_path.is_file()

    assert citation_version() == version
    for path in ("registry/calendar.json", "registry/months.json", "registry/localizations.json", "tests/test-vectors.json", "tests/conversion-vectors.json", "tests/short4-ux-vectors.json", "tests/accessibility-vectors.json"):
        assert json.loads((ROOT / path).read_text(encoding="utf-8"))["specVersion"] == version, path

    assert f"## {version} —" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert version in (ROOT / "README.md").read_text(encoding="utf-8")
    assert version in notes_path.read_text(encoding="utf-8")

    print("Tredecadia release publication metadata: OK")


if __name__ == "__main__":
    main()
