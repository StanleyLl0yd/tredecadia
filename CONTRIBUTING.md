# Contributing

Tredecadia is currently in the `1.0.0-rc.2` release-candidate cycle.

Contributions are welcome, especially for:

- specification consistency and ambiguity review;
- calendar arithmetic and test vectors;
- localization and pronunciation review by native speakers;
- accessibility and implementation feedback;
- independent checks of the month-name and weekday-name design constraints.

## RC feedback

For findings against the published release candidate, use the **Tredecadia RC feedback** issue form. Reports may concern correctness, interoperability, localization, accessibility, packaging, the reference implementation, or documentation.

Please report the concrete observation rather than trying to decide release severity yourself. During M4 every report is classified against the frozen v1 identity as one of:

- **compatibility-critical defect** — an existing canonical identifier, valid date mapping, or other frozen v1 contract would need an incompatible correction; this requires another RC rather than a silent stable change;
- **compatible correction** — a fix can be made without changing the frozen identity;
- **editorial issue** — wording, translation, navigation, or explanatory material needs improvement without changing behavior;
- **non-blocking future work** — useful work that does not need to delay v1.0.0.

The machine-readable observation record is `release/rc-observation.json`. RC2 observation starts only after the actual `v1.0.0-rc.2` publication timestamp is recorded. Stable publication remains blocked while the observation period is open or a release-blocking report remains unresolved.

## Before proposing a change

Please distinguish between:

- **normative** changes, which alter required behavior or canonical data;
- **editorial** changes, which improve clarity without changing meaning;
- **rationale/research** changes, which document why a design choice was made.

Canonical month names, their order, syllable structure, and abbreviations are frozen for v1 RC testing and should not be changed casually. The RC2 weekday identities are also part of the compatibility-critical candidate surface: `W1..W7` map in order to `Mene, Noko, Kese, Zoyo, Sote, Yemo, Toze`. A proposal to change canonical month or weekday identity before final v1 must identify a concrete interoperability, safety, or substantial international-language problem and include evidence.

Localized weekday aliases are **not** implied by existing month-localization profiles. Any proposed localized weekday spelling or pronunciation must be reviewed as a separate localization surface before it is presented as reviewed or stable.

Calendar-conversion changes are also cross-cutting: a change to the epoch, leap rule, intercalary representation, or civil anchor must update the corresponding specification, conversion vectors, executable validation, rationale, and public summary in the same pull request.

## Pull requests

Keep pull requests focused. When changing machine-readable registry data, update the corresponding specification and test vectors in the same pull request. When changing duplicated canonical tables in documentation, keep them synchronized with the corresponding registry; CI checks this automatically.

The compatibility policy in `specification/compatibility.md` defines the intended v1 boundary. Incompatible corrections remain possible before final `v1.0.0` only when RC testing uncovers a genuine correctness or interoperability defect. After `v1.0.0`, incompatible calendar-identity changes require a new major version or separately named profile.
