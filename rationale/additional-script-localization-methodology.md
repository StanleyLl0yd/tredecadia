# Additional-script month localization methodology

Status: **M5 research / v1.1.0 candidate preparation**

This document records the review logic for six proposed month-display profiles that are not part of the published `v1.0.0` localization registry. The executable source is `rationale/additional-script-localization-candidates.json`; review outcomes are recorded separately in `rationale/additional-script-localization-decisions.json`.

## Compatibility boundary

Tredecadia v1 canonical month identity remains the ASCII Latin names and canonical syllable sequences in `registry/months.json`. Display aliases do not redefine those identifiers.

The stable compatibility policy classifies a new localization profile as a compatible **minor** addition. These profiles therefore target `1.1.0`; they MUST NOT be inserted into the already published `1.0.0` registry while still claiming to be the same release.

Weekday aliases are out of scope. Their independent canonical `E/O` inventory and all seven `W1..W7` identities require a separate review surface.

## Common construction rule

Every proposal supplies one deterministic target-script string for each canonical month syllable:

`MA MI MU NA NI NU SA SU TA YA KA ZU`

Full, Short-6 and Short-4 aliases are derived by concatenating five, three and two mapped syllables respectively. No alias is entered independently of that derivation.

Promotion gates:

1. all 12 mapped syllables are non-empty and distinct;
2. every alias is NFC-normalized and contains no bidi-control or zero-width separator characters;
3. all 13 Full, Short-6 and Short-4 values are unique at each level;
4. every generated alias reverses to exactly one canonical month within its profile;
5. material pronunciation or orthographic approximations are explicit;
6. `reviewed` requires directly applicable external standards/orthographic evidence or competent independent review;
7. `stable` requires a later explicit release decision; research evidence alone does not make a profile stable.

## `ka-Geor` — Georgian Mkhedruli

Proposed maturity: **reviewed**.

Mapping: `MA მა`, `MI მი`, `MU მუ`, `NA ნა`, `NI ნი`, `NU ნუ`, `SA სა`, `SU სუ`, `TA ტა`, `YA ია`, `KA კა`, `ZU ზუ`.

The State Language Department of Georgia publishes transcription/transliteration guidance and an English-to-Georgian converter; its published material supports the relevant CV spellings, including `ya [ja] → ია`. ISO 9984:2026 supplies an independent current Georgian/Latin transliteration standard.

Evidence:
- <https://enadep.gov.ge/converter>
- <https://enadep.gov.ge/uploads/fileuploads/Transliteration_ENG_to_KA.pdf>
- <https://www.iso.org/standard/87131.html>

No native-speaker usability study is claimed.

## `hy-Armn` — Eastern Armenian

Proposed maturity: **reviewed**.

Mapping: `MA մա`, `MI մի`, `MU մու`, `NA նա`, `NI նի`, `NU նու`, `SA սա`, `SU սու`, `TA տա`, `YA յա`, `KA կա`, `ZU զու`.

The Library of Congress Armenian romanization table supports the relevant Eastern Armenian letter values, and ISO 9985:2026 provides a current independent Armenian/Latin transliteration standard. Western Armenian consonant realizations are explicitly outside this profile.

Evidence:
- <https://www.iso.org/standard/87132.html>
- <https://www.loc.gov/catdir/cpso/romanization/romguide/Armenian-Transliteration-Table-Revised.pdf>

No native-speaker usability study is claimed.

## `ar-Arab` — fully vocalized Arabic

Proposed maturity: **reviewed**.

Mapping: `MA مَ`, `MI مِ`, `MU مُ`, `NA نَ`, `NI نِ`, `NU نُ`, `SA سَ`, `SU سُ`, `TA تَ`, `YA يَ`, `KA كَ`, `ZU زُ`.

The profile is intentionally fully vocalized. Arabic fatḥa, kasra and ḍamma explicitly encode short `/a/`, `/i/` and `/u/`; omitting harakat would collapse information Tredecadia needs to preserve mechanically. The result is more vocalized than ordinary adult prose by design.

Evidence:
- <https://doi.org/10.1163/15700585-12341640>
- Unicode Arabic-script discussion: <https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/>

No native-speaker usability study is claimed.

## `hi-Deva` — Hindi-oriented Devanagari

