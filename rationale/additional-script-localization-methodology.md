# Additional-script month localization methodology

Status: **M5 research / v1.1.0 candidate preparation**

This document records the review logic for six proposed month-display profiles that are not part of the published `v1.0.0` localization registry. The executable source of the proposals is `rationale/additional-script-localization-candidates.json`.

## Compatibility boundary

Tredecadia v1 canonical month identity remains the ASCII Latin names and canonical syllable sequences in `registry/months.json`. Display aliases do not redefine those identifiers.

The stable compatibility policy classifies a new localization profile as a compatible **minor** addition. Therefore these proposals target `1.1.0`; they MUST NOT be silently inserted into the already published `1.0.0` registry while still claiming to be the same release.

Weekday aliases are out of scope. The month syllable inventory uses `A/I/U`, while weekday aliases would have to review the independent canonical `E/O` inventory and all seven `W1..W7` identities.

## Common construction rule

Every proposal supplies one deterministic target-script string for each canonical month syllable:

`MA MI MU NA NI NU SA SU TA YA KA ZU`

Full, Short-6 and Short-4 aliases are then derived by concatenating respectively five, three and two mapped syllables. No alias is entered independently of that derivation.

Promotion gates:

1. all 12 mapped syllables are non-empty and distinct;
2. every alias is NFC-normalized and contains no bidi-control or zero-width separator characters;
3. all 13 Full values are unique;
4. all 13 Short-6 values are unique;
5. all 13 Short-4 values are unique;
6. every generated alias reverses to exactly one canonical month within its profile;
7. material pronunciation or orthographic approximations are explicit;
8. `reviewed` requires a directly applicable external standards/orthographic source or competent independent review;
9. `stable` requires a later explicit release decision; research evidence alone does not make a profile stable.

## `ka-Geor` — Georgian Mkhedruli

Proposed maturity: **reviewed**.

Mapping:

| Canonical | Georgian | Canonical | Georgian |
|---|---|---|---|
| MA | მა | NA | ნა |
| MI | მი | NI | ნი |
| MU | მუ | NU | ნუ |
| SA | სა | TA | ტა |
| SU | სუ | YA | ია |
| KA | კა | ZU | ზუ |

The State Language Department of Georgia publishes transcription/transliteration rules and an English-to-Georgian converter. Its published tables directly support the relevant Georgian CV spellings, including `ya [ja] → ია`. ISO 9984:2026 supplies an independent current Georgian/Latin transliteration standard.

Evidence:

- State Language Department: <https://enadep.gov.ge/converter>
- State Language Department English-to-Georgian guidance: <https://enadep.gov.ge/uploads/fileuploads/Transliteration_ENG_to_KA.pdf>
- ISO 9984:2026: <https://www.iso.org/standard/87131.html>

No native-speaker usability study is claimed.

## `hy-Armn` — Eastern Armenian

Proposed maturity: **reviewed**.

Mapping:

| Canonical | Armenian | Canonical | Armenian |
|---|---|---|---|
| MA | մա | NA | նա |
| MI | մի | NI | նի |
| MU | մու | NU | նու |
| SA | սա | TA | տա |
| SU | սու | YA | յա |
| KA | կա | ZU | զու |

The Library of Congress Armenian romanization table explicitly states that its primary phonetic values are Classical/Eastern Armenian and supports `մ=m`, `ն=n`, `ս=s`, `տ=t`, `կ=k`, `զ=z`, `յ=y`, `ու=u`. ISO 9985:2026 provides a current independent Armenian/Latin transliteration standard.

The profile is deliberately Eastern Armenian. Western Armenian consonant realizations are not silently claimed to be identical.

Evidence:

- ISO 9985:2026: <https://www.iso.org/standard/87132.html>
- Library of Congress Armenian Romanization Table: <https://www.loc.gov/catdir/cpso/romanization/romguide/Armenian-Transliteration-Table-Revised.pdf>

No native-speaker usability study is claimed.

## `ar-Arab` — fully vocalized Arabic

Proposed maturity: **reviewed**.

Mapping:

| Canonical | Arabic | Canonical | Arabic |
|---|---|---|---|
| MA | مَ | NA | نَ |
| MI | مِ | NI | نِ |
| MU | مُ | NU | نُ |
| SA | سَ | TA | تَ |
| SU | سُ | YA | يَ |
| KA | كَ | ZU | زُ |

