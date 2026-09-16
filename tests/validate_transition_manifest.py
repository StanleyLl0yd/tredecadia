#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the complete atomic RC2 -> stable metadata transition manifest."""

from __future__ import annotations

import json
from pathlib import Path

from release_state import citation_version

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = "release/stable-transition.json"

EXPECTED_VERSIONED_JSON = {
    "registry/calendar.json", "registry/months.json", "registry/localizations.json",
    "tests/test-vectors.json", "tests/conversion-vectors.json",
    "tests/short4-ux-vectors.json", "tests/accessibility-vectors.json",
}
EXPECTED_REGISTRIES = {"registry/calendar.json", "registry/months.json", "registry/localizations.json"}
EXPECTED_SPECS = {
    "specification/calendar-standard.md", "specification/conversion-standard.md",
    "specification/date-notation.md", "specification/month-naming-standard.md",
    "specification/localization.md", "specification/localization-profiles.md",
    "specification/compatibility.md",
}
LOCALIZED_READMES = {
    "README.ru.md", "README.es.md", "README.pt-BR.md", "README.fr.md",
    "README.de.md", "README.it.md", "README.tr.md", "README.pl.md",
    "README.uk.md", "README.zh-CN.md", "README.zh-TW.md", "README.ja.md",
    "README.ko.md", "README.ar.md", "README.fa.md", "README.hi.md",
    "README.bn.md", "README.id.md", "README.vi.md",
}
EXPECTED_PUBLIC_DOCS = {"README.md", "ROADMAP.md", "CONTRIBUTING.md", "docs/index.md", "CHANGELOG.md", *LOCALIZED_READMES}
EXPECTED_SCHEMAS = {"registry/calendar.schema.json", "registry/months.schema.json", "registry/localizations.schema.json"}
SCHEMA_VERSIONS = {
    "registry/calendar.schema.json": 2,
    "registry/months.schema.json": 3,
    "registry/localizations.schema.json": 1,
}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def all_atomic_paths(manifest: dict) -> set[str]:
    atomic = manifest["atomicCandidateCommit"]
    return {
        atomic["publicationTrigger"], atomic["citation"], atomic["stableReleaseNotes"], atomic["profileDecisionRecord"],
        *atomic["versionedJson"], *atomic["registryStatus"], *atomic["specificationStatusHeaders"], *atomic["publicVersionDocuments"],
    }


