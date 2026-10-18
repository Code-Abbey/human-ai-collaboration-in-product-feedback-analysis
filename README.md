# Human–AI Collaboration in Product Feedback Analysis

**Bachelor's thesis research · Abiodun Michael Adefusi**

Dataset preparation and feasibility assessment · 18 October 2026

My thesis investigates how structured human refinement affects the quality and efficiency of AI-generated product-feedback analysis. I plan to compare three workflows: manual analysis, AI-only analysis, and a human analyst refining AI output. Each workflow will produce a report containing themes, short summaries, references to the supporting reviews, and suggested product improvements.

This repository documents the datasets available for that study, the completed data checks, and the proposed use of the reviews. The analysis and participant evaluation are planned research activities.

## Dataset suitability

The available reviews support the study design. Existing classifications, themes and reference summaries are not prerequisites: generating and evaluating those outputs is part of the research. Final reports will be assessed against their source reviews using the same evaluation criteria across conditions.

| Dataset | Downloaded reviews | Candidates after initial filtering¹ | Role in the thesis |
|---|---:|---:|---|
| [Kahoot! / GenAI-EdSent](docs/dataset-cards/kahoot.md) | 34,147 | 15,143 | Proposed primary case study: one educational app, with sufficient reviews for comparable analysis batches |
| [Spotify / Top 15](docs/dataset-cards/top15.md) | 1,000 | 1,000 | Alternative case study with detailed feedback about app features and user experience |
| [Zoom / Top 15](docs/dataset-cards/top15.md) | 1,000 | 997 | Alternative case study covering communication and meeting workflows |
| [RARE](docs/dataset-cards/rare.md) | 10,000 gold pairs + 10,000 silver pairs | Reported by split | Related work on individual-review refinement; supplementary to the main report-generation study |

¹ Initial filtering retains nonblank reviews with at least five whitespace-separated words, removes repeated normalised texts, and excludes texts flagged by an email/URL/phone pattern. These counts precede manual checks for language, relevance and personal information.

**My proposed choice is Kahoot!**, subject to a content-screening pilot and confirmation of the final app. Spotify is a practical alternative if a smaller corpus with more detailed complaints is preferable. Missing dates in Top 15 limit temporal analysis but do not prevent the planned comparison of report quality.

## Connection to the study

The [dataset-to-method assessment](docs/decision.md) maps the available fields to the three workflows, human intervention stages and report evaluation. The [study plan](docs/study-plan.md) follows the existing thesis protocol: human corrections to classification, theme structure, summaries and proposed actions; independent assessment of evidence support and actionability; and separate recording of human effort.

The [current research status](docs/status.md) distinguishes completed preparation from the remaining experiments. The [academic references](references/README.md) and [BibTeX bibliography](references/references.bib) document dataset provenance and related methods.

## Completed data preparation

Both Kahoot! Parquet files, the complete 15,000-row Top 15 CSV, and the complete RARE archive have been downloaded and inspected. The [audit summary](reports/audit-summary.md) reports measured quality findings, with the complete schemas and statistics in [audit.json](reports/audit.json). The other GenAI-EdSent apps have not been audited.

The checks identify short or repeated reviews, missing fields and potential personal information. RARE also contains 130 distinct review texts shared between its supplied gold training and test files. This affects a potential RARE benchmark; it does not prevent using Kahoot! or Spotify for the proposed thesis study.

## Reproducibility and data handling

The [download manifest](data/manifest.json) records original sources, versions and checksums. Raw reviews and annotation files are excluded from Git. This repository contains preparation scripts, aggregate results and research documentation. Source licences and data handling are documented in [rights and privacy](docs/rights-and-privacy.md).

The recorded environment uses Python 3.9.6 and the package versions in `requirements.txt`.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/download.py --accept-source-terms
python scripts/download.py --verify-only
python scripts/audit.py
python scripts/sample.py --app kahoot --n 300 --seed 20261018
python -m unittest discover -s tests -v
```

The sampling script creates a reproducible local candidate list for screening. Its output does not constitute a final study sample. The [verification report](reports/verification.md) records the checks performed.

## Research discussion

Feedback on the dataset choice, sampling and evaluation design is welcome through the repository's [Issues](https://github.com/Code-Abbey/thesis-app-review-feasibility/issues).
