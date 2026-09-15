# Contributing

Tredecadia is currently in the `1.0.0-rc.1` release-candidate cycle.

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

Canonical month names, their order, syllable structure, and abbreviations are frozen for v1 RC testing and should not be changed casually. A proposal to change them before final v1 must identify a concrete interoperability, safety, or substantial international-language problem and include evidence.

Calendar-conversion changes are also cross-cutting: a change to the epoch, leap rule, intercalary representation, or civil anchor must update the corresponding specification, conversion vectors, executable validation, rationale, and public summary in the same pull request.

## Pull requests

Keep pull requests focused. When changing machine-readable registry data, update the corresponding specification and test vectors in the same pull request. When changing duplicated canonical tables in documentation, keep them synchronized with `registry/months.json`; CI checks this automatically.

The compatibility policy in `specification/compatibility.md` defines the intended v1 boundary. Incompatible corrections remain possible before final `v1.0.0` only when RC testing uncovers a genuine correctness or interoperability defect. After `v1.0.0`, incompatible calendar-identity changes require a new major version or separately named profile.
