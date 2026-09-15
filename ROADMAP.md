# Roadmap

Tredecadia is intentionally pre-1.0 until the release-candidate audit and final publication gates are complete.

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

Status: **complete**

All M2 issues are closed. Draft 0.3 now includes pronunciation, conversational Short-4, accessibility, a reference converter, a localization review framework, and three independently reviewed non-Latin display profiles.

- [x] define pronunciation identity versus citation realization (#4, merged in #11);
- [x] choose weak initial reference prominence and make it abbreviation-stable (#4, #10, merged in #11);
- [x] add pronunciation conformance examples for Full / Short-6 / Short-4 (#9, merged in #11);
- [x] complete compact Short-4 conversational/UI review (#8, merged in #15);
- [x] define conservative Short-4 fuzzy/voice recognition behavior (#13, merged in #15);
- [x] define localization profile maturity/evidence rules and separated registry (#14, merged in #16);
- [x] promote Japanese Katakana to standards-reviewed (#17, merged in #18);
- [x] add standards-reviewed Korean Hangul profile (#19, merged in #20);
- [x] promote Russian Cyrillic to independently reviewed with explicit `MI/NI` approximation notes (#23, merged in #24);
- [x] close the overall localization review after confirming three reviewed profiles and all #6 deliverables;
- [x] implement a dependency-free Python reference converter (#5, merged in #7);
- [x] cross-check the reference implementation against the independent M1 oracle and published vectors (#5, merged in #7);
- [x] review accessibility and parsing behavior for five-digit/signed years (#21, merged in #22).

## M3 — v1.0 release candidate

Status: **in progress — tracked in #25 / PR #26**

- [x] begin repository-wide specification/registry/test inventory;
- [x] define the v1 compatibility-critical surface;
- [x] add an executable RC freeze gate for canonical calendar/month/localization identity;
- [x] add real Draft 2020-12 JSON Schema validation;
- [x] add repository-local Markdown/schema link validation;
- [ ] audit external review-evidence references;
- [ ] audit all version/schema relationships and transition Draft 0.3 to `1.0.0-rc.1`;
- [ ] prepare deterministic release artifacts and checksums;
- [ ] finalize public documentation / GitHub Pages structure;
- [ ] run final clean CI on the RC commit;
- [ ] tag `v1.0.0-rc.1` only after every #25 gate is complete.

## M4 — v1.0 publication

- promote explicitly accepted reviewed localization profiles to `stable`;
- tag `v1.0.0`;
- publish immutable release artifacts;
- archive the release with a DOI-capable repository such as Zenodo;
- publish citation metadata for the stable version.
