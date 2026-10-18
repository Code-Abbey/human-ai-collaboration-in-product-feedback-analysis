# Kahoot! from GenAI-EdSent

## Provenance and scope

[Publisher dataset](https://huggingface.co/datasets/Erfan-Nourbakhsh/GenAI-EdSent), Erfan Nourbakhsh; associated preprint by Adeleh Mazaherian and Erfan Nourbakhsh, [DOI 10.48550/arXiv.2512.11934](https://doi.org/10.48550/arXiv.2512.11934). The preprint is a relevant source, not verified peer-reviewed evidence. Author spelling follows arXiv; the dataset prose uses a variant spelling.

Inspected the two `app_Kahoot_Play_Create_Quizzes` Parquet shards at commit `32783444ddc6b56cc95996d77d0923d6eb075164`. Retrieval and checksums are in the manifest. The broader source describes educational-app review analysis; inclusion in this collection does not establish that every Kahoot! review concerns AI functionality.

## Actual files

34,147 rows and 40 columns. Observed review dates run from **16 December 2013 to 12 August 2025**. The audit interprets timestamps as UTC for consistent parsing; source timezone is not established. These dates do not describe the app's current state in October 2026.

| Field group | Actual examples | Proposed treatment |
|---|---|---|
| Review text and rating | `review_content`, `review_score` | Main input; ratings are context, not human sentiment labels |
| Review history | `review_at`, `review_reviewCreatedVersion`, `review_appVersion` | Optional time/version analysis; 9,418 missing version values |
| Engagement | `review_thumbsUpCount` | Optional descriptive variable; not a measure of issue importance |
| Identifiers | `review_reviewId`, `review_userName`, `review_userImage` | Exclude from shared/annotation exports |
| Developer replies | `review_replyContent`, `review_repliedAt` | Exclude from the initial experiment to avoid extra evidence/leakage |
| App metadata | `app_info_json`, descriptions, developer email, app ratings/install counts | Exclude repeated metadata from text modelling |

The complete column list, inferred types and null counts are in [audit.json](../../reports/audit.json). The inspected schema contains **no sentiment label, feedback-category label, or reference summary**, despite the source card's general description of sentiment outputs. App metadata should not be interpreted as historical values for every review date.

## Measured quality

- Five missing text rows; no repeated review IDs.
- 9,905 excess normalised text duplicates. Repeated generic praise is not evidence of fake reviews.
- 18,873 texts have fewer than five whitespace tokens.
- Ratings: 1★ 4,866; 2★ 796; 3★ 1,354; 4★ 2,764; 5★ 24,367. The strong positive imbalance matters for sampling.
- Seven texts match an email/URL/phone screening expression. This is neither a complete personal-data count nor proof that the other rows are anonymous.
- 15,143 mechanically eligible candidates remain. Language, relevance, near-duplicates and privacy still need review.

## Uses and limits

Recommended for a 150–300-review pilot of category correction, theme grouping and evidence-linked summary editing. There is ample capacity to reserve a development set and untouched evaluation batches. A historical window can be selected if the research question concerns a particular product period. The snapshot cannot establish today's issue prevalence, and user-review writers are not a representative user sample.

Declared data licence: **CC BY-NC 4.0**. The MIT badge concerns source code. Data attribution, the licence link and transformation records are retained separately. See [rights and privacy](../rights-and-privacy.md).
