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
    rc1 = load("release/v1-identity.json")
    rc2 = load("release/rc2-identity.json")

    assert calendar["schemaVersion"] == 2
    assert months["schemaVersion"] == 3
    assert localizations["schemaVersion"] == 1

    assert calendar["profile"] == "tredecadia-civil"
    assert calendar["era"] == {
        "name": "Tredecadia Era",
        "symbol": "TE",
        "yearNumbering": "all-integers",
        "yearZero": True,
        "canonicalMinimumDigits": 5,
    }
    expected_weekdays = [
        {"id": "W1", "canonical": "Mene", "syllables": ["ME", "NE"], "citationIpa": "ˈme.ne"},
        {"id": "W2", "canonical": "Noko", "syllables": ["NO", "KO"], "citationIpa": "ˈno.ko"},
        {"id": "W3", "canonical": "Kese", "syllables": ["KE", "SE"], "citationIpa": "ˈke.se"},
        {"id": "W4", "canonical": "Zoyo", "syllables": ["ZO", "YO"], "citationIpa": "ˈzo.jo"},
        {"id": "W5", "canonical": "Sote", "syllables": ["SO", "TE"], "citationIpa": "ˈso.te"},
        {"id": "W6", "canonical": "Yemo", "syllables": ["YE", "MO"], "citationIpa": "ˈje.mo"},
        {"id": "W7", "canonical": "Toze", "syllables": ["TO", "ZE"], "citationIpa": "ˈto.ze"},
    ]
    assert calendar["regularGrid"] == {
        "monthsPerYear": 13,
        "daysPerMonth": 28,
        "regularDaysPerYear": 364,
        "weeksPerMonth": 4,
        "weekdays": expected_weekdays,
    }
    assert rc2["calendar"]["regularGrid"]["weekdays"] == expected_weekdays
    assert rc1["calendar"]["regularGrid"]["weekdays"] == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]

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
    assert rc2["months"] == rc1["months"]

    assert months["syllableInventory"] == ["MA", "MI", "MU", "NA", "NI", "NU", "SA", "SU", "TA", "YA", "KA", "ZU"]
    assert months["pronunciation"] == rc2["pronunciation"] == rc1["pronunciation"]

    profiles = {profile["id"]: profile for profile in localizations["profiles"]}
    assert set(profiles) == {"ru-Cyrl", "ja-Kana", "ko-Hang"}
    assert all(profile["review"]["status"] in {"reviewed", "stable"} for profile in profiles.values())
    for profile_id, mapping in rc2["localizationMaps"].items():
        assert profiles[profile_id]["syllableMap"] == mapping
    assert rc2["localizationMaps"] == rc1["localizationMaps"]

    compatibility = (ROOT / "specification/compatibility.md").read_text(encoding="utf-8")
    for phrase in (
        "13 regular months",
        "00000-EQ",
        "canonical Short-6",
        "canonical Short-4",
        "W1",
        "Mene",
        "Toze",
        "minimum five ASCII digits",
        "MUST NOT silently fuzzy-autocorrect",
        "new major version",
    ):
        assert phrase in compatibility, phrase

    print("Tredecadia v1 RC2 compatibility freeze validation: OK")


if __name__ == "__main__":
    main()
