# Roadmap

Tredecadia is intentionally pre-1.0 until the localization/implementation review and a complete release-candidate consistency audit are finished.

## M0 — Repository bootstrap

Status: **complete**

- publish draft specifications;
- publish canonical month registry and schema;
- encode naming/cycle invariants as executable checks;
- establish licensing, citation, contribution, and changelog metadata.

## M1 — Era and civil calendar semantics

Status: **complete**

- define the Tredecadia Era with a real year `0`;
- fix the mathematical origin at the conventional March-equinoctial civil boundary of 10000 BCE;
- define `EQ` as opening a year and `ED` as closing a leap year;
- define the proleptic-Gregorian astronomical conversion coordinate;
- define the exact leap rule;
- publish machine-readable calendar profile/schema;
- publish conversion vectors including epoch, BCE/CE, modern, century, and 400-year boundaries;
- verify bidirectional conversion and negative/zero/expanded year arithmetic;
- enforce cross-document and artifact-version consistency in CI.

## M2 — Internationalization and implementation review

Status: **in progress**

Tracked separately as issues #4, #5, and #6.

- [ ] review canonical stress/pronunciation wording (#4);
- [ ] add independently reviewed localization profiles (#6);
- [ ] test compact month forms in realistic interfaces;
- [x] implement a dependency-free Python reference converter (#5, implementation in review);
- [x] cross-check the reference implementation against the independent M1 oracle and published vectors (#5, implementation in review);
- [ ] review accessibility and parsing behavior for five-digit/signed years.

## M3 — v1.0 release candidate

- repository-wide specification/registry/test consistency audit;
- freeze compatibility-critical identifiers;
- finalize public documentation and GitHub Pages site;
- run release-candidate review before tagging.

## M4 — v1.0 publication

- tag `v1.0.0`;
- publish immutable release artifacts;
- archive the release with a DOI-capable repository such as Zenodo;
- publish citation metadata for the stable version.
