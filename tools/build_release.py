#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a deterministic Tredecadia release bundle and SHA-256 checksum."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED_RELEASES = ROOT / "release" / "published-releases.json"

INCLUDE_FILES = (
    "README.md",
    "README.languages.md",
    "README.ru.md",
    "README.es.md",
    "README.pt-BR.md",
    "README.fr.md",
    "README.de.md",
    "README.it.md",
    "README.tr.md",
    "README.pl.md",
    "README.uk.md",
    "README.zh-CN.md",
    "README.zh-TW.md",
    "README.ja.md",
    "README.ko.md",
    "README.ar.md",
    "README.fa.md",
    "README.hi.md",
    "README.bn.md",
    "README.id.md",
    "README.vi.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "LICENSE.md",
    "LICENSES/CC-BY-4.0.md",
    "LICENSES/MIT.txt",
    "specification/calendar-standard.md",
    "specification/conversion-standard.md",
    "specification/date-notation.md",
    "specification/month-naming-standard.md",
    "specification/localization.md",
    "specification/localization-profiles.md",
    "specification/compatibility.md",
    "registry/calendar.json",
    "registry/calendar.schema.json",
    "registry/months.json",
    "registry/months.schema.json",
    "registry/localizations.json",
    "registry/localizations.schema.json",
    "tests/test-vectors.json",
    "tests/conversion-vectors.json",
    "tests/short4-ux-vectors.json",
    "tests/accessibility-vectors.json",
    "reference/python/README.md",
    "reference/python/tredecadia.py",
)


def citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(r'^version:\s*"([^"]+)"\s*$', text, re.MULTILINE)
    if match is None:
        raise ValueError("CITATION.cff does not contain a quoted version")
    return match.group(1)


def validate_version(version: str) -> None:
    if re.fullmatch(r"[0-9A-Za-z][0-9A-Za-z.-]*", version) is None:
        raise ValueError(f"unsafe release version: {version!r}")


def published_release(version: str) -> dict | None:
    if not PUBLISHED_RELEASES.is_file():
        return None
    data = json.loads(PUBLISHED_RELEASES.read_text(encoding="utf-8"))
    for entry in data["releases"]:
        if entry["version"] == version:
            return entry
    return None


def git_head() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    head = result.stdout.strip()
    return head if re.fullmatch(r"[0-9a-f]{40}", head) else None


def assert_source_lock(version: str) -> None:
    """Refuse to rebuild a published version from a different source commit.

    Published artifacts are immutable. After a tag is released, the default
    branch may legitimately gain documentation and tooling changes while its
    citation version still names the current public release. Reusing that
    version string for a new archive would create a second, different artifact
    with the same release identity, so known published versions are buildable
    only from their recorded source commit.
    """
    entry = published_release(version)
    if entry is None:
        return

    head = git_head()
    if head is None:
        raise RuntimeError(
            f"{version} is already published; source commit cannot be verified. "
            f"Check out {entry['tag']} ({entry['commit']}) in a Git repository to reproduce it."
        )
    if head != entry["commit"]:
        raise RuntimeError(
            f"{version} is already published from {entry['commit']}; current HEAD is {head}. "
            f"Check out {entry['tag']} to reproduce the published archive instead of creating "
            "a different archive with the same version."
        )


def tar_info(name: str, size: int) -> tarfile.TarInfo:
    info = tarfile.TarInfo(name=name)
    info.size = size
    info.mtime = 0
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""
    info.mode = 0o644
    return info


def build_bundle(output_dir: Path, version: str, *, enforce_source_lock: bool = True) -> tuple[Path, Path]:
    validate_version(version)
    if enforce_source_lock:
        assert_source_lock(version)
    output_dir.mkdir(parents=True, exist_ok=True)

    root_name = f"tredecadia-{version}"
    archive_path = output_dir / f"{root_name}.tar.gz"
    checksum_path = output_dir / "SHA256SUMS"

    missing = [path for path in INCLUDE_FILES if not (ROOT / path).is_file()]
    if missing:
        raise FileNotFoundError(f"release inputs missing: {missing}")

    manifest = {
        "project": "Tredecadia",
        "version": version,
        "files": list(INCLUDE_FILES),
    }
    manifest_bytes = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")

    raw_tar = io.BytesIO()
    with tarfile.open(fileobj=raw_tar, mode="w", format=tarfile.PAX_FORMAT) as tar:
        for relative in sorted(INCLUDE_FILES):
            payload = (ROOT / relative).read_bytes()
            info = tar_info(f"{root_name}/{relative}", len(payload))
            tar.addfile(info, io.BytesIO(payload))

        manifest_name = f"{root_name}/RELEASE-MANIFEST.json"
        tar.addfile(tar_info(manifest_name, len(manifest_bytes)), io.BytesIO(manifest_bytes))

    with archive_path.open("wb") as output:
        with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0, compresslevel=9) as gz:
            gz.write(raw_tar.getvalue())

    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    checksum_path.write_text(f"{digest}  {archive_path.name}\n", encoding="ascii", newline="\n")
    return archive_path, checksum_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=None, help="bundle version; defaults to CITATION.cff")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    version = args.version or citation_version()
    archive, checksum = build_bundle(args.output_dir, version)
    print(archive)
    print(checksum)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
