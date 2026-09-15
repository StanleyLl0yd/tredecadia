#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate repository-wide version consistency for RC and stable stages."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    version = citation_version()
    publish = load("release/publish.json")
    assert publish["version"] == version
    assert publish["tag"] == f"v{version}"

    versioned_json = [
        "registry/months.json",
        "registry/calendar.json",
        "registry/localizations.json",
        "tests/test-vectors.json",
        "tests/conversion-vectors.json",
        "tests/short4-ux-vectors.json",
        "tests/accessibility-vectors.json",
    ]
    assert {load(path)["specVersion"] for path in versioned_json} == {version}

    specifications = [
        "specification/calendar-standard.md",
        "specification/conversion-standard.md",
        "specification/date-notation.md",
        "specification/month-naming-standard.md",
        "specification/localization.md",
        "specification/localization-profiles.md",
        "specification/compatibility.md",
    ]
    for path in specifications:
        assert f"Status: **{version}" in (ROOT / path).read_text(encoding="utf-8"), path

    for path in ("README.md", "ROADMAP.md", "docs/index.md", "CHANGELOG.md"):
        assert version in (ROOT / path).read_text(encoding="utf-8"), path

    # The M3 audit is a historical RC record and must keep identifying the RC,
    # even after the working tree advances to stable v1.0.0.
    audit = (ROOT / "rationale/release-candidate-audit.md").read_text(encoding="utf-8")
    assert "1.0.0-rc.1" in audit

    print("Tredecadia version consistency: OK")


if __name__ == "__main__":
    main()
