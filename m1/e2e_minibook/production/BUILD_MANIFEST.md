# FEHLALARM v0.2 – Build Manifest

status: G5_APPROVED
date: 2026-08-30

## Source

- G4-manuscript: `m1/e2e_minibook/MANUSCRIPT_v02.md`
- source blob: `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
- G4 record: `m1/e2e_minibook/gates/G4.md` — blob `8c4181e878c0f64d233c2bdaeaf73a218a1ab5ac`

## Builder

- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`
- dependency-free Python standard library only

Command:

```text
python scripts/build_html.py \
  m1/e2e_minibook/MANUSCRIPT_v02.md \
  m1/e2e_minibook/production/FEHLALARM_v02.html
```

## Output

- `m1/e2e_minibook/production/FEHLALARM_v02.html`
- output blob: `1add4d45fea3e552521041ae5d6120fba717d214`
- type: standalone HTML reading/print artifact
- G5: **APPROVE**
- G5 record: `m1/e2e_minibook/gates/G5.md` — blob `96e2033e60575794645485924fe6045147a5a458`

Production features:

- semantic title and scene headings,
- responsive reading layout,
- book-oriented typography,
- A5 print CSS,
- print page breaks,
- safe HTML escaping,
- no external runtime or CDN dependency.

## Fidelity / Reproducibility QA

Regression test:

- `tests/test_build_html.py`
- test blob: `7d0bf4d7d592b4cad42fec29953c6fef93b205e8`

The test rebuilds the HTML from `MANUSCRIPT_v02.md` and requires **byte-for-byte equality** with the committed production artifact.

The first run exposed a real production drift: the HTML contained an older S3 intermediate version. This was not hidden or accepted. The HTML was rebuilt from the already approved G4 manuscript without modifying that manuscript.

Final verification:

- GitHub Actions workflow: `Framework Validation`
- Run #32 / ID `33306864034`
- head commit: `55e128aaba91744ebe277134d04b6a7b978769c8`
- result: **success**

The successful run includes:

- byte-exact HTML rebuild test,
- provenance invalidation tests,
- pipeline checker tests,
- scene readiness tests,
- prose audit tests,
- full NORMALFALL noise audit workflow.

## Validity

This manifest approves exactly output blob `1add4d45fea3e552521041ae5d6120fba717d214` against the fixed G4 source blob. A later content change requires G4 backtracking and rebuild. A production-only change creates a new output blob and requires a new G5 decision.
