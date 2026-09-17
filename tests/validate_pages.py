#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the GitHub Pages deployment contract and public landing page."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"
INDEX = ROOT / "docs" / "index.md"
CONFIG = ROOT / "docs" / "_config.yml"
DEPLOYMENT_NOTE = ROOT / "release" / "pages-deployment.md"

EXPECTED_ACTIONS = {
    "actions/checkout": "3d3c42e5aac5ba805825da76410c181273ba90b1",  # v7.0.1
    "actions/configure-pages": "45bfe0192ca1faeb007ade9deae92b16b8254a0d",  # v6.0.0
    "actions/jekyll-build-pages": "44a6e6beabd48582f863aeeb6cb2151cc1716697",  # v1.0.13
    "actions/upload-pages-artifact": "fc324d3547104276b827a68afc52ff2a11cc49c9",  # v5.0.0
    "actions/deploy-pages": "368f82528645a54fb793d4d04e342629a3f51346",  # v5.0.1
}


def main() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    index = INDEX.read_text(encoding="utf-8")
    config = CONFIG.read_text(encoding="utf-8")
    deployment_note = DEPLOYMENT_NOTE.read_text(encoding="utf-8")

    for action, sha in EXPECTED_ACTIONS.items():
        needle = f"{action}@{sha}"
        assert needle in workflow, f"Pages workflow must pin {needle}"

    for permission in ("contents: read", "pages: write", "id-token: write"):
        assert permission in workflow, f"missing Pages permission: {permission}"

    # Deployment remains explicit during the RC/stable transition even though
    # the one-time repository Pages setting has now been enabled successfully.
    assert "workflow_dispatch:" in workflow
    assert "pages_enabled:" in workflow
    assert "if: ${{ inputs.pages_enabled }}" in workflow
    assert "\n  push:\n" not in workflow

    assert "environment:" in workflow and "name: github-pages" in workflow
    assert "source: ./docs" in workflow
    assert "destination: ./_site" in workflow
    assert "path: ./_site" in workflow

    # Keep a durable record of both the original operational finding and the
    # later successful deployment that closed it.
    assert "Status: **live**" in deployment_note
    assert "35026608479" in deployment_note
    assert "35065725007" in deployment_note
    assert "a4c615a456a12a647417d029c474c286fa68ad3e" in deployment_note
    assert "https://stanleyll0yd.github.io/tredecadia/" in deployment_note
    assert "external-enable-required" not in deployment_note

    # The website is a navigation layer, never a second normative source.
    assert "navigational summary, not a second copy of the standard" in index
    assert "The GitHub repository is the canonical source" in index
    assert "specification/calendar-standard.md" in index
    assert "registry" in index
    assert "README.languages.md" in index, "Pages should expose the multilingual entry point"
    # Locale counts change as translations are added. Keep the landing-page
    # link count-free so it cannot silently become stale again.
    assert "Read the project introduction in all available languages" in index

    assert "theme: jekyll-theme-minimal" in config
    assert "title: Tredecadia" in config

    print("Tredecadia Pages deployment validation: OK")


if __name__ == "__main__":
    main()
