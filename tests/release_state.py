#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Shared release-stage helpers for Tredecadia validation scripts."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def citation_version(root: Path = ROOT) -> str:
    text = (root / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    assert match is not None, "CITATION.cff has no quoted version field"
    return match.group(1)


def is_prerelease(version: str) -> bool:
    """Return whether a SemVer-like project version carries a prerelease suffix."""
    return "-" in version


def expected_registry_status(version: str) -> str:
    return "draft" if is_prerelease(version) else "stable"
