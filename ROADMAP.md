# Roadmap

Tredecadia published `v1.0.0-rc.1` and subsequently identified one deliberate pre-stable compatibility correction: replace English weekday labels with internationally neutral canonical weekday identities. `v1.0.0-rc.2` carries that correction; final `v1.0.0` follows only after RC2 publication, a fresh observation period, and explicit stable decisions.

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

Status: **in progress — `v1.0.0-rc.2` candidate / publication preparation**

### RC2 compatibility correction

- [x] select seven internationally neutral canonical weekday names and stable machine IDs `W1..W7`;
- [x] prove the selected `E/O` CVCV set reaches the structural distance optimum and stays at character distance ≥3 from every canonical month Short-4;
- [x] record lexical clearance and exact candidate rationale (#42);
- [x] define an executable RC1 → RC2 compatibility-transition manifest (#44);
- [x] preserve RC1 tag/source/archive/identity and observation records as immutable history;
- [x] advance the calendar registry contract from schema `1` to schema `2` for structured weekday identity;
- [x] update normative week identity to `W1 Mene, W2 Noko, W3 Kese, W4 Zoyo, W5 Sote, W6 Yemo, W7 Toze`;
- [ ] complete repository-wide RC2 metadata/documentation/freeze migration and obtain clean exact-candidate CI;
- [ ] publish immutable `v1.0.0-rc.2` assets and verify tag target plus re-downloaded assets;
- [ ] record the exact published RC2 source commit and archive digest;
- [ ] start a fresh minimum one-full-day RC2 observation window from the actual publication timestamp.

### Stable v1.0 gate

Only after RC2 observation is complete:

- [ ] classify and resolve/defer RC2 feedback; publish another RC instead of mutating RC2 if a compatibility-critical defect is found;
- [ ] explicitly decide whether each reviewed month-localization profile (`ru-Cyrl`, `ja-Kana`, `ko-Hang`) is accepted as `stable` for v1.0;
- [ ] rerun the complete compatibility/conversion/localization/accessibility/schema/reference/release audit;
- [ ] prove stable candidate identity equals the accepted RC2 identity;
- [ ] change accepted registry/profile maturity to stable and atomically transition public version metadata from `1.0.0-rc.2` to `1.0.0`;
- [ ] tag and publish `v1.0.0` only from a clean, fully verified `main` commit;
- [ ] publish immutable stable release artifacts and checksums;
- [ ] archive the stable release with a DOI-capable repository such as Zenodo and record final citation metadata.