The profile is intentionally **fully vocalized**. Arabic fatḥa, kasra and ḍamma explicitly encode short `/a/`, `/i/` and `/u/`; omitting the harakat would make the proposed display aliases depend on lexical inference and would collapse information that Tredecadia needs to preserve mechanically.

This means the aliases look more vocalized than ordinary adult Arabic prose. That is a deliberate standards-display trade-off, not an accidental formatting choice.

Evidence:

- Modern Standard Arabic short-vowel reference: <https://doi.org/10.1163/15700585-12341640>

No native-speaker usability study is claimed.

## `hi-Deva` — Hindi-oriented Devanagari

Proposed maturity: **reviewed**.

Mapping:

| Canonical | Devanagari | Canonical | Devanagari |
|---|---|---|---|
| MA | मा | NA | ना |
| MI | मि | NI | नि |
| MU | मु | NU | नु |
| SA | सा | TA | ता |
| SU | सु | YA | या |
| KA | का | ZU | ज़ु |

The Government of India's Commission for Scientific and Technical Terminology states that international terms rendered in Devanagari should aim at maximum approximation to the standard pronunciation using the existing script. The Central Hindi Directorate maintains the official Devanagari/Hindi spelling standard.

Material approximations are explicit: Hindi vowel quantity/quality does not reproduce the broad Tredecadia citation vowels perfectly, and `ज़` uses nukta to preserve `/z/` rather than collapsing it into native `ज`.

Evidence:

- CSTT principles: <https://cstt.education.gov.in/principles-evolving-terminology>
- Central Hindi Directorate spelling standard: <https://chd.education.gov.in/en/devanagari-lipi-tatha-hindi-vartani-manakikaran>

No native-speaker usability study is claimed.

## `bn-Beng` — Bengali

Proposed maturity: **candidate**.

Mapping currently under review:

| Canonical | Bengali | Canonical | Bengali |
|---|---|---|---|
| MA | মা | NA | না |
| MI | মি | NI | নি |
| MU | মু | NU | নু |
| SA | সা | TA | তা |
| SU | সু | YA | ইয়া |
| KA | কা | ZU | জ়ু |

Two issues prevent automatic promotion:

1. Bengali orthography does not provide a simple universally neutral word-initial glide spelling equivalent to canonical `/ja/`; the proposal uses `ইয়া`, which is an orthographic adaptation rather than a one-grapheme transcription.
2. `/z/` is non-native/loanword-sensitive. Modern `জ়` can explicitly represent `/z/`, while established Bengali spelling practice often adapts foreign `/z/` differently. The profile therefore needs independent Bengali review before `reviewed` status.

The candidate retains `জ়ু` because it keeps the intended `/z/` distinction explicit and mechanically reversible, but that engineering advantage does not substitute for orthographic review.

## `fa-Arab` — Iranian Persian

Proposed maturity: **candidate**.

Mapping currently under review:

| Canonical | Persian | Canonical | Persian |
|---|---|---|---|
| MA | مَ | NA | نَ |
| MI | مِ | NI | نِ |
| MU | مو | NU | نو |
| SA | سَ | TA | تَ |
| SU | سو | YA | یَ |
| KA | کَ | ZU | زو |

Modern Iranian Persian does **not** share Arabic's short-vowel values. The Arabic-derived marks conventionally correspond to Persian short `a/e/o`, while long Persian vowels provide the closest regular written values for canonical `/i,u/`. The proposal therefore uses `ی/و`-based spellings where necessary and explicitly accepts a length/quality approximation.

This is a real phonological design question, not merely a Unicode choice. The profile remains candidate until an independent Persian-language review confirms the preferred display convention.

References useful for that review:

- Encyclopaedia Iranica style guide: <https://www.iranicaonline.org/style-guide/>
- Association for Iranian Studies transliteration guidance: <https://associationforiranianstudies.org/journal/transliteration>

## Current decision

The current evidence supports proposing `ka-Geor`, `hy-Armn`, `ar-Arab`, and `hi-Deva` at `reviewed` maturity for a future v1.1.0 registry. `bn-Beng` and `fa-Arab` remain candidates.

None of these profiles is `stable` merely because this research file is merged. Stable status requires an explicit v1.1.0 release decision and the normal release-validation process.
