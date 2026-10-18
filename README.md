# Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement

**Bachelor's thesis**
**Abiodun Michael Adefusi**

## About the project

This thesis will develop and evaluate a small AI tool with a dashboard. It will compare three ways of analysing app reviews:

1. A person analyses the reviews without AI.
2. AI analyses the reviews, and its results are used without human editing.
3. A person checks and edits the AI-generated results.

Each approach will produce a report with the same sections: main themes, short summaries, references to the supporting reviews, and suggested app improvements. A theme is a common issue identified across reviews, such as login problems.

Approximately 3–6 expert evaluators will assess clarity, usefulness, actionability, relevance to the original reviews, completeness and overall quality. Participants' perceived workload and time spent will be recorded where feasible.

## Main research question

How does a Human-in-the-Loop AI workflow compare with manual analysis and AI-only analysis in producing clear, useful, and actionable product feedback insights from app reviews?

The [research questions and objectives](docs/research-questions.md) contain the full wording submitted to the supervisor.

## Dataset

The proposed dataset is **Kahoot! reviews from GenAI-EdSent**. Spotify and Zoom are alternatives.

| App | Reviews in the source snapshot | Potential reviews after preliminary checks |
|---|---:|---:|
| Kahoot! | 34,147 | 15,143 |
| Spotify | 1,000 | 1,000 |
| Zoom | 1,000 | 997 |

These figures come from preliminary checks of source snapshots. They do not represent the final thesis dataset. The checks exclude blank, very short or repeated text and possible contact details; manual checks will still be needed when the dataset is downloaded and prepared for the study.


## Project documents

- [Concept overview](docs/concept.md)
- [Research questions and objectives](docs/research-questions.md)
- [Study plan](docs/study-plan.md)
- [Why the datasets fit the project](docs/decision.md)
- Dataset notes: [Kahoot!](docs/dataset-cards/kahoot.md), [Spotify and Zoom](docs/dataset-cards/top15.md), [RARE](docs/dataset-cards/rare.md)
- [Data-check results](reports/audit-summary.md)
- [References](references/README.md)
- [Six-month project plan](docs/project-plan.md)
- [Progress and next steps](docs/status.md)
- [Download and run instructions](docs/reproduce.md)
- [Data permissions and privacy](docs/rights-and-privacy.md)

Questions and feedback can be added to the [project discussion](https://github.com/Code-Abbey/human-ai-collaboration-in-product-feedback-analysis/issues/1).
