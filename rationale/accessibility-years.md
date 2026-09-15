# Signed-Year and Accessibility Rationale

This document is non-normative. Canonical date syntax lives in `specification/date-notation.md`.

## Machine syntax and human presentation are different layers

Tredecadia needs one exact serialization for interchange and parsing, but humans do not need to see or hear every machine-formatting detail.

The canonical machine year therefore keeps its minimum five digits and ASCII punctuation:

- `00000`
- `00001`
- `12025`
- `-00001`

A human-facing interface may instead display the integer coordinate without padding:

- `0 TE`
- `1 TE`
- `12025 TE`
- `−1 TE`

The typographic minus sign `−` (U+2212) may improve visual presentation, but it is not part of canonical machine syntax. Canonical input continues to require ASCII `-`.

## Why leading zeroes are not useful in ordinary prose

Padding is valuable to machines because it gives a stable minimum field width. In prose and UI labels, however, `00001 TE` visually overemphasizes representation rather than the actual year coordinate. Human display therefore normally uses the integer value itself while preserving the `TE` era context when needed.

This does not create an alternate identifier. `1 TE` is a display of canonical year field `00001`; it is not a second accepted machine serialization.

## Negative years

Negative Tredecadia years are ordinary values on the same mathematical axis. They are not BCE dates and should not be relabeled as BCE/CE.

A screen reader or voice interface should expose the sign semantically, for example as “Tredecadia Era year minus one”, rather than relying on the punctuation character to be pronounced correctly.

## Intercalary days

`EQ` and `ED` are compact machine tokens. Human-facing accessible names should expose their meanings:

- `EQ` → Equinox / New Year Day;
- `ED` → Earth Day.

An interface should not require a user to know that the letters E-Q or E-D are special dates.

## Semantic date labels

For accessibility, a date should be representable as semantic components rather than as one punctuation-heavy string.

Examples:

- `12025-07-11` → Tredecadia Era, year 12025, month Muyasanumi, day 11;
- `00000-EQ` → Tredecadia Era, year 0, Equinox / New Year Day;
- `-00001-01-01` → Tredecadia Era, year minus 1, month Masanumika, day 1.

The exact spoken wording may be localized. What matters is that era, signed year, month/day identity, and intercalary-day identity are available as semantics.

## Strict parsing boundary

The reference parser intentionally rejects presentation variants and visually confusable machine input, including:

- a leading plus sign;
- negative zero;
- redundant year padding;
- Unicode minus in place of ASCII `-`;
- non-ASCII decimal digits;
- surrounding whitespace;
- alternate separators;
- lower-case `eq` / `ed`.

Applications may offer a separate forgiving input layer, but they should normalize and confirm the result before storing or transmitting canonical Tredecadia data.
