# RARE: Repository for App review REfinement

## Provenance and role

[Zenodo version 2, 10.5281/zenodo.13939427](https://doi.org/10.5281/zenodo.13939427), deposited by Amrita Singh, 16 October 2024. Associated EMNLP Industry Track paper by Singh, Jain, Chaudhary and Anish: [10.18653/v1/2024.emnlp-industry.44](https://doi.org/10.18653/v1/2024.emnlp-industry.44).

The paper describes LLM-assisted review refinement checked by software engineers for the gold corpus; silver targets are automatically produced. This supports research on improving individual review wording. It does not supply ground truth for multi-review theme summaries or prove that this thesis's human-in-the-loop workflow will help.

## Actual archive

Downloaded and checksum-verified `RARE_Dataset.zip`. Its usable workbooks are:

| Workbook | Rows | Fields |
|---|---:|---|
| `Gold_Corpus_5k_Training.xlsx` | 5,000 | `App_Name`, `Extracted_Review`, `Gold_Standard` |
| `Gold_Corpus_5k_Testing.xlsx` | 5,000 | Same three fields |
| `Silver_Corpus_10k.xlsx` | 10,000 | `App_Name`, `Extracted_Review`, `Refined_Review` |

The archive also contains an Excel lock file beginning `~$`; the audit explicitly skips it. No source code from the archive is executed. All three fields are read as text. There are no missing inputs or targets, and no timestamp/rating columns.

Each gold split has 500 rows per app: Amazon, Candy Crush Saga, Duolingo, Google Fit, Netflix, Spotify, Twitter, Uber, WhatsApp and YouTube. Silver has 1,000 per app; its WhatsApp label is spelled `WhatsAPP`, versus `WhatsApp` in gold. There is Spotify content, but no Kahoot! or Zoom.

## Leakage and quality findings

After Unicode NFKC, casefold and whitespace normalisation, **130 distinct source-review texts occur in both gold training and gold testing**. Within-split duplicate excess is 126 training rows and 12 testing rows. Silver shares 155 distinct source texts with gold training and eight with gold testing. These are text matches, not estimates of reviewer overlap; near-duplicate overlap is unmeasured.

No gold input/target pairs are identical after this normalisation; two silver pairs are. Changed wording is not evidence of improved factual accuracy. A refinement evaluation would need to assess preservation of intent and unsupported additions.

## Recommended use

RARE would serve as a secondary benchmark if individual-review refinement becomes an explicit research question. Such an experiment would require grouping exact and near-duplicate originals before splitting and reporting the grouping rules and counts. Retaining the published test set would require removing overlapping texts from training and documenting the resulting evaluation limits.

Silver targets provide machine-generated supervision rather than independent human evaluation. Combining RARE with Spotify Top 15 would require cross-source duplication checks, which are outside the current audit.

Declared dataset licence: **CC BY 4.0**. Dataset and paper attribution and transformation records are retained. Raw text remains excluded from Git because licence availability alone does not resolve privacy. [Rights details](../rights-and-privacy.md).
