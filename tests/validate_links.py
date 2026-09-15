#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check repository-local Markdown and registry path references."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def local_target(source: Path, raw: str) -> Path | None:
    target = raw.strip()
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    # Optional Markdown title after a simple whitespace-separated destination
    # is not used by this repository; strip angle brackets if present.
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    return (source.parent / unquote(target)).resolve()


def validate_markdown_links() -> None:
    errors: list[str] = []
    for source in sorted(ROOT.rglob("*.md")):
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1)
            target = local_target(source, raw)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing target: {raw}")

    if errors:
        raise AssertionError("Broken repository-local Markdown links:\n" + "\n".join(f"- {item}" for item in errors))


def validate_registry_schema_links() -> None:
    for path in sorted((ROOT / "registry").glob("*.json")):
        if path.name.endswith(".schema.json"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        schema_ref = data.get("$schema")
        assert isinstance(schema_ref, str) and schema_ref, f"{path.name} lacks $schema"
        if schema_ref.startswith(("http://", "https://")):
            continue
        target = (path.parent / schema_ref).resolve()
        assert target.is_file(), f"{path.name}: missing schema target {schema_ref}"


def main() -> None:
    validate_markdown_links()
    validate_registry_schema_links()
    print("Tredecadia repository-local link validation: OK")


if __name__ == "__main__":
    main()
