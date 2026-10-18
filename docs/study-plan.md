# Study plan: human refinement of product-feedback reports

## Research question

How does structured human-in-the-loop refinement affect the quality and efficiency of product-feedback insights compared with manual and AI-only analysis of app reviews?

The study follows the three-workflow design in the existing thesis protocol. Each condition produces the same four-part report: top themes, short theme summaries, references to supporting source reviews, and proposed product improvement actions. The selected dataset supplies the reviews; producing and evaluating the analytical outputs is part of the thesis.

## Study conditions

| Condition | Procedure | Material retained |
|---|---|---|
| A: Manual | Analyst receives reviews and a blank report template, then produces the report without AI assistance | Final report and active analysis time |
| B: AI-only | A fixed pipeline processes the reviews using recorded prompts, model settings and report format | Unedited output, configuration and system latency |
| C: Human-in-the-loop | Analyst revises the AI output through the three intervention stages | Initial/final outputs, edits, reasons and active analysis time |

The human intervention stages are:

- **H1 — Classification:** correct review labels, including multiple labels for mixed feedback.
- **H2 — Themes:** rename, merge, split or reorganise themes and move or remove review assignments.
- **H3 — Summaries and actions:** improve specificity, correct unsupported claims and revise proposed improvements against source evidence.

Corrections affect the current analysis session. Persistent feedback learning and model retraining are outside the proposed scope.

## Materials and sampling

The working protocol proposes two or three comparable batches of 50–75 reviews from one app, giving 100–225 study reviews. A separate development sample will support prompt and interface development. Final batch size will follow the content-screening and timing pilots.

Kahoot! is the proposed case study, with Spotify and Zoom as alternatives. The screening process will check language, relevant product feedback, repeated or near-duplicate content and personal information. Batch matching will consider review length, issue variety and the distribution of ratings. Batch membership will be fixed before evaluation.

Existing sentiment labels and reference summaries are unnecessary. Ratings provide sampling context rather than ground truth for feedback categories. Stable internal IDs will connect each included review to its themes, summaries and proposed actions.

The repository's 300-review candidate exports support preparation. They are not the final experimental batches or an approved sample.

## Participants and procedure

The working target is four to six analysts producing manual and human-refined reports, with some replication across review batches. Three to six independent experts will evaluate the completed reports. These recruitment targets remain subject to feasibility and supervisory discussion.

Where an analyst completes both manual and human-refined tasks, different matched batches and a counterbalanced order will reduce memory and order effects. Instructions, training and time limits will be standardised after a pilot. The AI-only output will be retained for each batch with its model and prompt configuration.

Reports will receive neutral identifiers, and condition-specific traces will be removed before expert assessment. Evaluators will have access to the relevant source reviews. Analysts will not independently evaluate their own reports.

## Evaluation

The primary proposed outcomes remain **evidence support** and **actionability**, rated on anchored 1–5 scales. Clarity, usefulness and coverage are secondary outcomes.

| Criterion | 1: Poor | 3: Adequate | 5: Excellent |
|---|---|---|---|
| Evidence support | Multiple unsupported or contradicted claims | Mostly grounded, with some unsupported claims | Claims and suggestions consistently supported by source-review references |
| Actionability | Vague or impractical actions | Some feasible but underspecified steps | Concrete, feasible actions connected to review evidence |
| Clarity | Difficult to understand or organise | Mostly understandable, with some ambiguity | Clear, coherent and concise |
| Usefulness | Few insights relevant to product decisions | Some relevant concerns identified | Important product concerns are clearly prioritised |
| Coverage | Many prominent issues omitted | Most key issues included | Main issues covered with little significant omission |

Experts will record short reasons, supporting review IDs, unsupported claims and omitted themes. Human effort will be measured using active analysis/editing time and the number and type of interventions. System latency will be recorded separately.

Classification accuracy may be an additional technical measure if an independently annotated reference set is created. It is not a prerequisite for the main expert evaluation of final reports.

## Analysis and limitations

The analysis will compare condition-level scores and variation between reports, examine evaluator agreement, and describe the types of human corrections. Multiple ratings of one report will not be treated as independent replications of the workflow. The planned sample supports an exploratory case study; broader superiority claims will require stronger evidence.

The dataset is a historical, selected collection of user reviews. The study evaluates the analysis workflow on that collection rather than estimating current app satisfaction. The completed data audit establishes the available inputs; report generation and human evaluation remain to be conducted.
