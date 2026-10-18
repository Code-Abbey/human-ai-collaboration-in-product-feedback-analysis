# Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement

**Bachelor's thesis**

**Abiodun Michael Adefusi**

## About the project

My thesis follows a design-and-evaluation approach: I will build a small AI/NLP tool with a dashboard and compare three ways of analysing app reviews:

1. A person analyses the reviews without AI.
2. AI analyses the reviews, and its results are used without human editing.
3. A person checks and edits the AI-generated results.

Each approach will produce a report with the same sections: main topics, short summaries, references to the supporting reviews, and suggested app improvements. A topic is a group of reviews about a similar issue, such as login problems. I will compare clarity, usefulness, actionability and relevance to the original reviews. Completeness and overall quality will also be assessed. I plan to involve approximately 3–6 expert evaluators. Participants' perceived workload and time spent will be recorded where feasible.

## Main research question

How does a Human-in-the-Loop AI workflow compare with manual analysis and AI-only analysis in producing clear, useful, and actionable product feedback insights from app reviews?

The [research questions and objectives](docs/research-questions.md) contain the full wording submitted to my supervisor.

## Dataset

My proposed choice is **Kahoot!**, using reviews from the GenAI-EdSent dataset. Spotify and Zoom are alternatives.

| App | Reviews downloaded | Reviews passing the first checks |
|---|---:|---:|
| Kahoot! | 34,147 | 15,143 |
| Spotify | 1,000 | 1,000 |
| Zoom | 1,000 | 997 |

The initial checks exclude reviews with no text, reviews with fewer than five words, repeated text, and reviews flagged as possibly containing contact details. The remaining reviews still need to be checked manually for relevance and personal information.

The dataset does not need ready-made topics or summaries. Creating and evaluating those results is part of the thesis. I plan to use one app and approximately 100–300 reviews, with the final number agreed with my supervisor after a small trial.

## Progress

The candidate datasets have been downloaded and checked for basic data quality. The main analysis and comparison have not yet been carried out.

The original downloaded review files are stored locally and are not uploaded to this public repository. This repository contains the findings, source links and scripts needed to download the same files.

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
