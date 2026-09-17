#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the M5 additional-script localization candidate pack."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONTHS = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]
PACK = json.loads(
    (ROOT / "rationale/additional-script-localization-candidates.json").read_text(encoding="utf-8")
)

EXPECTED_IDS = {"ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva", "bn-Beng", "fa-Arab"}
INVENTORY = {"MA", "MI", "MU", "NA", "NI", "NU", "SA", "SU", "TA", "YA", "KA", "ZU"}
REVIEWED = {"ka-Geor", "hy-Armn", "ar-Arab", "hi-Deva"}
CANDIDATE = {"bn-Beng", "fa-Arab"}


def derive(profile: dict, syllables: list[str]) -> str:
    return "".join(profile["syllableMap"][syllable] for syllable in syllables)


def main() -> None:
    assert PACK["schemaVersion"] == 1
    assert PACK["targetMinor"] == "1.1.0"
    assert PACK["canonicalSource"] == "registry/months.json"

    profiles = PACK["profiles"]
    ids = [profile["id"] for profile in profiles]
    assert len(ids) == len(set(ids))
    assert set(ids) == EXPECTED_IDS

    by_id = {profile["id"]: profile for profile in profiles}
    canonical_by_number = {month["number"]: month for month in MONTHS}

    for profile in profiles:
        pid = profile["id"]
        assert profile["direction"] in {"ltr", "rtl"}
        assert profile["method"] in {"phonemic-transcription", "orthographic-adaptation"}
        assert profile["proposedMaturity"] in {"candidate", "reviewed"}
        assert set(profile["syllableMap"]) == INVENTORY
        assert all(profile["syllableMap"].values())
        assert len(set(profile["syllableMap"].values())) == 12, f"{pid}: syllable map not reversible"

        aliases = profile["aliases"]
        assert len(aliases) == 13
        assert [a["month"] for a in aliases] == list(range(1, 14))

        full: list[str] = []
        short6: list[str] = []
        short4: list[str] = []
        for alias in aliases:
            month = canonical_by_number[alias["month"]]
            syllables = month["syllables"]
            assert alias["full"] == derive(profile, syllables), f"{pid} M{alias['month']:02d} full"
            assert alias["short6"] == derive(profile, syllables[:3]), f"{pid} M{alias['month']:02d} short6"
            assert alias["short4"] == derive(profile, syllables[:2]), f"{pid} M{alias['month']:02d} short4"
            full.append(alias["full"])
            short6.append(alias["short6"])
            short4.append(alias["short4"])

        assert len(set(full)) == 13
        assert len(set(short6)) == 13
        assert len(set(short4)) == 13
        assert profile["notes"].strip()

        evidence = profile["evidence"]
        if profile["proposedMaturity"] == "reviewed":
            assert evidence, f"{pid}: reviewed proposal lacks evidence"
            assert any(item.get("url") for item in evidence), f"{pid}: reviewed evidence lacks URL"

    assert {pid for pid, p in by_id.items() if p["proposedMaturity"] == "reviewed"} == REVIEWED
    assert {pid for pid, p in by_id.items() if p["proposedMaturity"] == "candidate"} == CANDIDATE

    assert by_id["ka-Geor"]["syllableMap"]["YA"] == "ია"
    assert by_id["hy-Armn"]["syllableMap"]["YA"] == "յա"

    ar = by_id["ar-Arab"]
    assert ar["direction"] == "rtl"
    assert ar["syllableMap"]["MA"] == "مَ"
    assert ar["syllableMap"]["MI"] == "مِ"
    assert ar["syllableMap"]["MU"] == "مُ"
    assert "fully vocalized" in ar["notes"].lower()

    hi = by_id["hi-Deva"]
    assert hi["syllableMap"]["ZU"] == "ज़ु"
    assert "approximation" in hi["notes"].lower()

    bn = by_id["bn-Beng"]
    assert bn["syllableMap"]["YA"] == "ইয়া"
    assert bn["syllableMap"]["ZU"] == "জ়ু"
    assert "candidate only" in bn["notes"].lower()

    fa = by_id["fa-Arab"]
    assert fa["direction"] == "rtl"
    assert fa["syllableMap"]["MU"] == "مو"
    assert "candidate only" in fa["notes"].lower()

    print("Tredecadia additional-script localization candidate validation: OK")


if __name__ == "__main__":
    main()
