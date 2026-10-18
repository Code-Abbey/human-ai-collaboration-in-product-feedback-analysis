# Dataset decision for discussion with Moh

## Proposed choice

Select **Kahoot!** provisionally. The verified 15,143 mechanical candidates give room for a 150–300-review study, a separate development set and sensitivity checks. Its dates allow an explicit historical window. The cost is manual screening and creation of task-specific reference labels.

Select **Spotify / Top 15** if a smaller, simpler corpus is preferable. All 1,000 rows pass the initial text filters, but no date-based analysis is possible. Its low-rating-heavy distribution is useful for complaint analysis and unsuitable for claiming typical user satisfaction. Zoom is a viable third option if its workflow is more familiar to the researcher.

Use **RARE** as supporting literature and an optional refinement benchmark. Its paired targets are academically valuable, but review rewriting differs from identifying themes or producing product-feedback reports. The measured split overlap must be handled before any benchmark claim.

## What is feasible now?

| Work | Feasible with these files? | Additional work |
|---|---|---|
| Explore ratings, lengths, missingness and exact duplicates | Yes; initial audit completed | Choose final filtering policy |
| Classify bugs, requests, usability, pricing and praise | Yes, as a new experiment | Define multi-label codebook; independent human labels |
| Group themes and produce evidence-linked reports | Yes | Human theme inventory and blinded quality rubric |
| Measure human correction benefit | Not from dataset alone | Controlled comparison, edit logs and independent evaluators |
| Evaluate meaning-preserving rewriting | RARE provides pairs | Fix overlap; inspect target fidelity |
| Measure current product problems in 2026 | No | A new, authorised and dated source would be needed |
| Infer representative satisfaction or causal product impact | No | These observational selected reviews do not support it |

## Decision gates

1. Moh agrees the primary app and whether the outcome is categories, themes, summaries or a combination.
2. Review 30–50 candidates for relevant content, language and privacy; revise the codebook and eligibility rules.
3. Freeze the corpus version, sampling design and reference-building process before model comparison.
4. Confirm university research-data handling and the permitted model environment.

The corpus audit is complete for the downloaded files. Academic feasibility remains conditional on the evaluation design and annotation effort. No new claim about the earlier synthetic experiment is made here.
