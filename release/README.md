# Release publication gate

Tredecadia releases are published explicitly through `release/publish.json`.

A change to that file on `main` triggers `.github/workflows/publish-release.yml`. The workflow validates the metadata, repeats the complete release conformance gates, builds the deterministic release archive and checksum, refuses to overwrite an existing tag or release, tags the exact checked commit, publishes the GitHub release, downloads its assets again, and byte-compares them with the locally built artifacts.

`release/publish.json` therefore acts as a deliberate publication trigger and MUST NOT be edited as ordinary metadata. Its version must match `CITATION.cff`, all published registry/vector `specVersion` values, the changelog release heading, and the release-notes filename.

For a prerelease, `prerelease` must be `true`. Final stable release publication must use `false` and should occur only after the stable-status transition required by the compatibility/localization policy.
