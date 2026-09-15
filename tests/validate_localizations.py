#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate localization profile maturity, derivation, and reverse mapping."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONTH_DATA = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))
LOC_DATA = json.loads((ROOT / "registry/localizations.json").read_text(encoding="utf-8"))
LOC_SCHEMA = json.loads((ROOT / "registry/localizations.schema.json").read_text(encoding="utf-8"))
MONTHS = MONTH_DATA["months"]
INVENTORY = MONTH_DATA["syllableInventory"]


def apply_case(text: str, transform: str) -> str:
    if transform == "none":
        return text
    if transform == "capitalize-first-codepoint":
        assert text
        return text[0].upper() + text[1:]
    raise AssertionError(f"unknown case transform: {transform}")


def derive(profile: dict, syllables: list[str]) -> str:
    raw = "".join(profile["syllableMap"][syllable] for syllable in syllables)
    return apply_case(raw, profile["caseTransform"])


def has_evidence(profile: dict, kind: str, url_prefix: str) -> bool:
    return any(
        evidence["kind"] == kind
        and evidence.get("url", "").startswith(url_prefix)
        for evidence in profile["review"]["evidence"]
    )


def main() -> None:
    assert LOC_DATA["schemaVersion"] == 1
    assert LOC_SCHEMA["properties"]["schemaVersion"]["const"] == 1
    assert LOC_DATA["specVersion"] == MONTH_DATA["specVersion"] == "0.3.0-draft"
    assert LOC_DATA["status"] == "draft"
    assert LOC_SCHEMA["$schema"] == "https://json-schema.org/draft/2020-12/schema"

    assert all("localizations" not in month for month in MONTHS)

    profiles = LOC_DATA["profiles"]
    assert profiles
    ids = [profile["id"] for profile in profiles]
    assert len(ids) == len(set(ids))
    assert set(ids) == {"ru-Cyrl", "ja-Kana", "ko-Hang"}

    canonical_by_number = {month["number"]: month for month in MONTHS}
    profile_by_id = {profile["id"]: profile for profile in profiles}

    for profile in profiles:
        assert profile["role"] == "display-alias"
        assert profile["reverseMapping"] == "unique-within-profile"
        assert profile["direction"] in {"ltr", "rtl"}
        assert profile["method"] in {"transliteration", "phonemic-transcription", "orthographic-adaptation"}
        assert set(profile["syllableMap"]) == set(INVENTORY)
        assert all(profile["syllableMap"][syllable] for syllable in INVENTORY)

        review = profile["review"]
        assert review["status"] in {"candidate", "reviewed", "stable"}
        if review["status"] != "candidate":
            assert review["evidence"], f"{profile['id']} lacks review evidence"
        if review["status"] == "stable":
            assert LOC_DATA["status"] == "stable", "stable profile in draft registry"

        aliases = profile["aliases"]
        assert len(aliases) == 13
        assert [alias["month"] for alias in aliases] == list(range(1, 14))

        full_values: list[str] = []
        short6_values: list[str] = []
        short4_values: list[str] = []

        for alias in aliases:
            month = canonical_by_number[alias["month"]]
            assert alias["full"] == derive(profile, month["syllables"])
            assert alias["short6"] == derive(profile, month["syllables"][:3])
            assert alias["short4"] == derive(profile, month["syllables"][:2])
            full_values.append(alias["full"])
            short6_values.append(alias["short6"])
            short4_values.append(alias["short4"])

        assert len(set(full_values)) == 13
        assert len(set(short6_values)) == 13
        assert len(set(short4_values)) == 13

    ru = profile_by_id["ru-Cyrl"]
    assert ru["review"]["status"] == "reviewed"
    assert has_evidence(ru, "expert-review", "https://old.bigenc.ru/")
    assert has_evidence(ru, "orthographic-reference", "https://gramota.ru/")
    assert ru["syllableMap"]["MI"] == "ми"
    assert ru["syllableMap"]["NI"] == "ни"
    assert ru["syllableMap"]["YA"] == "я"
    assert "palatal" in ru["notes"].lower()

    ja = profile_by_id["ja-Kana"]
    assert ja["review"]["status"] == "reviewed"
    assert has_evidence(ja, "standards-reference", "https://www.bunka.go.jp/")

    ko = profile_by_id["ko-Hang"]
    assert ko["review"]["status"] == "reviewed"
    assert has_evidence(ko, "standards-reference", "https://www.korean.go.kr/")
    assert ko["syllableMap"] == {
        "MA": "마", "MI": "미", "MU": "무",
        "NA": "나", "NI": "니", "NU": "누",
        "SA": "사", "SU": "수", "TA": "타",
        "YA": "야", "KA": "카", "ZU": "주",
    }

    # Draft 0.3 now has several independently reviewed profiles while keeping
    # all of them explicitly non-stable until the stable Tredecadia release.
    assert sum(profile["review"]["status"] == "reviewed" for profile in profiles) >= 3
    assert all(profile["review"]["status"] != "stable" for profile in profiles)

    print("Tredecadia localization profile validation: OK")


if __name__ == "__main__":
    main()
