# Roadmap

Tredecadia has published two immutable v1 release candidates. `v1.0.0-rc.2` carries the deliberate pre-stable compatibility correction that replaces the English weekday labels used by RC1 with internationally neutral canonical weekday identities. Final `v1.0.0` follows only after the fresh RC2 observation window is explicitly completed and approved.

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

All M2 issues are closed. The v1 RC includes pronunciation, conversational Short-4, accessibility, a reference converter, a localization review framework, and three independently reviewed non-Latin month-display profiles.

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

## M3 — first v1 release candidate

Status: **complete — `v1.0.0-rc.1` published and immutable**

- [x] inventory normative specifications and machine-readable artifacts;
- [x] define and executable-check the v1 compatibility-critical surface;
- [x] validate all published registries with a real Draft 2020-12 JSON Schema validator;
- [x] validate repository-local Markdown links and registry `$schema` paths;
- [x] recheck external localization review-evidence references;
- [x] audit canonical parser/confusable edge cases;
- [x] audit schema-version relationships;
- [x] transition every published artifact/specification version to `1.0.0-rc.1` without changing schema versions unnecessarily;
- [x] implement deterministic release artifacts and SHA-256 checksums;
- [x] prepare the public documentation / GitHub Pages structure;
- [x] publish `v1.0.0-rc.1` from commit `937d8d681fcce6095d6a4d196783136b908c1be5` as a GitHub prerelease;
- [x] attach and re-download/byte-verify the deterministic archive and `SHA256SUMS` in the publication workflow.

Historical RC1 archive SHA-256:

`018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf`

## M4 — RC2 correction and v1.0 publication

Status: **in progress — `v1.0.0-rc.2` published; fresh observation window open**

### RC2 compatibility correction

- [x] select seven internationally neutral canonical weekday names and stable machine IDs `W1..W7`;
- [x] prove the selected `E/O` CVCV set reaches the structural distance optimum and stays at character distance ≥3 from every canonical month Short-4;
- [x] record lexical clearance and exact candidate rationale (#42);
- [x] define an executable RC1 → RC2 compatibility-transition manifest (#44);
- [x] preserve RC1 tag/source/archive/identity and observation records as immutable history;
- [x] advance the calendar registry contract from schema `1` to schema `2` for structured weekday identity;
- [x] update normative week identity to `W1 Mene, W2 Noko, W3 Kese, W4 Zoyo, W5 Sote, W6 Yemo, W7 Toze`;
- [x] complete the repository-wide RC2 metadata/documentation/freeze migration and pass exact PR CI (#45, Validate #140);
- [x] publish immutable `v1.0.0-rc.2` from source commit `b816d613618d51515d910e0d3bdb9d2f211b6d22`;
- [x] verify the remote tag target and re-download/byte-compare the published release assets;
- [x] record RC2 publication at `2026-09-16T09:44:59Z` with archive SHA-256 `23e40180098c656c88aa4ba27c6989ac053d9ce8b8029c9ce2e3b16946bf32ec` (#46);
- [x] open a fresh minimum one-full-day RC2 observation window; earliest permitted completion is `2026-09-17T09:44:59Z`;
- [x] accept the reviewed month-localization profiles `ru-Cyrl`, `ja-Kana`, and `ko-Hang` for promotion in the future atomic stable commit (#47); RC2 registry status itself remains reviewed/draft until then.

### Stable v1.0 gate

Current machine-enforced blockers are the RC2 observation/approval gate and stable publication authorization. The time gate cannot be bypassed.

Only after `2026-09-17T09:44:59Z`, and only if review remains clean:

- [ ] classify and resolve/defer all RC2 feedback; publish another RC instead of mutating RC2 if a compatibility-critical defect is found;
- [ ] explicitly complete the RC2 observation and record the overall stable decision as approved or blocked;
- [ ] rerun the complete compatibility/conversion/localization/accessibility/schema/reference/release audit;
- [ ] prove stable candidate identity equals the published RC2 identity;
- [ ] promote the three accepted month-localization profiles and registries to stable in the atomic stable candidate;
- [ ] atomically transition public version metadata from `1.0.0-rc.2` to `1.0.0`;
- [ ] tag and publish `v1.0.0` only from a clean, fully verified `main` commit;
- [ ] publish immutable stable release artifacts and checksums;
- [ ] archive the stable release with a DOI-capable repository such as Zenodo and record final citation metadata.
