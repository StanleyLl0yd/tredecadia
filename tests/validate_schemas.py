#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate published registries with their Draft 2020-12 JSON Schemas."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

PAIRS = (
    ("registry/calendar.json", "registry/calendar.schema.json"),
    ("registry/months.json", "registry/months.schema.json"),
    ("registry/localizations.json", "registry/localizations.schema.json"),
)


def load(path: str) -> object:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    for instance_path, schema_path in PAIRS:
        instance = load(instance_path)
        schema = load(schema_path)
        assert isinstance(schema, dict)
        assert schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"

        # Check the schema itself before applying it. This catches malformed
        # keyword values that ordinary project assertions would not notice.
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
        if errors:
            lines = [f"{instance_path} failed {schema_path}:"]
            for error in errors:
                location = "/".join(str(part) for part in error.absolute_path) or "<root>"
                lines.append(f"- {location}: {error.message}")
            raise AssertionError("\n".join(lines))

    print("Tredecadia Draft 2020-12 schema validation: OK")


if __name__ == "__main__":
    main()
