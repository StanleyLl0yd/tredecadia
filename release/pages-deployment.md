# GitHub Pages deployment status

Status: **external-enable-required**

Tredecadia keeps its public website as a navigational layer over the repository. Normative source remains under `specification/` and `registry/`; the Pages site must not become a second normative copy.

## What has been implemented

- `.github/workflows/pages.yml` builds `docs/` with GitHub's Jekyll Pages action;
- the workflow uses only official GitHub Pages actions pinned to immutable commit SHAs;
- deployment uses the `github-pages` environment and the minimum required permissions;
- `tests/validate_pages.py` checks the deployment contract in ordinary repository CI.

## First deployment attempt

PR #35 merged the workflow as commit `56d9819fdc49473e3b7853eb5c03e34be155c554`.

The first real deployment attempt was workflow run `35026608479`. It failed at `actions/configure-pages` before site generation with GitHub's response that the repository does not yet have Pages enabled/configured for GitHub Actions.

This is a repository setting, not a site-build failure.

## One-time external prerequisite

In the GitHub repository UI:

1. Open **Settings**.
2. Open **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.

The installed GitHub connector cannot mutate this repository-administration setting, and GitHub's `GITHUB_TOKEN` is not permitted to perform first-time Pages enablement.

## Verification after enablement

After the setting above exists:

1. Open the **Deploy Pages** workflow.
2. Run it manually.
3. Confirm the `pages_enabled` input.
4. Require both `build` and `deploy` jobs to succeed.
5. Record the returned Pages URL in M4 issue #29.
6. Fetch the public URL independently and verify that the rendered page identifies GitHub as the canonical source and links to the multilingual README index and published RC.

Only after those checks should M4 Phase A's Pages checkbox be marked complete.

The default GitHub Pages URL is expected to be under the repository owner's `github.io` site, but Tredecadia does not treat any URL as confirmed until a successful deployment returns it.
