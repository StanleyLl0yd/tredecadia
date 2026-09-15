# Tredecadia

Tredecadia is an open 13 × 28 perennial calendar standard with equal months, stable weekdays, a continuous mathematical year coordinate, and internationally neutral month names.

> **Status: `1.0.0-rc.1` release candidate — published.** M0–M3 are complete. The v1 compatibility surface is frozen for release-candidate testing; reviewed localization profiles remain non-stable until final `v1.0.0` acceptance.

Published release: [`v1.0.0-rc.1`](https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0-rc.1)

## Core model

- 13 months × 28 days = 364 regular in-month days.
- Every month has exactly four complete weeks.
- Day `01` of every month is Monday; day `28` is Sunday.
- **Equinox / New Year Day (`EQ`) opens each Tredecadia year** and is outside the month/week cycle.
- A leap year has one additional intercalary **Earth Day (`ED`)** after month 13 day 28 and immediately before the next year's `EQ`.
- The canonical month names are designed for international neutrality and high mutual distinguishability.

Ordinary-year boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Leap-year boundary:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Tredecadia Era

Tredecadia uses the **Tredecadia Era (TE)**, a single integer year coordinate with a real year `0`.

The mathematical origin is:

`TE 00000-EQ ↔ proleptic Gregorian astronomical year -9999, March 20`

Astronomical Gregorian year `-9999` is conventionally described as **10000 BCE**. The epoch is not claimed to be the beginning of humanity, civilization, agriculture, the Holocene, or any historical process. It is only the mathematical origin of the Tredecadia year coordinate.

Tredecadia does not use BCE/CE internally:

```text
…  -2  -1   0   1   2  …  9999  10000  …  12025 …
```

For the civil conversion profile, if `G` is the astronomical Gregorian year containing a Tredecadia year's `EQ` and `01-01`:

`TE year = G + 9999`

Examples:

| External year | Astronomical G | Tredecadia year |
|---|---:|---:|
| 10000 BCE | -9999 | 0 |
| 1 BCE | 0 | 9999 |
| 1 CE | 1 | 10000 |
| 2026 CE | 2026 | 12025 |

The March-20 anchor is a deterministic **civil convention associated with the March equinox**. It is not a claim that the astronomical equinox instant occurs on March 20 in every year, location, or time scale.

## Date presentation

Canonical interchange uses a strict ASCII form with a minimum five-digit year field, for example `12025-07-11`, `00000-EQ`, and `-00001-01-01`.

Human-facing presentation may suppress leading zeroes and may use a typographic minus sign, for example `1 TE` or `−1 TE`. These are display forms, not alternate canonical identifiers.

Accessible interfaces should expose the era, signed integer year, month/day identity, and named intercalary day semantically. `EQ` should be presented accessibly as **Equinox / New Year Day** and `ED` as **Earth Day**, rather than relying on the two-letter machine tokens alone.

## Month pronunciation

Month identity is the ordered sequence of five canonical CV syllables. Stress is not identity-critical.

Tredecadia's reference/citation pronunciation uses **weak initial prominence on the first syllable**. Full, Short-6, and Short-4 forms keep that same reference-prominence location, so shortening never moves the citation stress.

Short-4 is the preferred conversational compact form when the month context is already clear; Short-6 remains the safer written/display abbreviation where more redundancy helps. Fuzzy or low-confidence recognition must not silently turn one valid Short-4 month into another.

Localized speech may adapt stress, rhythm, and predictable allophony to the target language while preserving the recognizable canonical segmental sequence.

## Localization profiles

Canonical months and localized aliases are intentionally separate machine registries:

- `registry/months.json` contains language-neutral canonical identity;
- `registry/localizations.json` contains language/script display aliases.

Localization profiles progress through `candidate` → `reviewed` → `stable`; generated mappings cannot skip independent review.

`1.0.0-rc.1` contains three **reviewed, non-stable** profiles:

- Russian Cyrillic (`ru-Cyrl`) — reviewed against independent Russian practical-transcription and orthographic references; `ми/ни` palatalization is explicitly documented as a localization approximation;
- Japanese Katakana (`ja-Kana`) — reviewed against Japan's official foreign-word orthographic guidance;
- Korean Hangul (`ko-Hang`) — reviewed against Korea's official IPA-to-Hangul foreign-word rules.

