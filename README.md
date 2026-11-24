# RustQEC documentation artifacts

This repository stores historical design documents, generated documentation-site
assets, and benchmark evidence from the main
[`rust-qec`](https://github.com/nzy1997/rust-qec) source repository.

Each evidence bundle records its measured source commit and input inventory;
for atom-loss, see `site/static/data/atom-loss/source-manifest.json`. The source
repository contains the scripts and contracts that regenerate and verify these
files; this repository keeps the published artifacts and historical documents.

## Layout

- `site/static/data/atom-loss/` — published atom-loss evidence bundle.
- `site/static/rsmp-v1-showcase/og.png` — generated social-preview image.
- `docs/test-reports/` — rendered documentation test reports.
- `docs/superpowers/` — archived design specifications and implementation plans,
  copied from [rust-qec at `e383c477`](https://github.com/nzy1997/rust-qec/tree/e383c47727d7e4702562dd5ecfdeaf45a45ea501/docs/superpowers).
- `benchmarks/rstim_vs_stim_simulator/fixtures/*.dem` — pinned large DEM
  fixture used by the release evidence checker.

The main repository fetches a pinned commit from this repository before site
builds and evidence checks. Regenerate the site and evidence artifacts from the
source repository before updating its artifact pin. The historical documents are
preserved as published with the [source license](docs/superpowers/LICENSE).
For links that refer to source files outside the archive,
use the original source snapshot linked above.

Run `python3 tools/check_artifacts.py` to verify every published artifact listed
in `ARTIFACTS.sha256`. GitHub Actions runs the same command for pull requests and
updates to `master`. Source-specific physics and replay checks run in `rust-qec`
against its pinned artifact revision.
