# RARE dataset

**Source:** [RARE on Zenodo, version 2](https://doi.org/10.5281/zenodo.13939427).

## What it contains

RARE contains pairs of original and rewritten app reviews from ten apps, including Spotify.

- **10,000 gold pairs:** rewritten reviews checked by people, split into 5,000 training and 5,000 test examples.
- **10,000 silver pairs:** rewritten reviews produced automatically.

The files contain the app name, original review and rewritten version. They have no review dates or star ratings.

## Main finding

The checks found **130 different original review texts appearing in both the gold training and test files**. A separate experiment using those files would need to handle this overlap before evaluating a model.

## Use in the thesis

RARE is useful background on improving review wording. My main study concerns reports covering several reviews, so it does not need this dataset. RARE is kept as a reference rather than an extra experiment.

**Data licence:** CC BY 4.0, with attribution. The related paper is listed in the [references](../../references/README.md), and the detailed counts are in the [data report](../../reports/audit.json).
