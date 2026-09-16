# Security Policy

Tredecadia is primarily a public standard, reference implementation, and release-tooling repository. Security-sensitive reports can still matter when they affect release integrity, CI/CD, parsing, reference code, published artifacts, or repository automation.

## Supported versions

Security fixes target the current release-candidate/stable line and the current `main` branch. Historical published tags remain immutable records and are not rewritten.

## Reporting a vulnerability

If GitHub shows **Report a vulnerability** on the repository Security tab, use that private channel and include:

- affected file, workflow, release, or version;
- impact and realistic attack conditions;
- minimal reproduction steps;
- any suggested mitigation, if known.

Do not publish secrets, credentials, private exploit material, or a working attack against release infrastructure in a public issue.

If private vulnerability reporting is not available, open a minimal public issue that states only that a security-sensitive problem exists and which broad area is affected, without exploit details, so a private follow-up channel can be arranged.

## Release integrity

Published tags and release artifacts are treated as immutable. A security fix after publication is made in a new version/release candidate rather than by moving a published tag or replacing a published artifact.
