# Roadmap

Tredecadia `v1.0.0` is published from the fully verified RC2 identity. RC1 and RC2 remain immutable historical releases; stable v1 preserves the published RC2 canonical calendar identity. The GitHub stable release and deterministic artifacts are recorded; only the optional external DOI/archive handoff remains from M4.

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

Status: **complete except external DOI/archive handoff — `v1.0.0` published and verified**

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
- [x] complete the fresh minimum one-full-day RC2 observation window;
- [x] accept the reviewed month-localization profiles `ru-Cyrl`, `ja-Kana`, and `ko-Hang` for stable promotion (#47).

### Stable v1.0 gate

The RC2 observation completed after the machine-enforced minimum interval with zero compatibility-critical findings and zero open reports. The atomic stable transition was published from exact source commit `8c272bf6a48b1b84a4b2ca8c1db43c6ffb9f5ce3`.

Stable transition checklist:

- [x] classify and resolve/defer all RC2 feedback; no compatibility-critical defect was found;
- [x] explicitly complete the RC2 observation and record the overall stable decision as approved;
- [x] rerun the complete compatibility/conversion/localization/accessibility/schema/reference/release audit;
- [x] prove stable candidate identity equals the published RC2 identity apart from planned version/status/maturity metadata;
- [x] prepare the three accepted month-localization profiles and registries for stable maturity in the atomic stable candidate;
- [x] prepare and verify the complete atomic public-version transition from `1.0.0-rc.2` to `1.0.0`;
- [x] tag and publish `v1.0.0` from exact clean source commit `8c272bf6a48b1b84a4b2ca8c1db43c6ffb9f5ce3`;
- [x] publish and re-verify deterministic stable release artifacts; `tredecadia-1.0.0.tar.gz` SHA-256 is `2f14cc4fb2bcac2cfcce280ddbe948d4c65cab098ce23c1d385d220709f5c392`;
- [ ] archive the stable release with a DOI-capable repository such as Zenodo and record final citation metadata.

## M5 — additional-script month localization profiles

Status: **in progress — `v1.1.0-rc.1` published and verified; observation open**

This milestone is a compatible minor-version localization expansion. It does not alter canonical month or weekday identity and does not rewrite the published `v1.0.0` registry.

- [x] build executable candidate mappings for `ka-Geor`, `hy-Armn`, `ar-Arab`, `hi-Deva`, `bn-Beng`, and `fa-Arab` (#60);
- [x] enforce deterministic Full / Short-6 / Short-4 derivation, uniqueness, reverse mapping, Unicode safety, and evidence rules;
- [x] separate technical candidate validity from explicit review decisions (#62);
- [x] resolve Bengali initial `/ja/` and `/z/` orthography using Government of Bangladesh dictionary evidence (#63);
- [x] resolve Iranian Persian `/i,u/` spelling versus short `/e,o/` using ALA-LC and Unicode evidence (#63);
- [x] clear all six profiles for `reviewed` maturity without claiming a native-speaker usability study;
- [x] promote the six accepted profiles into the normative `v1.1.0-rc.1` localization registry at `reviewed` maturity;
- [x] update reader-facing localized documentation for the six newly normative profiles;
- [x] run the complete v1.1 RC compatibility/release audit;
- [x] publish immutable `v1.1.0-rc.1` from source commit `8d1b5a0c05eab8875e95b9896fd1c386edfe1220`;
- [x] verify the remote tag and re-download/byte-compare the deterministic release assets; archive SHA-256 is `5b32dad3438572b67381ef5af05bf6fd915a2393fc69c8c132b7bef125ff876e`;
- [ ] complete the minimum one-full-day v1.1 RC observation no earlier than `2026-09-19T08:01:59Z`;
- [ ] classify all v1.1 RC feedback and require zero compatibility-critical findings/open reports for stable approval;
- [x] record an explicit stable acceptance decision for each of the six reviewed profiles, without waiving the independent RC observation gate;
- [x] define and CI-enforce the atomic `1.1.0-rc.1` → `1.1.0` transition contract against an immutable RC identity snapshot;
- [ ] apply and verify the atomic `1.1.0-rc.1` → `1.1.0` transition after observation approval;
- [ ] publish and re-verify stable `v1.1.0`.
