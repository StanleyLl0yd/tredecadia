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


def main() -> None:
    version = citation_version()
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index = (ROOT / "README.languages.md").read_text(encoding="utf-8")
    months = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]
    calendar = json.loads((ROOT / "registry/calendar.json").read_text(encoding="utf-8"))
    weekdays = calendar["regularGrid"]["weekdays"]
    localization_registry = json.loads((ROOT / "registry/localizations.json").read_text(encoding="utf-8"))
    profiles = {profile["id"]: profile for profile in localization_registry["profiles"]}

    assert "README.languages.md" in root_readme
    assert "README.md" in index
    assert [day["id"] for day in weekdays] == [f"W{i}" for i in range(1, 8)]

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

        # Every localized introduction must expose the language-neutral RC2
        # weekday identity. Localized weekday aliases remain a separate,
        # unreviewed surface and must not replace these canonical forms.
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

        # Canonical Latin identifiers stay visible in every edition so a
        # reader can map prose back to the normative registry.
        for month in months:
            for field in ("canonical", "short6", "short4"):
                value = month[field]
                assert value in text, f"{path}: missing canonical {field} {value}"

        # Where Tredecadia already has an independently reviewed local-script
        # month profile, the corresponding reader-facing README must actually
        # use it instead of showing only the English/Latin spellings. These
        # profiles do not imply any reviewed weekday alias.
        profile_id = REVIEWED_PROFILE_BY_LOCALE.get(locale)
        if profile_id is not None:
            profile = profiles[profile_id]
            assert profile["review"]["status"] == "reviewed", profile_id
            for alias in profile["aliases"]:
                for field in ("full", "short6", "short4"):
                    value = alias[field]
                    assert value in text, f"{path}: missing reviewed {profile_id} {field} alias {value}"

        assert path in root_readme, f"README.md does not link {path}"
        assert path in index, f"README.languages.md does not link {path}"

    assert len(set(LOCALES.values())) == len(LOCALES)
    assert len(LOCALES) == 19
    print("Tredecadia localized README validation: OK")


if __name__ == "__main__":
    main()
