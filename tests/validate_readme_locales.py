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

PROFILE_BY_LOCALE = {
    "ru": "ru-Cyrl",
    "ja": "ja-Kana",
    "ko": "ko-Hang",
    "ka": "ka-Geor",
    "hy": "hy-Armn",
    "ar": "ar-Arab",
    "hi": "hi-Deva",
    "bn": "bn-Beng",
    "fa": "fa-Arab",
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


def main() -> None:
    version = citation_version()
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index = (ROOT / "README.languages.md").read_text(encoding="utf-8")
    months = load("registry/months.json")["months"]
    calendar = load("registry/calendar.json")
    weekdays = calendar["regularGrid"]["weekdays"]
    localization_registry = load("registry/localizations.json")
    profiles = {profile["id"]: profile for profile in localization_registry["profiles"]}

    assert "README.languages.md" in root_readme
    assert "README.md" in index
    assert [day["id"] for day in weekdays] == [f"W{i}" for i in range(1, 8)]
    weekday_cycle = " → ".join(f"{day['id']} {day['canonical']}" for day in weekdays)
    assert set(PROFILE_BY_LOCALE.values()) <= set(profiles)

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

        # Localized weekday aliases remain a separate, unreviewed surface.
        # Every README therefore exposes the exact canonical W1..W7 identity.
        assert weekday_cycle in text, f"{path}: canonical weekday cycle missing or out of order"
        for day in weekdays:
            assert day["id"] in text, f"{path}: missing canonical weekday ID {day['id']}"
            assert day["canonical"] in text, f"{path}: missing canonical weekday {day['canonical']}"

        assert "BCE" in text and "CE" in text, f"{path}: BCE/CE notation missing"
        assert "Before Common Era" in text, f"{path}: BCE expansion missing"
        assert "Common Era" in text, f"{path}: CE expansion missing"

        for phrase in UNLOCALIZED_PROSE:
            assert phrase not in lowered, f"{path}: untranslated English prose remains: {phrase!r}"

        lines = text.splitlines()
        profile_id = PROFILE_BY_LOCALE.get(locale)
        profile = profiles.get(profile_id) if profile_id else None
        aliases_by_month = {alias["month"]: alias for alias in profile["aliases"]} if profile else {}

        for month in months:
            prefix = f"| {month['number']:02d} |"
            rows = [line for line in lines if line.startswith(prefix)]
            assert len(rows) == 1, f"{path}: expected exactly one table row for month {month['number']:02d}"
            row = rows[0]
            # Canonical Latin identity remains visible even where a local-script
            # display alias is normative.
            for field in ("canonical", "short6", "short4"):
                value = month[field]
                assert value in row, f"{path}: month {month['number']:02d} row missing canonical {field} {value}"
            if profile is not None:
                alias = aliases_by_month[month["number"]]
                for field in ("full", "short6", "short4"):
                    value = alias[field]
                    assert value in row, f"{path}: month {month['number']:02d} row missing {profile_id} {field} alias {value}"

        if profile is not None:
            assert profile["review"]["status"] in {"reviewed", "stable"}, profile_id

        assert path in root_readme, f"README.md does not link {path}"
        assert path in index, f"README.languages.md does not link {path}"

    assert len(set(LOCALES.values())) == len(LOCALES)
    assert len(LOCALES) == 21
    print("Tredecadia localized README validation: OK")


if __name__ == "__main__":
    main()
