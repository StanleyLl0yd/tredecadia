# Stable archive / DOI handoff plan

Status: **M4 groundwork; no stable deposit exists yet.**

After `v1.0.0` is published and its GitHub assets have been re-downloaded and byte-verified, the immutable stable release should be deposited in a DOI-capable archival repository such as Zenodo.

The archival handoff should preserve, at minimum:

- the exact `v1.0.0` source tag/commit identifier;
- `tredecadia-1.0.0.tar.gz`;
- `SHA256SUMS`;
- release notes;
- `CITATION.cff`;
- licensing information;
- the deterministic `RELEASE-MANIFEST.json` embedded in the archive;
- a record of the GitHub release URL and archive SHA-256.

The deposited archive bytes must match the already-published GitHub stable asset. A DOI must not be inserted into pre-publication metadata speculatively; once the archival service assigns a DOI, citation/public documentation may be updated to record that external identifier without changing the stable calendar identity.

If the archival service generates its own source snapshot in addition to the uploaded deterministic artifact, Tredecadia should cite the uploaded deterministic archive as the checksum-verifiable release artifact.
