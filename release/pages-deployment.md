# GitHub Pages deployment status

Status: **live**

Tredecadia keeps its public website as a navigational layer over the repository. Normative source remains under `specification/` and `registry/`; the Pages site is not a second normative copy.

## Deployment contract

- `.github/workflows/pages.yml` builds `docs/` with GitHub's Jekyll Pages action;
- the workflow uses only official GitHub Pages actions pinned to immutable commit SHAs;
- deployment uses the `github-pages` environment and the minimum required permissions;
- `tests/validate_pages.py` checks the deployment contract in ordinary repository CI.

## Initial enablement finding

PR #35 merged the workflow as commit `56d9819fdc49473e3b7853eb5c03e34be155c554`.

The first real deployment attempt, workflow run `35026608479`, failed at `actions/configure-pages` because the repository had not yet enabled Pages with **Source = GitHub Actions**. PR #36 therefore changed deployment to an explicit manual gate while awaiting the one-time repository setting.

This was a repository-configuration issue, not a site-build failure.

## Successful deployment

GitHub Pages was enabled in **Settings → Pages → Build and deployment → Source → GitHub Actions**.

The manual **Deploy Pages** workflow was then run with `pages_enabled=true` from `main`:

- workflow run: `35065725007` (`Deploy Pages #2`);
- source commit: `a4c615a456a12a647417d029c474c286fa68ad3e`;
- `build`: **success**;
- `deploy`: **success**;
- Pages deployment result: **success**;
- published URL: <https://stanleyll0yd.github.io/tredecadia/>.

The deploy job itself returned that exact URL as the `github-pages` environment URL, so the address is no longer inferred from the repository name.

## Ongoing deployment

The workflow remains manually triggered by design. This keeps documentation deployment explicit during the RC/stable transition. A future maintenance change may add automatic deployment from `main` after stable `v1.0.0` if desired; that would be operational policy, not a calendar-identity change.

The GitHub repository remains the canonical source for normative specifications and registries.
