# Contributing

Tredecadia `1.0.0` is the current stable release. The published `1.1.0-rc.1` prerelease is under M5 observation as a compatible localization-only minor update.

Contributions are welcome, especially for:

- specification consistency and ambiguity review;
- calendar arithmetic and test vectors;
- localization and pronunciation review by native speakers;
- accessibility and implementation feedback;
- independent checks of the month-name and weekday-name design constraints.

## RC feedback

For findings against the published release candidate, use the **Tredecadia RC feedback** issue form. Reports may concern correctness, interoperability, localization, accessibility, packaging, the reference implementation, or documentation.

Please report the concrete observation rather than trying to decide release severity yourself. During the active M5 observation every report is classified against the frozen v1 identity as one of:

- **compatibility-critical defect** — an existing canonical identifier, valid date mapping, or other frozen v1 contract would need an incompatible correction; this requires another RC rather than a silent stable change;
- **compatible correction** — a fix can be made without changing the frozen identity;
- **editorial issue** — wording, translation, navigation, or explanatory material needs improvement without changing behavior;
- **non-blocking future work** — useful work that does not need to delay stable v1.1.0.

The active machine-readable v1.1 observation record is `release/v1.1-rc1-observation.json`; its source is the immutable published `v1.1.0-rc.1`. The earlier RC2 record remains at `release/rc-observation.json` as historical evidence for stable `v1.0.0`.

## Before proposing a change

Please distinguish between:

- **normative** changes, which alter required behavior or canonical data;
- **editorial** changes, which improve clarity without changing meaning;
- **rationale/research** changes, which document why a design choice was made.

Canonical month names, their order, syllable structure, abbreviations, and the canonical weekday identities are frozen in stable v1.0.0. `W1..W7` map in order to `Mene, Noko, Kese, Zoyo, Sote, Yemo, Toze`. Any incompatible change to this identity now requires a new major version or a separately named profile under the compatibility policy.

Localized weekday aliases are **not** implied by existing month-localization profiles. Any proposed localized weekday spelling or pronunciation must be reviewed as a separate localization surface before it is presented as reviewed or stable.

Calendar-conversion changes are also cross-cutting: a change to the epoch, leap rule, intercalary representation, or civil anchor must update the corresponding specification, conversion vectors, executable validation, rationale, and public summary in the same pull request.

## Pull requests

Keep pull requests focused. When changing machine-readable registry data, update the corresponding specification and test vectors in the same pull request. When changing duplicated canonical tables in documentation, keep them synchronized with the corresponding registry; CI checks this automatically.

The compatibility policy in `specification/compatibility.md` defines the v1 boundary. Because stable `v1.0.0` already exists, an incompatible canonical calendar-identity change requires a new major version or separately named profile. If the current v1.1 RC observation finds a compatibility-critical defect in its proposed compatible surface, publish another explicitly versioned v1.1 RC rather than mutating the published prerelease or silently promoting it to stable.
