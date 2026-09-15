#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Ensure draft version identifiers stay synchronized across published artifacts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = "0.1.0-draft"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    artifacts = {
        "registry/months.json": load("registry/months.json")["specVersion"],
        "registry/calendar.json": load("registry/calendar.json")["specVersion"],
        "tests/test-vectors.json": load("tests/test-vectors.json")["specVersion"],
        "tests/conversion-vectors.json": load("tests/conversion-vectors.json")["specVersion"],
    }

    assert set(artifacts.values()) == {EXPECTED}, artifacts

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    assert f'version: "{EXPECTED}"' in citation

    print("Tredecadia version consistency: OK")


if __name__ == "__main__":
    main()
