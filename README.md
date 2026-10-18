# Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement

**Bachelor's thesis — Abiodun Michael Adefusi**

## About the project

My thesis explores whether human checking can improve AI-generated analysis of app reviews. I will compare three ways of working:

1. A person analyses the reviews without AI.
2. AI analyses the reviews, and its results are used without human editing.
3. A person checks and edits the AI-generated results.

Each approach will produce a report with the same sections: main topics, short summaries, references to the supporting reviews, and suggested app improvements. A topic is a group of reviews about a similar issue, such as login problems. I will compare report quality and the time spent on the task.

## Dataset

My proposed choice is **Kahoot!**, using reviews from the GenAI-EdSent dataset. Spotify and Zoom are alternatives.

| App | Reviews downloaded | Reviews passing the first checks |
|---|---:|---:|
| Kahoot! | 34,147 | 15,143 |
| Spotify | 1,000 | 1,000 |
| Zoom | 1,000 | 997 |

The initial checks exclude reviews with no text, reviews with fewer than five words, repeated text, and reviews flagged as possibly containing contact details. The remaining reviews still need to be checked manually for relevance and personal information.

The dataset does not need ready-made topics or summaries. Creating and evaluating those results is part of the thesis. I plan to use one app and around 100–225 reviews, with the final number agreed with my supervisor after a small trial.

## Progress

The candidate datasets have been downloaded and checked for basic data quality. The main analysis and comparison have not yet been carried out.

The original downloaded review files are stored locally and are not uploaded to this public repository. This repository contains the findings, source links and scripts needed to download the same files.

## Project documents

- [Study plan](docs/study-plan.md)
- [Why the datasets fit the project](docs/decision.md)
- Dataset notes: [Kahoot!](docs/dataset-cards/kahoot.md), [Spotify and Zoom](docs/dataset-cards/top15.md), [RARE](docs/dataset-cards/rare.md)
- [Data-check results](reports/audit-summary.md)
- [References](references/README.md)
- [Progress and next steps](docs/status.md)
- [Download and run instructions](docs/reproduce.md)
- [Data permissions and privacy](docs/rights-and-privacy.md)

Questions and feedback can be added to the [project discussion](https://github.com/Code-Abbey/human-ai-collaboration-in-product-feedback-analysis/issues/1).
