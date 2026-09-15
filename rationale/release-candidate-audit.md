# v1 Release-Candidate Audit Record

Status: **`1.0.0-rc.1` published and verified**  
Audit started: **2026-09-15**  
Publication completed: **2026-09-15**  
Tracking issue: `#25`

This document is non-normative. It records what was checked while preparing and publishing the first Tredecadia v1 release candidate.

## Milestone entry state

At M3 entry:

- M0 repository bootstrap was complete;
- M1 era/calendar/conversion semantics were complete;
- M2 pronunciation, Short-4 UX, accessibility, reference implementation, localization framework, and reviewed localization-profile work were complete;
- all M2 issues were closed;
- no compatibility-critical month-name search was reopened.

## Normative specification inventory

The RC audit treats the following files as normative specification documents:

- `specification/calendar-standard.md`;
- `specification/conversion-standard.md`;
- `specification/date-notation.md`;
- `specification/month-naming-standard.md`;
- `specification/localization.md`;
- `specification/localization-profiles.md`;
- `specification/compatibility.md`.

## Machine-readable inventory

Canonical registries:

- `registry/calendar.json` + `calendar.schema.json`;
- `registry/months.json` + `months.schema.json`;
- `registry/localizations.json` + `localizations.schema.json`.

Published conformance/decision vectors:

- `tests/test-vectors.json`;
- `tests/conversion-vectors.json`;
- `tests/short4-ux-vectors.json`;
- `tests/accessibility-vectors.json`.

Executable conformance aids include the independent calendar arithmetic oracle, registry/localization/UX/accessibility checks, RC freeze checks, and `reference/python/tredecadia.py`.

## Compatibility freeze

`specification/compatibility.md` defines the intended v1 stable identity boundary. `tests/validate_rc_freeze.py` independently pins the compatibility-critical calendar constants, era origin, conversion formulas, canonical month order/names/syllables/abbreviations, pronunciation policy, and reviewed localization maps.

Any change to that frozen surface during RC preparation must be intentional, documented, and reviewed rather than hidden inside an editorial change.

No compatibility-critical value changed between the final audited RC branch state and the published release target.

## JSON Schema audit

Earlier draft CI checked registry structure with project-specific assertions but did not execute the published Draft 2020-12 schemas with a standards implementation.

M3 added:

- pinned test dependency `jsonschema==4.26.0`;
- `Draft202012Validator.check_schema()` on every published registry schema;
- actual instance validation for all three published registries.

Project-specific semantic assertions remain in place because JSON Schema alone cannot express every cross-file or mathematical invariant.

## Version and schema relationship audit

The RC specification version is `1.0.0-rc.1` across all registries, published vector sets, normative specification status headers, citation metadata, release metadata, and public documentation.

Schema versions intentionally remain:

- calendar registry schema: `1`;
- canonical month registry schema: `3`;
- localization registry schema: `1`.

A release-version change does not by itself require a schema-version bump. No schema contract changed during the Draft 0.3 → RC version transition.

Registry `status` remains `draft` during the RC. Localization profiles remain `reviewed`, not `stable`. Those states change only as part of the explicit final `v1.0.0` release decision.

## Repository-local link audit

M3 added an executable scan of repository-local Markdown links and registry `$schema` paths. Links that escape the repository, point to missing files, or reference missing local schemas fail CI.

External web references are intentionally audited separately so transient network conditions do not make ordinary CI nondeterministic.

## External review-evidence audit

The localization registry records independent evidence for every profile currently marked `reviewed`.

Evidence references were rechecked during RC preparation on 2026-09-15:

### Japanese `ja-Kana`

- Agency for Cultural Affairs, Japan — `外来語の表記`:
  https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/
- authoritative page was retrievable in the RC web audit and exposes the foreign-word notation tables/guidance.

### Korean `ko-Hang`

- National Institute of Korean Language — `외래어 표기법`:
  https://www.korean.go.kr/kornorms/m/m_regltn.do?regltn_code=0003
- authoritative page was retrievable in the RC web audit; it exposes the current rule text and IPA-to-Hangul table.

### Russian `ru-Cyrl`

- Большая российская энциклопедия — `Транскрипция`:
  https://old.bigenc.ru/linguistics/text/4199684
