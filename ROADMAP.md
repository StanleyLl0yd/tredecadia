# Roadmap

Tredecadia is intentionally pre-1.0 until the remaining calendar-semantics gaps are resolved and the complete repository passes a final consistency review.

## M0 — Repository bootstrap

Status: **complete**

- publish draft specifications;
- publish canonical month registry and schema;
- encode naming/cycle invariants as executable checks;
- establish licensing, citation, contribution, and changelog metadata.

## M1 — Close normative calendar gaps

- choose and specify the leap-year determination rule;
- define the epoch and year-number semantics;
- define normative Gregorian/ISO-calendar conversion behavior;
- finalize representation of intercalary days;
- add conversion test vectors, including boundary and leap cases.

## M2 — Internationalization and implementation review

- review canonical pronunciation wording;
- add independently reviewed localization profiles;
- test compact month forms in realistic interfaces;
- publish a small reference implementation after the normative conversion rules are stable.

## M3 — v1.0 release candidate

- repository-wide specification/registry/test consistency audit;
- freeze compatibility-critical identifiers;
- finalize public documentation and GitHub Pages site;
- run release-candidate review before tagging.

## M4 — v1.0 publication

- tag `v1.0.0`;
- publish the immutable release artifacts;
- archive the release with a DOI-capable repository such as Zenodo;
- publish the citation metadata for the stable version.
