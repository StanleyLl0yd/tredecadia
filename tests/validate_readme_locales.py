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


def main() -> None:
    version = citation_version()
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    index = (ROOT / "README.languages.md").read_text(encoding="utf-8")
    months = json.loads((ROOT / "registry/months.json").read_text(encoding="utf-8"))["months"]

    assert "README.languages.md" in root_readme
    assert "README.md" in index

    for locale, path in LOCALES.items():
        file = ROOT / path
        assert file.is_file(), f"missing localized README: {path}"
        text = file.read_text(encoding="utf-8")

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

        for month in months:
            for field in ("canonical", "short6", "short4"):
                value = month[field]
                assert value in text, f"{path}: missing canonical {field} {value}"

        assert path in root_readme, f"README.md does not link {path}"
        assert path in index, f"README.languages.md does not link {path}"

    assert len(set(LOCALES.values())) == len(LOCALES)
    assert len(LOCALES) == 19
    print("Tredecadia localized README validation: OK")


if __name__ == "__main__":
    main()
