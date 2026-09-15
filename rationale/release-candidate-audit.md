# v1 Release-Candidate Audit Record

Status: **`1.0.0-rc.1` final validation record**  
Audit started: **2026-09-15**  
Tracking issue: `#25`

This document is non-normative. It records what was checked while preparing the first Tredecadia v1 release candidate.

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

## JSON Schema audit

Earlier draft CI checked registry structure with project-specific assertions but did not execute the published Draft 2020-12 schemas with a standards implementation.

M3 adds:

- pinned test dependency `jsonschema==4.26.0`;
- `Draft202012Validator.check_schema()` on every published registry schema;
- actual instance validation for all three published registries.

Project-specific semantic assertions remain in place because JSON Schema alone cannot express every cross-file or mathematical invariant.

## Version and schema relationship audit

The RC specification version is `1.0.0-rc.1` across all registries, published vector sets, normative specification status headers, citation metadata, and public documentation.

Schema versions intentionally remain:

- calendar registry schema: `1`;
- canonical month registry schema: `3`;
- localization registry schema: `1`.

A release-version change does not by itself require a schema-version bump. No schema contract changed during the Draft 0.3 → RC version transition.

Registry `status` remains `draft` during the RC. Localization profiles remain `reviewed`, not `stable`. Those states change only as part of the explicit final `v1.0.0` release decision.

## Repository-local link audit

M3 adds an executable scan of repository-local Markdown links and registry `$schema` paths. Links that escape the repository, point to missing files, or reference missing local schemas fail CI.

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

## Public documentation

GitHub Pages source lives under `docs/`. It is intentionally a navigational/public summary rather than a duplicate normative specification. The canonical source remains `specification/` plus the machine-readable registries. CI checks the duplicated month table on the Pages page against `registry/months.json`.

## Localization RC state

The three reviewed profiles are intentionally still `reviewed`, not `stable`, during `1.0.0-rc.1`:

- `ru-Cyrl`;
- `ja-Kana`;
- `ko-Hang`.

Final promotion to `stable` is reserved for the final `v1.0.0` release action. This prevents an RC from claiming final profile stability prematurely.

## Remaining RC gates

Before tagging `v1.0.0-rc.1`:

- run the complete CI suite on the exact RC commit;
- merge that exact reviewed state to `main`;
- require clean post-merge CI on `main`;
- verify the tag target equals the clean main commit;
- publish the RC tag/release and deterministic bundle/checksum artifacts;
- close issue `#25` with the final audit result.

No compatibility-critical defect was found during the M3 audit. The hardening work exposed missing validation coverage and release engineering gaps rather than semantic inconsistencies.
