#!/usr/bin/env python3
"""Validate the Tredecadia draft registry using only the Python standard library."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "months.json"
SCHEMA = ROOT / "registry" / "months.schema.json"
VECTORS = ROOT / "tests" / "test-vectors.json"

INVENTORY = ["MA", "MI", "MU", "NA", "NI", "NU", "SA", "SU", "TA", "YA", "KA", "ZU"]
BANNED_BIGRAMS = {("MA", "ZU"), ("ZU", "NI"), ("ZU", "MU"), ("NU", "ZU"), ("ZU", "SU"), ("ZU", "YA")}


def hamming(a: list[str], b: list[str]) -> int:
    assert len(a) == len(b)
    return sum(x != y for x, y in zip(a, b))


def levenshtein(a: str, b: str) -> int:
    row = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        new = [i]
        for j, cb in enumerate(b, 1):
            new.append(min(new[-1] + 1, row[j] + 1, row[j - 1] + (ca != cb)))
        row = new
    return row[-1]


def ssd(counts: Counter[str], positions: int) -> Fraction:
    mean = Fraction(13 * positions, 12)
    return sum((Fraction(counts[s]) - mean) ** 2 for s in INVENTORY)


def cyclic_distance(i: int, j: int, n: int = 13) -> int:
    d = abs(i - j)
    return min(d, n - d)


def assert_float(value: float, expected: Fraction) -> None:
    assert abs(value - float(expected)) < 1e-12, (value, float(expected))


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    json.loads(SCHEMA.read_text(encoding="utf-8"))  # Syntax check for the published schema.
    vectors = json.loads(VECTORS.read_text(encoding="utf-8"))
    months = data["months"]

    calendar = vectors["calendar"]
    assert calendar == {
        "monthsPerYear": 13,
        "daysPerMonth": 28,
        "regularDaysPerYear": 364,
        "weeksPerMonth": 4,
        "firstWeekday": "Monday",
        "lastWeekday": "Sunday",
    }

    assert data["syllableInventory"] == INVENTORY
    assert len(months) == 13
    assert [m["number"] for m in months] == list(range(1, 14))

    canonicals = [m["canonical"] for m in months]
    short6 = [m["short6"] for m in months]
    short4 = [m["short4"] for m in months]
    assert len(set(canonicals)) == 13
    assert len(set(short6)) == 13
    assert len(set(short4)) == 13

    for month in months:
        syllables = month["syllables"]
        assert len(syllables) == 5
        assert len(set(syllables)) == 5
        assert all(s in INVENTORY for s in syllables)
        assert all(a[0] != b[0] for a, b in zip(syllables, syllables[1:]))
        assert all((a, b) not in BANNED_BIGRAMS for a, b in zip(syllables, syllables[1:]))

        canonical = "".join(syllables).lower().capitalize()
        expected6 = "".join(syllables[:3]).lower().capitalize()
        expected4 = "".join(syllables[:2]).lower().capitalize()
        assert month["canonical"] == canonical
        assert month["short6"] == expected6
        assert month["short4"] == expected4
        assert len(canonical) == 10
        assert len(expected6) == 6
        assert len(expected4) == 4
        assert month["localizations"].get("ru")

    # Pairwise positional distinguishability.
    for i in range(13):
        for j in range(i + 1, 13):
            assert hamming(months[i]["syllables"], months[j]["syllables"]) >= 4
            assert hamming(months[i]["syllables"][:3], months[j]["syllables"][:3]) >= 2

    full_counts = Counter(s for m in months for s in m["syllables"])
    short6_counts = Counter(s for m in months for s in m["syllables"][:3])
    short4_counts = Counter(s for m in months for s in m["syllables"][:2])
    naming = vectors["naming"]

    assert dict(full_counts) == naming["fullFrequencyVector"]
    assert sum(v * v for v in full_counts.values()) == naming["fullSumSquaredCounts"] == 379
    assert ssd(full_counts, 5) == Fraction(323, 12)
    assert ssd(short6_counts, 3) == Fraction(41, 4)
    assert ssd(short4_counts, 2) == Fraction(11, 3)
    assert_float(naming["fullSsd"], Fraction(323, 12))
    assert_float(naming["short6Ssd"], Fraction(41, 4))
    assert_float(naming["short4Ssd"], Fraction(11, 3))

    d2_6: list[list[str]] = []
    d1_4: list[list[str]] = []
    for i in range(13):
        for j in range(i + 1, 13):
            if levenshtein(short6[i].lower(), short6[j].lower()) == 2:
                d2_6.append([short6[i], short6[j]])
            if levenshtein(short4[i].lower(), short4[j].lower()) == 1:
                d1_4.append([short4[i], short4[j]])

    assert d2_6 == naming["short6LevenshteinDistance2Pairs"]
    assert d1_4 == naming["short4LevenshteinDistance1Pairs"]

    # Canonical cycle adjacency quality.
    adjacent_full: list[int] = []
    adjacent_short6: list[int] = []
    adjacent_short4: list[int] = []
    adjacent_shared: list[int] = []
    for i in range(13):
        a = months[i]["syllables"]
        b = months[(i + 1) % 13]["syllables"]
        adjacent_full.append(hamming(a, b))
        adjacent_short6.append(hamming(a[:3], b[:3]))
        adjacent_short4.append(hamming(a[:2], b[:2]))
        adjacent_shared.append(len(set(a) & set(b)))

    cycle = vectors["cycle"]
    assert min(adjacent_full) == cycle["minimumAdjacentFullHamming"] == 5
    assert min(adjacent_short6) == cycle["minimumAdjacentShort6SyllableHamming"] == 3
    assert min(adjacent_short4) == cycle["minimumAdjacentShort4SyllableHamming"] == 2
    assert max(adjacent_shared) == cycle["maximumAdjacentSharedSyllables"] == 2

    index6 = {m["short6"]: i for i, m in enumerate(months)}
    index4 = {m["short4"]: i for i, m in enumerate(months)}
    distances = {
        "Yanimu/Yanazu": cyclic_distance(index6["Yanimu"], index6["Yanazu"]),
        "Nazu/Kazu": cyclic_distance(index4["Nazu"], index4["Kazu"]),
        "Yani/Yana": cyclic_distance(index4["Yani"], index4["Yana"]),
    }
    assert distances == cycle["closePairCyclicDistances"]

    print("Tredecadia registry validation: OK")


if __name__ == "__main__":
    main()
