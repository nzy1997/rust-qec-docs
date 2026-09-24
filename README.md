# RustQEC documentation artifacts

This repository stores generated documentation-site assets and benchmark
evidence that are too large or too frequently regenerated for the main
[`rust-qec`](https://github.com/nzy1997/rust-qec) source repository.

Each evidence bundle records its measured source commit and input inventory;
for atom-loss, see `site/static/data/atom-loss/source-manifest.json`. The source
repository contains the scripts and contracts that regenerate and verify these
files; this repository contains only the published artifacts.

## Layout

- `site/static/data/atom-loss/` — published atom-loss evidence bundle.
- `site/static/rsmp-v1-showcase/og.png` — generated social-preview image.
- `docs/test-reports/` — rendered documentation test reports.
- `benchmarks/rstim_vs_stim_simulator/fixtures/*.dem` — pinned large DEM
  fixture used by the release evidence checker.

The main repository fetches a pinned commit from this repository before site
builds and evidence checks. Do not edit these files by hand; regenerate them
from the source repository and update the pinned revision there.