- indexed/retrievable in the RC web audit and contains the practical-transcription discussion cited by the profile.
- Gramota.ru — `Буквы а — я, у — ю`:
  https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/bukvy-a-ya-u-yu
- Gramota.ru — `Буквы и — ы`:
  https://gramota.ru/biblioteka/spravochniki/pravila-russkoy-orfografii-i-punktuatsii/bukvy-i-y
- both orthographic pages were indexed/retrievable in the RC web audit and support the documented `YA` behavior and `MI/NI` palatalization note.

The evidence audit checks existence and applicability; it does not convert an evidence-based profile review into a claim of a separate native-speaker usability study.

## Machine syntax audit

M2/M3 canonical parsing checks cover:

- signed year zero/negative boundary cases;
- ASCII-only canonical digits;
- ASCII hyphen-minus for negative machine years;
- rejection of leading plus signs and negative zero;
- rejection of redundant year padding;
- rejection of Unicode minus and non-ASCII digit confusables;
- valid/invalid month and day ranges;
- uppercase `EQ`/`ED` only;
- conditional validity of `ED`;
- strict round-trip conversion across wide positive/negative ranges.

## Deterministic release packaging

`tools/build_release.py` builds `tredecadia-1.0.0-rc.1.tar.gz`, embeds a deterministic `RELEASE-MANIFEST.json`, and emits `SHA256SUMS`.

CI builds the bundle twice in independent temporary directories and requires byte-for-byte identical archives and checksum files. Tar ownership/timestamps and the gzip timestamp/filename fields are normalized.

The published archive has SHA-256:

`018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf`

The published `SHA256SUMS` asset is itself reported by GitHub with digest:

`bc0c0084154068d033fff8b0f44c3b0b42c2e56f6c6ac98941f421908d956006`

## Public documentation

GitHub Pages source lives under `docs/`. It is intentionally a navigational/public summary rather than a duplicate normative specification. The canonical source remains `specification/` plus the machine-readable registries. CI checks the duplicated month table on the Pages page against `registry/months.json`.

## Localization RC state

The three reviewed profiles are intentionally still `reviewed`, not `stable`, during `1.0.0-rc.1`:

- `ru-Cyrl`;
- `ja-Kana`;
- `ko-Hang`.

Final promotion to `stable` is reserved for the final `v1.0.0` release action. This prevents an RC from claiming final profile stability prematurely.

## Publication gate

Release publication is explicit and separate from ordinary validation. `release/publish.json` is the deliberate publication trigger.

The guarded workflow:

1. validates release metadata against citation/version/changelog data;
2. reruns the complete release conformance suite before publishing anything;
3. builds deterministic release assets;
4. refuses to overwrite an existing release/tag;
5. creates the release tag at the exact checked `GITHUB_SHA`;
6. publishes the GitHub prerelease and two assets;
7. verifies the remote tag target and release metadata;
8. re-downloads both assets and byte-compares them with the local deterministic build.

## Final publication record

The M3 gates completed as follows:

- exact RC branch commit: `7a6cdfd21d6d0ef653a7737802a65f8bede6b7f4` — Validate run #67: **success**;
- PR #26 merged to `main` as `50a13cdae8c3340fb293d1178b5acf2028c44ccf` — Validate run #68: **success**;
- guarded publication workflow added via PR #27; final PR head `370d6aae6194bae00846596b86b916a8063fd144` — Validate run #70: **success**;
- PR #27 merged to `main` as `937d8d681fcce6095d6a4d196783136b908c1be5`;
- release-target `main` Validate run #71: **success**;
- Publish Release run #1: **success**, including post-publication asset download and byte comparison;
- tag: `v1.0.0-rc.1`;
- GitHub release: `Tredecadia 1.0.0-rc.1`, `prerelease=true`, `draft=false`;
- tag/release target: exactly `937d8d681fcce6095d6a4d196783136b908c1be5`;
- assets: `tredecadia-1.0.0-rc.1.tar.gz` and `SHA256SUMS`.

All publication gates succeeded. No compatibility-critical defect was found during M3. The hardening work exposed missing validation and release-engineering coverage rather than semantic inconsistencies.

M3 is complete. Further incompatible changes belong only to a reopened RC defect review; ordinary next work is M4 evaluation of the public RC before final `v1.0.0` stabilization.
