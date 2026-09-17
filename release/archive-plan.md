# Stable archive / DOI handoff plan

Status: **GitHub `v1.0.0` published and verified; external DOI deposit remains pending.**

The stable GitHub release was published from exact source commit `8c272bf6a48b1b84a4b2ca8c1db43c6ffb9f5ce3` on `2026-09-17T12:53:29Z`. The publication workflow re-downloaded and verified the published assets. The deterministic archive is:

- asset: `tredecadia-1.0.0.tar.gz`
- SHA-256: `2f14cc4fb2bcac2cfcce280ddbe948d4c65cab098ce23c1d385d220709f5c392`
- GitHub release: <https://github.com/StanleyLl0yd/tredecadia/releases/tag/v1.0.0>

The remaining archival handoff is to deposit those already-published stable bytes in a DOI-capable archival repository such as Zenodo.

The archival handoff should preserve, at minimum:

- the exact `v1.0.0` source tag/commit identifier;
- `tredecadia-1.0.0.tar.gz`;
- `SHA256SUMS`;
- release notes;
- `CITATION.cff`;
- licensing information;
- the deterministic `RELEASE-MANIFEST.json` embedded in the archive;
- the GitHub release URL and archive SHA-256 above.

The deposited archive bytes must match the already-published GitHub stable asset. A DOI must not be inserted speculatively; once the archival service assigns one, citation/public documentation may record that external identifier without changing stable calendar identity.

If the archival service generates its own source snapshot in addition to the uploaded deterministic artifact, Tredecadia should cite the uploaded deterministic archive as the checksum-verifiable release artifact.
