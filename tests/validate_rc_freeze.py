#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Release-candidate freeze checks for compatibility-critical Tredecadia data."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    calendar = load("registry/calendar.json")
    months = load("registry/months.json")
    localizations = load("registry/localizations.json")

    # Registry contract versions at the v1 RC freeze point.
    assert calendar["schemaVersion"] == 1
    assert months["schemaVersion"] == 3
    assert localizations["schemaVersion"] == 1

    # Calendar identity.
    assert calendar["profile"] == "tredecadia-civil"
    assert calendar["era"] == {
        "name": "Tredecadia Era",
        "symbol": "TE",
        "yearNumbering": "all-integers",
        "yearZero": True,
        "canonicalMinimumDigits": 5,
    }
    assert calendar["regularGrid"] == {
        "monthsPerYear": 13,
        "daysPerMonth": 28,
        "regularDaysPerYear": 364,
        "weeksPerMonth": 4,
        "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    }
    assert calendar["epoch"] == {
        "tredecadia": "00000-EQ",
        "gregorianAstronomical": {"year": -9999, "month": 3, "day": 20},
    }
    assert calendar["civilAnchor"] == {
        "equinoxDay": {"gregorianYearFormula": "Y-9999", "month": 3, "day": 20, "opensYear": True},
        "regularYearStart": {"gregorianYearFormula": "Y-9999", "month": 3, "day": 21},
        "earthDay": {"gregorianYearFormula": "Y-9998", "month": 3, "day": 19, "leapOnly": True, "closesYear": True},
    }
    assert calendar["leapRule"] == {
        "kind": "proleptic-gregorian-astronomical-year",
        "gregorianYearFormula": "Y-9998",
    }
    assert calendar["intercalary"] == [
        {"code": "EQ", "name": "Equinox / New Year Day", "position": "start", "leapOnly": False, "hasMonth": False, "hasWeekday": False},
        {"code": "ED", "name": "Earth Day", "position": "end", "leapOnly": True, "hasMonth": False, "hasWeekday": False},
    ]

    # Canonical month identity and abbreviation surface.
    expected_months = [
        (1, "Masanumika", ("MA", "SA", "NU", "MI", "KA"), "Masanu", "Masa"),
        (2, "Tasuzunumu", ("TA", "SU", "ZU", "NU", "MU"), "Tasuzu", "Tasu"),
        (3, "Nazumasanu", ("NA", "ZU", "MA", "SA", "NU"), "Nazuma", "Nazu"),
        (4, "Mikasumani", ("MI", "KA", "SU", "MA", "NI"), "Mikasu", "Mika"),
        (5, "Yanimuzunu", ("YA", "NI", "MU", "ZU", "NU"), "Yanimu", "Yani"),
        (6, "Zumitanasu", ("ZU", "MI", "TA", "NA", "SU"), "Zumita", "Zumi"),
        (7, "Muyasanumi", ("MU", "YA", "SA", "NU", "MI"), "Muyasa", "Muya"),
        (8, "Sunizusaka", ("SU", "NI", "ZU", "SA", "KA"), "Sunizu", "Suni"),
        (9, "Numanamuta", ("NU", "MA", "NA", "MU", "TA"), "Numana", "Numa"),
        (10, "Kazunusuya", ("KA", "ZU", "NU", "SU", "YA"), "Kazunu", "Kazu"),
        (11, "Yanazumasa", ("YA", "NA", "ZU", "MA", "SA"), "Yanazu", "Yana"),
        (12, "Sanumikazu", ("SA", "NU", "MI", "KA", "ZU"), "Sanumi", "Sanu"),
        (13, "Nimutazuna", ("NI", "MU", "TA", "ZU", "NA"), "Nimuta", "Nimu"),
    ]
    actual_months = [
        (month["number"], month["canonical"], tuple(month["syllables"]), month["short6"], month["short4"])
        for month in months["months"]
    ]
    assert actual_months == expected_months

    assert months["syllableInventory"] == ["MA", "MI", "MU", "NA", "NI", "NU", "SA", "SU", "TA", "YA", "KA", "ZU"]
    assert months["pronunciation"] == {
        "identity": "ordered-segmental-syllables",
        "stressIdentityCritical": False,
        "citationProminence": "weak-initial",
        "abbreviationsInheritCitationProminence": True,
        "syllableIpa": {
            "MA": "ma", "MI": "mi", "MU": "mu", "NA": "na", "NI": "ni", "NU": "nu",
            "SA": "sa", "SU": "su", "TA": "ta", "YA": "ja", "KA": "ka", "ZU": "zu",
        },
    }

    # Reviewed localization identities and maps are frozen for the RC. They
    # remain non-stable until the final v1 release action.
    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == {"ru-Cyrl", "ja-Kana", "ko-Hang"}
    assert all(profile["review"]["status"] == "reviewed" for profile in profiles.values())
    assert profiles["ru-Cyrl"]["syllableMap"] == {
        "MA": "ма", "MI": "ми", "MU": "му", "NA": "на", "NI": "ни", "NU": "ну",
        "SA": "са", "SU": "су", "TA": "та", "YA": "я", "KA": "ка", "ZU": "зу",
    }
    assert profiles["ja-Kana"]["syllableMap"] == {
        "MA": "マ", "MI": "ミ", "MU": "ム", "NA": "ナ", "NI": "ニ", "NU": "ヌ",
        "SA": "サ", "SU": "ス", "TA": "タ", "YA": "ヤ", "KA": "カ", "ZU": "ズ",
    }
    assert profiles["ko-Hang"]["syllableMap"] == {
        "MA": "마", "MI": "미", "MU": "무", "NA": "나", "NI": "니", "NU": "누",
        "SA": "사", "SU": "수", "TA": "타", "YA": "야", "KA": "카", "ZU": "주",
    }

    compatibility = (ROOT / "specification/compatibility.md").read_text(encoding="utf-8")
    for phrase in (
        "13 regular months",
        "00000-EQ",
        "canonical Short-6",
        "canonical Short-4",
        "minimum five ASCII digits",
        "MUST NOT silently fuzzy-autocorrect",
        "new major version",
    ):
        assert phrase in compatibility, phrase

    print("Tredecadia v1 release-candidate freeze validation: OK")


if __name__ == "__main__":
    main()
