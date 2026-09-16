#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Prove that Tredecadia release bundles are deterministic and self-describing."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import build_release  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_localized_readme_coverage() -> None:
    language_index = (ROOT / "README.languages.md").read_text(encoding="utf-8")
    indexed = set(re.findall(r"\((README\.[A-Za-z0-9-]+\.md)\)", language_index))
    indexed.discard("README.languages.md")
    bundled = {
        path
        for path in build_release.INCLUDE_FILES
        if path.startswith("README.")
        and path.endswith(".md")
        and path not in {"README.md", "README.languages.md"}
    }
    assert indexed, "language index must expose localized README editions"
    assert bundled == indexed, (
        f"release localized README set differs from README.languages.md: "
        f"missing={sorted(indexed - bundled)}, extra={sorted(bundled - indexed)}"
    )


def main() -> None:
    # The default branch legitimately evolves after a published tag while
    # CITATION.cff still names the current public version. Determinism testing
    # therefore uses a synthetic, unpublished version rather than generating a
    # second archive that falsely claims the already-published RC identity.
    version = f"{build_release.citation_version()}.ci-snapshot"
    assert build_release.published_release(version) is None
    validate_localized_readme_coverage()

    with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
        first_archive, first_sums = build_release.build_bundle(Path(first_dir), version)
        second_archive, second_sums = build_release.build_bundle(Path(second_dir), version)

        first_bytes = first_archive.read_bytes()
        second_bytes = second_archive.read_bytes()
        assert first_bytes == second_bytes, "release archive is not byte-for-byte reproducible"
        assert first_sums.read_bytes() == second_sums.read_bytes()

        digest = sha256(first_archive)
        assert first_sums.read_text(encoding="ascii") == f"{digest}  {first_archive.name}\n"

        root_name = f"tredecadia-{version}"
        with tarfile.open(first_archive, "r:gz") as tar:
            names = tar.getnames()
            expected = [f"{root_name}/{path}" for path in sorted(build_release.INCLUDE_FILES)]
            expected.append(f"{root_name}/RELEASE-MANIFEST.json")
            assert names == expected

            members = tar.getmembers()
            assert all(member.mtime == 0 for member in members)
            assert all(member.uid == 0 and member.gid == 0 for member in members)
            assert all(member.uname == "" and member.gname == "" for member in members)

            manifest_member = tar.extractfile(f"{root_name}/RELEASE-MANIFEST.json")
            assert manifest_member is not None
            manifest = json.loads(manifest_member.read().decode("utf-8"))
            assert manifest == {
                "project": "Tredecadia",
                "version": version,
                "files": list(build_release.INCLUDE_FILES),
            }

    print("Tredecadia deterministic release bundle validation: OK")


if __name__ == "__main__":
    main()
