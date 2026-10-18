# Proposed study: does human refinement improve product-feedback analysis?

This is a proposal for Moh's review. The earlier conversation mentions three conditions, but its full approved definitions were not available. The following operational definitions must be reconciled with the approved concept before preregistration.

## Question and conditions

For a fixed sample of one app's reviews, does human correction improve the factual support, coverage and usefulness of AI-generated feedback reports, and at what time cost?

| Condition | Process | Outputs retained |
|---|---|---|
| Manual-only | Analyst reads reviews and produces the report without generated suggestions | Categories/themes/report and elapsed time |
| AI-only | Frozen model, prompt, settings and input batches | Unedited model outputs, model version and run settings |
| AI plus human | Starts from the same AI-only output; analyst corrects labels, groups and summaries | Before/after output, every edit, reason and elapsed time |

Use the same evidence and report format in all conditions. Separate analysts and randomise/counterbalance batch allocation to reduce learning effects. If only one analyst is available, use disjoint matched batches and explicitly report the confounding and exploratory scope. An analyst must not independently grade their own edited report.

## Sampling and annotation

Start with 300 candidate reviews, manually screen and replace rejected rows using the same deterministic ordering. A possible study allocation is 50 development reviews and 250 held-out reviews in ten batches of 25. This is a planning example, not a power calculation. Freeze the actual size with Moh after pilot annotation effort is measured.

The supplied sampler gives a reproducible unstratified pilot list, not a final stratified design. Choose either proportional rating sampling for the eligible population or an explicitly balanced diagnostic sample. Record the resulting inclusion probabilities and avoid population claims from a balanced sample. Report changes from exclusions of short, non-English, sensitive or irrelevant text.

Group exact and near duplicates before splitting. Keep related versions in one partition. Define labels using a pilot codebook: bug/failure, feature request, usability, pricing/access, praise and other; allow multiple labels. Two independent annotators should label held-out reviews and adjudicate disagreements. Report agreement before adjudication. Create theme coverage references independently of model output.

## Measures

- **Classification:** macro-F1 and per-label precision/recall against independent labels; report uncertainty and rare-label counts.
- **Summary factual support (primary proposed measure):** proportion of atomic claims supported by cited review evidence; separately count unsupported or contradicted claims.
- **Theme coverage:** proportion of independently identified themes recovered, with a documented matching rule.
- **Usefulness and clarity:** blinded raters score anchored 1–5 rubrics. For usefulness, 1 means no actionable product insight, 3 means some useful but vague findings, 5 means specific evidence-linked insights.
- **Effort:** active minutes, number/type of edits and time per supported insight. Log accepted unchanged output as well as corrections.

Pair AI-only and human-edited results by source batch. Report paired differences with uncertainty resampled at batch level; reviews within a shared summary are not independent summary observations. With ten batches, intervals may be wide: treat this as a limited case study and do not promise statistical power. Rater agreement and disagreements are part of the result.

## Limits and controls

Do not use star ratings as gold labels, model-written references as independent truth, or silver RARE targets as human judgements. Keep the model/prompt fixed between paired conditions, log model nondeterminism and retain failures. Review text is untrusted input: quote it as evidence and tell the model not to follow instructions embedded inside reviews. Do not upload unreviewed personal text to an external model service.

This repository implements data preparation only. No model, annotation study or human-benefit evaluation has been run.
