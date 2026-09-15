#!/usr/bin/env python3
"""Validate the Tredecadia canonical month registry and naming invariants."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ["MA", "MI", "MU", "NA", "NI", "NU", "SA", "SU", "TA", "YA", "KA", "ZU"]
SYLLABLE_IPA = {
    "MA": "ma", "MI": "mi", "MU": "mu",
    "NA": "na", "NI": "ni", "NU": "nu",
    "SA": "sa", "SU": "su", "TA": "ta",
    "YA": "ja", "KA": "ka", "ZU": "zu",
}
BANNED_BIGRAMS = {
    ("MA", "ZU"), ("ZU", "NI"), ("ZU", "MU"),
    ("NU", "ZU"), ("ZU", "SU"), ("ZU", "YA"),
}


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


def fraction_from_json(value: dict[str, int]) -> Fraction:
    return Fraction(value["numerator"], value["denominator"])


def cyclic_distance(i: int, j: int, n: int = 13) -> int:
    distance = abs(i - j)
    return min(distance, n - distance)


def main() -> None:
    data = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "registry/months.schema.json").read_text(encoding="utf-8"))
    vectors = json.loads((ROOT / "tests/test-vectors.json").read_text(encoding="utf-8"))
    months = data["months"]

    assert data["schemaVersion"] == 3
    assert schema["properties"]["schemaVersion"]["const"] == 3
    assert data["status"] == "draft"
    assert data["specVersion"] == vectors["specVersion"] == "1.0.0-rc.1"
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert data["syllableInventory"] == INVENTORY

    pronunciation = data["pronunciation"]
    assert pronunciation == {
        "identity": "ordered-segmental-syllables",
        "stressIdentityCritical": False,
        "citationProminence": "weak-initial",
        "abbreviationsInheritCitationProminence": True,
        "syllableIpa": SYLLABLE_IPA,
    }

    assert len(months) == 13
    assert [month["number"] for month in months] == list(range(1, 14))
    canonicals = [month["canonical"] for month in months]
    short6 = [month["short6"] for month in months]
    short4 = [month["short4"] for month in months]
    assert len(set(canonicals)) == len(set(short6)) == len(set(short4)) == 13

    required_keys = {
        "number", "canonical", "syllables", "citationIpa",
        "short6", "short4",
    }
    for month in months:
        assert set(month) == required_keys
        syllables = month["syllables"]
        assert len(syllables) == 5
        assert len(set(syllables)) == 5
        assert all(syllable in INVENTORY for syllable in syllables)
        assert all(a[0] != b[0] for a, b in zip(syllables, syllables[1:]))
        assert all((a, b) not in BANNED_BIGRAMS for a, b in zip(syllables, syllables[1:]))

        assert month["canonical"] == "".join(syllables).lower().capitalize()
        assert month["short6"] == "".join(syllables[:3]).lower().capitalize()
        assert month["short4"] == "".join(syllables[:2]).lower().capitalize()

        segmental = ".".join(SYLLABLE_IPA[syllable] for syllable in syllables)
        assert month["citationIpa"] == f"ˈ{segmental}"
        assert month["citationIpa"].startswith("ˈ" + SYLLABLE_IPA[syllables[0]])

        short6_segmental = ".".join(SYLLABLE_IPA[syllable] for syllable in syllables[:3])
        short4_segmental = ".".join(SYLLABLE_IPA[syllable] for syllable in syllables[:2])
        assert f"ˈ{short6_segmental}".startswith("ˈ" + SYLLABLE_IPA[syllables[0]])
        assert f"ˈ{short4_segmental}".startswith("ˈ" + SYLLABLE_IPA[syllables[0]])

        assert "ipa" not in month
        assert "localizations" not in month

    for i in range(13):
        for j in range(i + 1, 13):
            assert hamming(months[i]["syllables"], months[j]["syllables"]) >= 4
            assert hamming(months[i]["syllables"][:3], months[j]["syllables"][:3]) >= 2

    full = Counter(s for month in months for s in month["syllables"])
    counts6 = Counter(s for month in months for s in month["syllables"][:3])
    counts4 = Counter(s for month in months for s in month["syllables"][:2])
    naming = vectors["naming"]

    assert dict(full) == naming["fullFrequencyVector"]
    assert sum(value * value for value in full.values()) == naming["fullSumSquaredCounts"] == 379
    assert ssd(full, 5) == fraction_from_json(naming["fullSsd"]) == Fraction(323, 12)
    assert ssd(counts6, 3) == fraction_from_json(naming["short6Ssd"]) == Fraction(41, 4)
    assert ssd(counts4, 2) == fraction_from_json(naming["short4Ssd"]) == Fraction(11, 3)

    distance2_short6: list[list[str]] = []
    distance1_short4: list[list[str]] = []
    for i in range(13):
        for j in range(i + 1, 13):
            if levenshtein(short6[i].lower(), short6[j].lower()) == 2:
                distance2_short6.append([short6[i], short6[j]])
            if levenshtein(short4[i].lower(), short4[j].lower()) == 1:
                distance1_short4.append([short4[i], short4[j]])
    assert distance2_short6 == naming["short6LevenshteinDistance2Pairs"]
    assert distance1_short4 == naming["short4LevenshteinDistance1Pairs"]

    adjacent_full: list[int] = []
    adjacent6: list[int] = []
    adjacent4: list[int] = []
    adjacent_shared: list[int] = []
    for i in range(13):
        a = months[i]["syllables"]
        b = months[(i + 1) % 13]["syllables"]
        adjacent_full.append(hamming(a, b))
        adjacent6.append(hamming(a[:3], b[:3]))
        adjacent4.append(hamming(a[:2], b[:2]))
        adjacent_shared.append(len(set(a) & set(b)))

    cycle = vectors["cycle"]
    assert min(adjacent_full) == cycle["minimumAdjacentFullHamming"] == 5
    assert min(adjacent6) == cycle["minimumAdjacentShort6SyllableHamming"] == 3
    assert min(adjacent4) == cycle["minimumAdjacentShort4SyllableHamming"] == 2
    assert max(adjacent_shared) == cycle["maximumAdjacentSharedSyllables"] == 2

    index6 = {month["short6"]: i for i, month in enumerate(months)}
    index4 = {month["short4"]: i for i, month in enumerate(months)}
    assert {
        "Yanimu/Yanazu": cyclic_distance(index6["Yanimu"], index6["Yanazu"]),
        "Nazu/Kazu": cyclic_distance(index4["Nazu"], index4["Kazu"]),
        "Yani/Yana": cyclic_distance(index4["Yani"], index4["Yana"]),
    } == cycle["closePairCyclicDistances"]

    print("Tredecadia canonical month registry validation: OK")


if __name__ == "__main__":
    main()
