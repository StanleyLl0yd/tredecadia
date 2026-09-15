#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate Short-4 conversational/UX invariants and close-pair policy."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
MONTHS = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]
POLICY = json.loads((ROOT / "tests/short4-ux-vectors.json").read_text(encoding="utf-8"))


def levenshtein(a: str, b: str) -> int:
    row = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        new = [i]
        for j, cb in enumerate(b, 1):
            new.append(min(new[-1] + 1, row[j] + 1, row[j - 1] + (ca != cb)))
        row = new
    return row[-1]


def syllable_hamming(a: list[str], b: list[str]) -> int:
    assert len(a) == len(b)
    return sum(x != y for x, y in zip(a, b))


def normalize_pairs(pairs: list[tuple[str, str]]) -> list[list[str]]:
    order = {m["short4"]: m["number"] for m in MONTHS}
    normalized = []
    for a, b in pairs:
        if order[a] > order[b]:
            a, b = b, a
        normalized.append([a, b])
    return sorted(normalized, key=lambda p: (order[p[0]], order[p[1]]))


def main() -> None:
    assert POLICY["specVersion"] == citation_version()
    assert POLICY["policyVersion"] == 1
    assert POLICY["preferredConversationalForm"] == "short4"

    short4 = [m["short4"] for m in MONTHS]
    assert len(short4) == 13
    assert len(set(x.casefold() for x in short4)) == 13
    assert all(len(x) == 4 and x.isascii() and x[0].isupper() and x[1:].islower() for x in short4)

    by_short = {m["short4"]: m for m in MONTHS}
    for month in MONTHS:
        assert month["short4"] == "".join(month["syllables"][:2]).lower().capitalize()
        assert month["canonical"].lower().startswith(month["short4"].lower())
        assert month["short6"].lower().startswith(month["short4"].lower())
        assert month["citationIpa"].startswith("ˈ")

    lev1: list[tuple[str, str]] = []
    syllable1: list[tuple[str, str]] = []
    for i, a in enumerate(MONTHS):
        for b in MONTHS[i + 1 :]:
            if levenshtein(a["short4"].casefold(), b["short4"].casefold()) == 1:
                lev1.append((a["short4"], b["short4"]))
            if syllable_hamming(a["syllables"][:2], b["syllables"][:2]) == 1:
                syllable1.append((a["short4"], b["short4"]))

    expected = POLICY["knownClosePairs"]
    assert normalize_pairs(lev1) == expected["characterLevenshtein1"]
    assert normalize_pairs(syllable1) == expected["syllableHamming1"]

    for group in expected.values():
        for a, b in group:
            assert a in by_short and b in by_short and a != b

    recognition = POLICY["recognitionPolicy"]
    assert recognition == {
        "exactValidShort4MayResolve": True,
        "fuzzyValidToValidAutocorrection": False,
        "ambiguousInputRequiresDisambiguation": True,
        "voiceShouldUseSurroundingMonthContext": True,
        "machineStorageUsesCanonicalIdentity": True,
    }

    contexts = {item["kind"]: item for item in POLICY["contextExamples"]}
    for kind in ("month-picker", "calendar-header", "date-chip", "reminder-summary"):
        assert contexts[kind]["structuredMonthContext"] is True
        assert contexts[kind]["short4Safe"] is True
    assert contexts["unrestricted-prose"]["structuredMonthContext"] is False
    assert contexts["unrestricted-prose"]["short4Safe"] is False

    print("Tredecadia Short-4 UX validation: OK")


if __name__ == "__main__":
    main()
