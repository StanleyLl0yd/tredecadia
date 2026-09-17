#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate localized project READMEs against canonical project data."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]

LOCALES = {
    "ru": "README.ru.md",
    "es": "README.es.md",
    "pt-BR": "README.pt-BR.md",
    "fr": "README.fr.md",
    "de": "README.de.md",
    "it": "README.it.md",
    "tr": "README.tr.md",
    "pl": "README.pl.md",
    "uk": "README.uk.md",
    "ka": "README.ka.md",
    "hy": "README.hy.md",
    "zh-CN": "README.zh-CN.md",
    "zh-TW": "README.zh-TW.md",
    "ja": "README.ja.md",
    "ko": "README.ko.md",
    "ar": "README.ar.md",
    "fa": "README.fa.md",
    "hi": "README.hi.md",
    "bn": "README.bn.md",
    "id": "README.id.md",
    "vi": "README.vi.md",
}

REVIEWED_PROFILE_BY_LOCALE = {
    "ru": "ru-Cyrl",
    "ja": "ja-Kana",
    "ko": "ko-Hang",
}

# These phrases were visible translation leftovers in the first multilingual
# pass. Keep them out of localized explanatory prose; identifiers such as
# ASCII, Python, CC BY, MIT, BCE/CE, Short-6 and Short-4 are intentionally
# retained where they are part of the technical vocabulary.
UNLOCALIZED_PROSE = (
    "release candidate",
    "compatibility surface",
    "observation period",
    "canonical interchange format",
    "reference pronunciation",
    "normative documents",
    "machine-readable registries",
)


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def expected_profile_status(profile_id: str, version: str, plan: dict) -> str:
    entries = {entry["id"]: entry for entry in plan["localizationProfiles"]}
    entry = entries[profile_id]
    if version == plan["sourceRc"]["version"]:
        return entry["currentStatus"]
    assert version == plan["targetVersion"], version
    decision = entry["stableDecision"]
    assert decision in {"accepted", "rejected"}, f"stable candidate has unresolved profile decision: {profile_id}"
    policy = plan["profileDecisionPolicy"]
    return policy["acceptedStatus"] if decision == "accepted" else policy["rejectedStatus"]


def main() -> None:
    version = citation_version()
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index = (ROOT / "README.languages.md").read_text(encoding="utf-8")
    months = load("registry/months.json")["months"]
    calendar = load("registry/calendar.json")
    weekdays = calendar["regularGrid"]["weekdays"]
    localization_registry = load("registry/localizations.json")
    profiles = {profile["id"]: profile for profile in localization_registry["profiles"]}
    stable_plan = load("release/stable-plan.json")

    assert version in {stable_plan["sourceRc"]["version"], stable_plan["targetVersion"]}
    assert "README.languages.md" in root_readme
    assert "README.md" in index
    assert [day["id"] for day in weekdays] == [f"W{i}" for i in range(1, 8)]
    weekday_cycle = " → ".join(f"{day['id']} {day['canonical']}" for day in weekdays)

    for locale, path in LOCALES.items():
        file = ROOT / path
        assert file.is_file(), f"missing localized README: {path}"
        text = file.read_text(encoding="utf-8")
        lowered = text.lower()

        assert text.startswith("# Tredecadia\n"), path
        assert f"`{version}`" in text, f"{path}: current version missing"
        assert "README.md" in text, f"{path}: English README link missing"
        assert "README.languages.md" in text, f"{path}: language-index link missing"
        assert "specification/" in text, f"{path}: specification link missing"
        assert "registry/" in text, f"{path}: registry link missing"
        assert "LICENSE.md" in text, f"{path}: license link missing"
        assert "00000-EQ" in text, f"{path}: epoch example missing"
        assert "12025-07-11" in text, f"{path}: modern date example missing"
        assert "EQ" in text and "ED" in text, f"{path}: intercalary identifiers missing"

        # Every localized introduction must expose the language-neutral weekday
        # identity in exact W1..W7 order. Localized weekday aliases remain a
        # separate, unreviewed surface and must not replace canonical forms.
        assert weekday_cycle in text, f"{path}: canonical weekday cycle missing or out of order"
        for day in weekdays:
            assert day["id"] in text, f"{path}: missing canonical weekday ID {day['id']}"
            assert day["canonical"] in text, f"{path}: missing canonical weekday {day['canonical']}"

        # BCE/CE may remain as international abbreviations, but a localized
        # README must spell out what they mean rather than assuming the reader
        # knows the English initials.
        assert "BCE" in text and "CE" in text, f"{path}: BCE/CE notation missing"
        assert "Before Common Era" in text, f"{path}: BCE expansion missing"
        assert "Common Era" in text, f"{path}: CE expansion missing"

        for phrase in UNLOCALIZED_PROSE:
            assert phrase not in lowered, f"{path}: untranslated English prose remains: {phrase!r}"

        # Require one numbered month-table row for every canonical month and
        # require all three canonical identities on that same row. This also
        # works for ru/ja/ko profiles, whose local aliases are shown before the
        # canonical Latin forms in parentheses.
        lines = text.splitlines()
        for month in months:
            prefix = f"| {month['number']:02d} |"
            rows = [line for line in lines if line.startswith(prefix)]
            assert len(rows) == 1, f"{path}: expected exactly one table row for month {month['number']:02d}"
            row = rows[0]
            for field in ("canonical", "short6", "short4"):
                value = month[field]
                assert value in row, f"{path}: month {month['number']:02d} row missing canonical {field} {value}"

        # Where Tredecadia has an independently reviewed local-script month
        # profile, the corresponding README must use it. The expected maturity
        # comes from the stable transition plan: reviewed in RC2, then exact
        # accepted/rejected maturity in the stable candidate.
        profile_id = REVIEWED_PROFILE_BY_LOCALE.get(locale)
        if profile_id is not None:
            profile = profiles[profile_id]
            expected_status = expected_profile_status(profile_id, version, stable_plan)
            assert profile["review"]["status"] == expected_status, (
                f"{profile_id}: expected {expected_status}, got {profile['review']['status']}"
            )
            for alias in profile["aliases"]:
                for field in ("full", "short6", "short4"):
                    value = alias[field]
                    assert value in text, f"{path}: missing {profile_id} {field} alias {value}"

        assert path in root_readme, f"README.md does not link {path}"
        assert path in index, f"README.languages.md does not link {path}"

    assert len(set(LOCALES.values())) == len(LOCALES)
    assert len(LOCALES) == 21
    print("Tredecadia localized README validation: OK")


if __name__ == "__main__":
    main()
