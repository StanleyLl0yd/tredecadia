#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the non-normative weekday candidate proposed for v1.0.0-rc.2."""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PATH = ROOT / "release" / "weekday-rc2-candidate.json"
MONTHS_PATH = ROOT / "registry" / "months.json"

CONSONANTS = {"M", "N", "S", "T", "Y", "K", "Z"}
VOWELS = {"E", "O"}
IPA = {
    "ME": "me", "MO": "mo",
    "NE": "ne", "NO": "no",
    "SE": "se", "SO": "so",
    "TE": "te", "TO": "to",
    "YE": "je", "YO": "jo",
    "KE": "ke", "KO": "ko",
    "ZE": "ze", "ZO": "zo",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def hamming(a: str, b: str) -> int:
    assert len(a) == len(b)
    return sum(x != y for x, y in zip(a.lower(), b.lower()))


def levenshtein(a: str, b: str) -> int:
    a = a.lower()
    b = b.lower()
    row = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        new = [i]
        for j, cb in enumerate(b, 1):
            new.append(min(new[-1] + 1, row[j] + 1, row[j - 1] + (ca != cb)))
        row = new
    return row[-1]


def main() -> None:
    candidate = load(CANDIDATE_PATH)
    months = load(MONTHS_PATH)["months"]

    assert candidate["candidateVersion"] == 1
    assert candidate["targetRelease"] == "1.0.0-rc.2"
    assert candidate["normative"] is False
    assert candidate["status"] == "selected-for-rc2-integration-review"

    design = candidate["design"]
    assert design["shape"] == "CVCV"
    assert set(design["consonants"]) == CONSONANTS
    assert set(design["vowels"]) == VOWELS
    assert design["syllableInventory"] == list(IPA)
    assert design["allSyllablesUsedExactlyOnce"] is True

    weekdays = candidate["weekdays"]
    assert len(weekdays) == 7
    assert [day["id"] for day in weekdays] == [f"W{i}" for i in range(1, 8)]
    assert len({day["canonical"] for day in weekdays}) == 7

    first_onsets: list[str] = []
    second_onsets: list[str] = []
    used_syllables: list[str] = []

    for day in weekdays:
        assert set(day) == {"id", "canonical", "syllables", "citationIpa"}
        syllables = day["syllables"]
        assert len(syllables) == 2
        assert all(syllable in IPA for syllable in syllables)
        assert syllables[0][0] != syllables[1][0]
        assert all(syllable[1] in VOWELS for syllable in syllables)

        first_onsets.append(syllables[0][0])
        second_onsets.append(syllables[1][0])
        used_syllables.extend(syllables)

        expected = "".join(syllables).lower().capitalize()
        assert day["canonical"] == expected
        assert day["citationIpa"] == "ˈ" + ".".join(IPA[syllable] for syllable in syllables)

    assert set(first_onsets) == CONSONANTS
    assert set(second_onsets) == CONSONANTS
    assert Counter(used_syllables) == Counter({syllable: 1 for syllable in IPA})

    names = [day["canonical"] for day in weekdays]
    pair_profile: Counter[int] = Counter()
    distance2_pairs: list[list[str]] = []
    for a, b in combinations(names, 2):
        distance = hamming(a, b)
        pair_profile[distance] += 1
        if distance == 2:
            distance2_pairs.append([a, b])
        assert levenshtein(a, b) >= 2

    expected_profile = {int(key): value for key, value in design["weekdayPairHammingProfile"].items()}
    assert dict(sorted(pair_profile.items())) == expected_profile == {2: 3, 3: 12, 4: 6}
    assert distance2_pairs == candidate["unavoidableDistance2Pairs"]

    month_short4 = [month["short4"] for month in months]
    minimum_month_hamming = min(hamming(day, month) for day in names for month in month_short4)
    minimum_month_levenshtein = min(levenshtein(day, month) for day in names for month in month_short4)
    assert minimum_month_hamming == design["minimumMonthShort4Hamming"] == 3
    assert minimum_month_levenshtein == design["minimumMonthShort4Levenshtein"] == 3

    adjacent = [hamming(names[i], names[(i + 1) % len(names)]) for i in range(len(names))]
    assert adjacent == design["adjacentHamming"] == [4, 4, 4, 3, 4, 4, 3]
    assert min(adjacent) == design["minimumAdjacentHamming"] == 3
    assert Counter(adjacent) == Counter({4: 5, 3: 2})

    clearance = candidate["semanticClearance"]
    assert clearance["policy"] == "BLOCK_SOFT_IGNORE"
    assert set(clearance["selectedForms"]) == set(names)
    assert set(clearance["selectedForms"].values()) <= {"SOFT", "IGNORE"}
    blocked = set(clearance["blockedExactForms"])
    assert blocked
    assert not ({name.upper() for name in names} & blocked)

    compatibility = candidate["compatibility"]
    assert compatibility == {
        "publishedRc1Unchanged": True,
        "requiresNewReleaseCandidate": True,
        "expectedCalendarSchemaVersion": 2,
    }

    print("Tredecadia RC2 weekday candidate validation: OK")


if __name__ == "__main__":
    main()