No localization profile is stable in the RC. Stable status is reserved for profiles explicitly accepted into the final `v1.0.0` release.

## Specification

- [`specification/calendar-standard.md`](specification/calendar-standard.md) — calendar structure and Tredecadia Era.
- [`specification/conversion-standard.md`](specification/conversion-standard.md) — proleptic-Gregorian civil conversion.
- [`specification/month-naming-standard.md`](specification/month-naming-standard.md) — canonical month names, pronunciation, abbreviations, and Short-4 recognition.
- [`specification/date-notation.md`](specification/date-notation.md) — canonical date representation and accessible human presentation.
- [`specification/localization.md`](specification/localization.md) — localization semantics.
- [`specification/localization-profiles.md`](specification/localization-profiles.md) — profile methods, maturity, evidence, and promotion.
- [`specification/compatibility.md`](specification/compatibility.md) — v1 compatibility boundary and versioning rules.

Machine-readable data lives in [`registry/`](registry/); verification vectors and executable checks live in [`tests/`](tests/). Design rationale is intentionally separated from normative text in [`rationale/`](rationale/).

## Canonical months

| # | Full name | Short-6 | Short-4 |
|---:|---|---|---|
| 01 | Masanumika | Masanu | Masa |
| 02 | Tasuzunumu | Tasuzu | Tasu |
| 03 | Nazumasanu | Nazuma | Nazu |
| 04 | Mikasumani | Mikasu | Mika |
| 05 | Yanimuzunu | Yanimu | Yani |
| 06 | Zumitanasu | Zumita | Zumi |
| 07 | Muyasanumi | Muyasa | Muya |
| 08 | Sunizusaka | Sunizu | Suni |
| 09 | Numanamuta | Numana | Numa |
| 10 | Kazunusuya | Kazunu | Kazu |
| 11 | Yanazumasa | Yanazu | Yana |
| 12 | Sanumikazu | Sanumi | Sanu |
| 13 | Nimutazuna | Nimuta | Nimu |

## Example

Proleptic Gregorian `2026-09-15` maps to:

`TE 12025-07-11`

The Tredecadia weekday is determined by the regular-month day number, not by the weekday label of the corresponding Gregorian civil date.

## Python reference implementation

A dependency-free reference converter is available at [`reference/python/tredecadia.py`](reference/python/tredecadia.py). It is executable documentation and a conformance aid; the specification and registries remain normative.

```console
$ python reference/python/tredecadia.py from-gregorian 2026-09-15
12025-07-11

$ python reference/python/tredecadia.py to-gregorian 00000-EQ
-9999-03-20
```

The reference code supports negative and zero astronomical Gregorian years, negative and zero Tredecadia years, `EQ`, conditional `ED`, strict canonical ASCII Tredecadia parsing, human display-year formatting, and both conversion directions. CI cross-checks it against the published vectors and the independent calendar-arithmetic oracle. See [`reference/python/README.md`](reference/python/README.md).

## Release-candidate verification

The RC CI validates the published JSON Schemas with a Draft 2020-12 implementation, checks local links and duplicated canonical tables, freezes compatibility-critical constants, exhaustively cross-checks calendar conversion windows, and proves that the release bundle is byte-for-byte reproducible.

The published prerelease tag points to commit `937d8d681fcce6095d6a4d196783136b908c1be5`. The guarded publication workflow reran the complete release conformance suite, built the deterministic archive, published it with `SHA256SUMS`, downloaded both assets again, and byte-compared them with the local build.

Published archive SHA-256:

`018a804f518b3cbff402e91f5aba7d7aba05361f6bf4b01de593c8ac17a0abdf`

`tools/build_release.py` reproduces `tredecadia-1.0.0-rc.1.tar.gz`; the archive embeds `RELEASE-MANIFEST.json` listing the included source files.

## Licensing

Documentation, specifications, machine-readable registries, and test vectors are licensed under **CC BY 4.0**. Source code, scripts, and CI/workflow code are licensed under the **MIT License** unless a file states otherwise. See [`LICENSE.md`](LICENSE.md).

The licenses do not grant trademark rights in the Tredecadia name or branding.

## Versioning

The published public version is **`1.0.0-rc.1`**. The compatibility-critical v1 surface is frozen for RC testing, but incompatible corrections remain possible before final `v1.0.0` if public RC review uncovers a genuine correctness or interoperability defect.
