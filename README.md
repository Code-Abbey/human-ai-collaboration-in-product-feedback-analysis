# Bachelor's thesis: app-review dataset feasibility

Prepared for Abiodun and supervisor Moh · inspected **18 October 2026** · private research repository.

**Recommendation: use Kahoot! from GenAI-EdSent for the primary case study; retain Spotify from Top 15 as a smaller fallback.** RARE is useful for a separate review-refinement experiment, but its supplied training/test split contains overlapping review texts. This repository establishes data feasibility. It does not yet demonstrate that human involvement improves AI results.

## What was actually downloaded and inspected

| Candidate | Verified source rows | Initial eligible pool¹ | Strongest use | Main constraint |
|---|---:|---:|---|---|
| [Kahoot! / GenAI-EdSent](docs/dataset-cards/kahoot.md) | 34,147 | 15,143 | One-app feedback categories, themes and evidence-linked summaries | Many short/repeated texts; no supplied human category or summary labels |
| [Spotify / Top 15](docs/dataset-cards/top15.md) | 1,000 | 1,000 | Compact, complaint-rich alternative | Older snapshot, no review dates, licence wording conflict |
| [Zoom / Top 15](docs/dataset-cards/top15.md) | 1,000 | 997 | Communication/workflow feedback | No dates; 24 missing review-version values |
| [RARE](docs/dataset-cards/rare.md) | 10,000 gold pairs + 10,000 silver pairs | See audit by split | Meaning-preserving review refinement | 130 distinct original texts overlap gold train/test; silver is machine-produced |

¹ Nonblank text, at least five whitespace tokens, first occurrence after Unicode/case/whitespace normalisation, and no email/URL/phone regex flag. **These are candidates, not manually approved English or anonymous records.** Filtering can bias the sample. See [measured audit](reports/audit-summary.md) and [complete schema and quality report](reports/audit.json).

Downloaded: both Kahoot! Parquet shards, the complete 15,000-row Top 15 CSV, and the complete RARE ZIP. The other GenAI-EdSent app files and combined `train` split were **not** downloaded. Its 480,831-review total across 22 apps is publisher metadata, not an independently audited full-corpus count. Do not concatenate its all-app and per-app views as independent observations.

## Read this first

1. [Dataset comparison and decision](docs/decision.md): what each source can support.
2. [Proposed human-in-the-loop evaluation](docs/study-plan.md): measurable outcomes and safeguards against circular evaluation.
3. [Academic references](references/README.md) and [BibTeX](references/references.bib): dataset DOIs, linked papers and methodological foundations.
4. [Rights and privacy](docs/rights-and-privacy.md): source terms, data minimisation and sharing.
5. [Current status and next steps](docs/status.md).

## Reproduce the inspection

Python **3.9.6** was used for the recorded run. The package versions are pinned in `requirements.txt`. A newer interpreter may require compatible package updates; record any such changes.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
# Read docs/rights-and-privacy.md before downloading.
python scripts/download.py --accept-source-terms
python scripts/download.py --verify-only
python scripts/audit.py
python scripts/sample.py --app kahoot --n 300 --seed 20261018
python -m unittest discover -s tests -v
```

All downloads use source URLs in [the manifest](data/manifest.json). Kahoot! is pinned to a Hugging Face commit; Zenodo files are pinned to record versions. SHA-256 mismatches fail rather than silently accepting changed data. Publisher MD5 checksums were also verified for the Zenodo files.

The sampling command writes local JSONL candidates for manual screening. It does **not** label, anonymise, translate or approve them. It strips username, image, source review ID, replies and app metadata columns; text can still contain personal details. Use a text/JSONL editor and avoid opening untrusted review strings as spreadsheet formula cells.

## What is stored here

- `data/manifest.json`: retrieval URLs, versions, file sizes and checksums.
- `scripts/`: download, aggregate audit and deterministic candidate selection.
- `reports/`: measured counts and verification notes; no real review quotations.
- `docs/`: dataset cards, rights notes, decision and proposed study design.
- `references/`: concise source comparisons, DOI bibliography and selected source metadata.

**Raw downloads and real-text candidate files are local-only and ignored by Git**, even though this repository is private. Moh can reproduce the downloads from the original repositories. This avoids republishing user identifiers and keeps the source licences separate from our code. No app-store scraping, paid API call or human evaluation was performed.

## Sharing

This is a private repository. Moh will need an invitation to his GitHub account and must accept it before he can read it. His username has not yet been supplied; no invitation has been sent. See [sharing instructions](docs/sharing.md).
