#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate repository-maintenance and GitHub Actions security invariants."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
PINNED_ACTION = re.compile(r"^\s*uses:\s*[^\s@]+@[0-9a-f]{40}(?:\s+#.*)?$")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    codeowners = text(".github/CODEOWNERS")
    assert "* @StanleyLl0yd" in codeowners

    dependabot = text(".github/dependabot.yml")
    assert "package-ecosystem: pip" in dependabot
    assert "package-ecosystem: github-actions" in dependabot
    assert dependabot.count("interval: weekly") == 2

    security = text("SECURITY.md")
    assert "Report a vulnerability" in security
    assert "Published tags and release artifacts are treated as immutable" in security

    workflow_texts: dict[str, str] = {}
    for path in sorted(WORKFLOWS.glob("*.yml")):
        body = path.read_text(encoding="utf-8")
        workflow_texts[path.name] = body
        assert "pull_request_target:" not in body, path
        for line in body.splitlines():
            if line.lstrip().startswith("uses:"):
                assert PINNED_ACTION.match(line), f"unpinned action in {path}: {line.strip()}"

    validate = workflow_texts["validate.yml"]
    assert "permissions:\n  contents: read" in validate
    assert "persist-credentials: false" in validate
    assert "timeout-minutes: 30" in validate
    assert "cancel-in-progress: true" in validate
    assert "python tests/validate_repo_security.py" in validate

    publish = workflow_texts["publish-release.yml"]
    assert "permissions:\n  contents: write" in publish
    assert "group: release-publication" in publish
    assert "cancel-in-progress: false" in publish
    assert "persist-credentials: false" in publish
    assert "timeout-minutes: 30" in publish
    assert "tests/validate_repo_security.py" in publish
    assert "refusing to overwrite it" in publish
    assert "test \"$TARGET\" = \"$GITHUB_SHA\"" in publish

    pages = workflow_texts["pages.yml"]
    assert "contents: read" in pages
    assert "pages: write" in pages
    assert "id-token: write" in pages
    assert "persist-credentials: false" in pages
    assert "workflow_dispatch:" in pages
    assert "\n  push:\n" in pages
    assert "branches: [main]" in pages
    assert '"docs/**"' in pages
    assert "pull_request:" not in pages

    housekeeping = workflow_texts["branch-housekeeping.yml"]
    assert "contents: write" in housekeeping
    assert "pull-requests: read" in housekeeping
    assert 'if [ "$branch" = "main" ]' in housekeeping
    assert 'open_count="$(gh pr list' in housekeeping
    assert 'merged_count="$(gh pr list' in housekeeping
    assert 'select(.mergedAt != null)' in housekeeping
    assert 'gh api --method DELETE' in housekeeping
    assert "m4/rc2-weekdays" in housekeeping
    assert "m4-pages-deployment" in housekeeping

    print("Tredecadia repository security/housekeeping validation: OK")


if __name__ == "__main__":
    main()
