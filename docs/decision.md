# Dataset suitability for the thesis design

## Research objective

My research question concerns whether structured human refinement improves the quality and efficiency of product-feedback reports compared with manual and AI-only analysis. The dataset therefore needs to provide sufficient relevant written reviews of one app. Ready-made theme labels, sentiment annotations or summaries are not required inputs.

This assessment uses the [existing study protocol](https://github.com/Code-Abbey/Bachelors-Thesis/blob/f417c24499c84b6993a7b30f318f7d142c83cdc3/human_ai_product_feedback/research/study_protocol.md) and [evaluation rubric](https://github.com/Code-Abbey/Bachelors-Thesis/blob/f417c24499c84b6993a7b30f318f7d142c83cdc3/human_ai_product_feedback/research/evaluation_rubric.md) as the methodological basis. These sources are held in the private thesis workspace; the relevant design is restated in the [study plan](study-plan.md).

## Dataset-to-method assessment

| Component of the study | Required material | Available evidence | Assessment |
|---|---|---|---|
| One app as a case study | Identifiable app and written reviews | Kahoot! has its own files; Top 15 identifies Spotify and Zoom by app name | Supported |
| Comparable batches of 50–75 reviews | Sufficient distinct, relevant texts and a fixed batch allocation | Initial pools: Kahoot! 15,143; Spotify 1,000; Zoom 997 | Volume is sufficient; manual relevance screening and batch matching remain |
| Manual workflow | Reviews and a common blank report template | Review text is present in all candidates | Supported |
| AI-only workflow | Same review evidence, fixed prompts/model and report structure | Reviews can be exported to a common input format | Supported after implementation |
| H1: correction of classification | AI-assigned labels attached to reviews | Labels will be generated during the study | Existing labels are not required |
| H2: theme restructuring | Review-to-theme assignments that can be merged, split or moved | Theme assignments will be generated from the review text | Existing themes are not required |
| H3: summary/action revision | Generated summaries and proposed improvements linked to evidence | Source text is available for checking those claims | Existing summaries are not required |
| Traceable evidence | Stable internal identifiers for included reviews | IDs can be assigned during preparation; the local sampler already generates deterministic candidate IDs | Supported; the final ID-to-review mapping will be retained with restricted study data |
| Expert assessment | Final reports, source reviews and a common rubric | The existing rubric covers evidence support, actionability, clarity, usefulness and coverage | Supported through the planned evaluation |
| Human effort comparison | Time and interaction records | These are collected in the study, not expected in an app-review dataset | Supported after logging is implemented |

## Proposed dataset choice

**Kahoot! is my proposed primary case study.** It offers sufficient volume for the protocol's two or three comparable batches and a separate development sample. Its review dates permit a deliberate historical window if needed. The main preparation task is identifying substantive feedback among short or generic comments.

**Spotify is a suitable alternative.** The 1,000 available reviews provide a manageable pool, and the limited initial content check identified feedback about downloads, playback, advertising and interface features. These observations are illustrative; they are not coded frequency estimates. Review dates are unnecessary for the main report-quality comparison, although their absence rules out reliable temporal analysis.

**Zoom is also feasible** if communication workflows are the preferred case-study context. Its initial sample includes authentication, meeting-sync and audio/video concerns. All three options require language, relevance and privacy screening before final selection.

**RARE is supplementary.** It supplies original/refined text pairs for a different task: improving individual-review wording. Its supplied labels and pairs are useful related work, but the main thesis does not depend on them. The split overlap matters only if RARE is used in a separate training/evaluation benchmark.

## Conclusion of the feasibility check

The downloaded Kahoot!, Spotify and Zoom data contain the inputs needed for the planned analysis. The absence of ready-made analytical outputs is compatible with the thesis. The contribution will be the implemented analysis workflow and the evaluation of human refinement.

The next research stage is a 30–50-review screening pilot, followed by selection of one app and fixed comparable batches. Dataset suitability does not itself establish that human refinement improves results; that question will be addressed by the experiment.