def source_reference_paths(source: str) -> set[str]:
    found: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(".git/"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if source in text:
            found.add(relative)
    return found


def validate_manifest_shape(manifest: dict) -> None:
    source = manifest["sourceVersion"]
    target = manifest["targetVersion"]
    assert manifest["manifestVersion"] == 2
    assert source == "1.0.0-rc.2"
    assert target == "1.0.0"

    atomic = manifest["atomicCandidateCommit"]
    assert atomic["requireSingleCommit"] is True
    assert atomic["publicationTrigger"] == "release/publish.json"
    assert atomic["citation"] == "CITATION.cff"
    assert atomic["stableReleaseNotes"] == "release/notes/1.0.0.md"
    assert atomic["profileDecisionRecord"] == "release/profile-readiness.json"
    assert set(atomic["versionedJson"]) == EXPECTED_VERSIONED_JSON
    assert set(atomic["registryStatus"]) == EXPECTED_REGISTRIES
    assert set(atomic["specificationStatusHeaders"]) == EXPECTED_SPECS
    assert set(atomic["publicVersionDocuments"]) == EXPECTED_PUBLIC_DOCS
    assert set(manifest["unchangedSchemaContracts"]) == EXPECTED_SCHEMAS

    pre = manifest["preconditions"]
    assert pre == {
        "stablePlan": "release/stable-plan.json",
        "publicationAllowed": True,
        "identityBaseline": "release/rc2-identity.json",
    }
    assert manifest["stableProfileMaturitySource"] == pre["stablePlan"]
    assert manifest["postPublication"]["archivePlan"] == "release/archive-plan.md"
    assert manifest["postPublication"]["doiMetadataMayFollow"] is True

    required = (
        all_atomic_paths(manifest)
        | set(manifest["unchangedSchemaContracts"])
        | set(manifest["historicalSourceReferences"])
        | set(manifest["historicalPredecessorReferences"])
        | {MANIFEST_PATH, pre["stablePlan"], pre["identityBaseline"], manifest["postPublication"]["archivePlan"]}
    )
    for path in required:
        assert (ROOT / path).is_file(), path


def validate_schema_freeze(manifest: dict) -> None:
    for path in manifest["unchangedSchemaContracts"]:
        schema = load(path)
        assert schema["properties"]["schemaVersion"]["const"] == SCHEMA_VERSIONS[path]


def validate_source_reference_coverage(manifest: dict) -> None:
    source = manifest["sourceVersion"]
    allowed = all_atomic_paths(manifest) | set(manifest["historicalSourceReferences"]) | {MANIFEST_PATH}
    unexpected = source_reference_paths(source) - allowed
    assert not unexpected, f"unclassified {source} references: {sorted(unexpected)}"


def validate_current_stage(manifest: dict) -> None:
    source = manifest["sourceVersion"]
    target = manifest["targetVersion"]
    version = citation_version()
    assert version in {source, target}

    atomic = manifest["atomicCandidateCommit"]
    publish = load(atomic["publicationTrigger"])
    stable_plan = load(manifest["preconditions"]["stablePlan"])
    profile_decisions = load(atomic["profileDecisionRecord"])
    notes = (ROOT / atomic["stableReleaseNotes"]).read_text(encoding="utf-8")

    for path in atomic["versionedJson"]:
        assert load(path)["specVersion"] == version, path

    packet_decisions = {entry["id"]: entry["decision"] for entry in profile_decisions["profiles"]}
    plan_decisions = {entry["id"]: entry["stableDecision"] for entry in stable_plan["localizationProfiles"]}
    assert packet_decisions == plan_decisions

    if version == source:
        assert publish == {"version": source, "tag": f"v{source}", "prerelease": True, "notes": f"release/notes/{source}.md"}
        for path in atomic["registryStatus"]:
            assert load(path)["status"] == "draft", path
        for path in atomic["specificationStatusHeaders"]:
            assert f"Status: **{source}" in (ROOT / path).read_text(encoding="utf-8"), path
        for path in atomic["publicVersionDocuments"]:
            assert source in (ROOT / path).read_text(encoding="utf-8"), path
        # Profile decisions may be resolved while RC2 observation is still
        # open. Resolution does not promote registry maturity or authorize
        # stable publication; those remain gated by the observation decision.
        assert all(decision in {"pending", "accepted", "rejected"} for decision in packet_decisions.values())
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" in notes
        assert stable_plan["publication"]["allowed"] is False
    else:
        assert stable_plan["publication"]["allowed"] is manifest["preconditions"]["publicationAllowed"] is True
        assert publish == {"version": target, "tag": f"v{target}", "prerelease": False, "notes": atomic["stableReleaseNotes"]}
        for path in atomic["registryStatus"]:
            assert load(path)["status"] == "stable", path
        for path in atomic["specificationStatusHeaders"]:
            assert f"Status: **{target}" in (ROOT / path).read_text(encoding="utf-8"), path
        for path in atomic["publicVersionDocuments"]:
            assert target in (ROOT / path).read_text(encoding="utf-8"), path
        assert all(decision in {"accepted", "rejected"} for decision in packet_decisions.values())
        assert "DRAFT — NOT AUTHORIZED FOR PUBLICATION" not in notes

    baseline = load(manifest["preconditions"]["identityBaseline"])
    assert baseline["release"]["tag"] == f"v{source}"
    assert baseline["schemaVersions"] == {"calendar": 2, "months": 3, "localizations": 1}
    assert stable_plan["identityBaseline"] == manifest["preconditions"]["identityBaseline"]


def main() -> None:
    manifest = load(MANIFEST_PATH)
    validate_manifest_shape(manifest)
    validate_schema_freeze(manifest)
    validate_source_reference_coverage(manifest)
    validate_current_stage(manifest)
    print("Tredecadia RC2 stable-transition manifest validation: OK")


if __name__ == "__main__":
    main()
