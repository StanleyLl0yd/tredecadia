# Contributing

Tredecadia is currently in pre-1.0 specification work.

Contributions are welcome, especially for:

- specification consistency and ambiguity review;
- calendar arithmetic and test vectors;
- localization and pronunciation review by native speakers;
- accessibility and implementation feedback;
- independent checks of the month-name design constraints.

## Before proposing a change

Please distinguish between:

- **normative** changes, which alter required behavior or canonical data;
- **editorial** changes, which improve clarity without changing meaning;
- **rationale/research** changes, which document why a design choice was made.

Canonical month names, their order, syllable structure, and abbreviations should not be changed casually. A proposal to change them should identify a concrete interoperability, safety, or substantial international-language problem and include evidence.

Calendar-conversion changes are also cross-cutting: a change to the epoch, leap rule, intercalary representation, or civil anchor must update the corresponding specification, conversion vectors, executable validation, rationale, and public summary in the same pull request.

## Pull requests

Keep pull requests focused. When changing machine-readable registry data, update the corresponding specification and test vectors in the same pull request. When changing duplicated canonical tables in documentation, keep them synchronized with `registry/months.json`; CI checks this automatically.

Until `v1.0.0`, incompatible draft changes are possible. After `v1.0.0`, compatibility rules will be stricter.