Proposed maturity: **reviewed**.

Mapping: `MA मा`, `MI मि`, `MU मु`, `NA ना`, `NI नि`, `NU नु`, `SA सा`, `SU सु`, `TA ता`, `YA या`, `KA का`, `ZU ज़ु`.

The Government of India's Commission for Scientific and Technical Terminology states that international terms rendered in Devanagari should aim at maximum approximation to standard pronunciation using the existing script. Material vowel quantity/quality approximations are explicit, and `ज़` uses nukta to preserve `/z/` rather than collapsing it into native `ज`.

Evidence:
- <https://cstt.education.gov.in/principles-evolving-terminology>
- <https://chd.education.gov.in/en/devanagari-lipi-tatha-hindi-vartani-manakikaran>

No native-speaker usability study is claimed.

## `bn-Beng` — Bengali

Proposed maturity: **reviewed**.

Reviewed mapping: `MA মা`, `MI মি`, `MU মু`, `NA না`, `NI নি`, `NU নু`, `SA সা`, `SU সু`, `TA তা`, `YA ইয়া`, `KA কা`, `ZU জু`.

The original candidate used `জ়ু` to preserve source `/z/` graphically. Further review found that this was over-engineered for standard Bengali orthography. The Government of Bangladesh Accessible Dictionary writes foreign initial `y-` with `ইয়া-/ইয়া-` in entries such as *yaba*, and adapts foreign `z` with ordinary `জ` in forms such as *zebra* → `জেব্রা` and *zone* → `জোন`. The reviewed Tredecadia profile therefore uses `YA=ইয়া` and `ZU=জু`.

This intentionally accepts a Bengali-specific phonetic approximation: ordinary `জ` may be realized closer to `/dʒ/` than canonical `/z/`. That is preferable to inventing an uncommon spelling solely for mechanical phonetic fidelity. Identity remains the Latin canonical syllable `ZU`.

Evidence:
- Government of Bangladesh Accessible Dictionary, Y entries: <https://accessibledictionary.gov.bd/english-to-bengali/?alp=Y>
- Government of Bangladesh Accessible Dictionary, Z entries: <https://accessibledictionary.gov.bd/english-to-bengali/?alp=Z>
- Library of Congress Bengali Romanization Table: <https://www.loc.gov/catdir/cpso/romanization/bengali.pdf>

No native-speaker usability study is claimed.

## `fa-Arab` — Iranian Persian

Proposed maturity: **reviewed**.

Reviewed mapping: `MA مَ`, `MI می`, `MU مو`, `NA نَ`, `NI نی`, `NU نو`, `SA سَ`, `SU سو`, `TA تَ`, `YA یَ`, `KA کَ`, `ZU زو`.

The initial candidate correctly recognized that modern Iranian Persian does not share Arabic's short-vowel values, but it still used kasra for canonical `I` in `MI/NI`. That was internally inconsistent: in modern Persian the short-vowel system is conventionally `a/e/o`, while `/i,u/` correspond to the regular Persian long-vowel spellings with `ی/و`.

The reviewed profile therefore uses `ی` for canonical `/i/` and `و` for canonical `/u/`. This produces the predictable Persian long-vowel realizations `/iː,uː/`, explicitly documented as a length approximation. `A` remains an explicit short-vowel display with fatḥa; `YA` is `یَ`. The spelling is deliberately more explicit than ordinary unvocalized Persian prose because the registry alias must remain deterministic.

Evidence:
- Library of Congress Persian Romanization Table: <https://www.loc.gov/catdir/cpso/romanization/persian.pdf>
- Unicode Arabic-script chapter, including Persian `/e/~/i/` and `/o/~/u/` distinctions: <https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/>
- Unicode CLDR Persian style guide, referencing Persian Academy orthography and Iranian character standards: <https://cldr.unicode.org/translation/language-specific/persian>

No native-speaker usability study is claimed.

## Current decision

All six additional-script month profiles now satisfy the project's `reviewed` evidence gate for future `v1.1.0` promotion:

- `ka-Geor`
- `hy-Armn`
- `ar-Arab`
- `hi-Deva`
- `bn-Beng`
- `fa-Arab`

None is `stable` merely because this research is merged. `stable` maturity requires explicit normative promotion and the normal `v1.1.0` release-validation process.
