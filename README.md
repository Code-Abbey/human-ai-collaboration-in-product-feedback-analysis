# Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement

**Bachelor's thesis — Abiodun Michael Adefusi**

## About the project

My thesis explores whether a person can improve AI analysis of app reviews. I will compare three ways of working:

1. A person analyses the reviews without AI.
2. AI analyses the reviews without human changes.
3. A person checks and improves the AI results.

Each approach will produce the same type of report: main topics, short summaries, links to the supporting reviews, and suggested app improvements. I will compare report quality and the time spent on the task.

## Dataset

My proposed choice is **Kahoot!**, using reviews from the GenAI-EdSent dataset. Spotify and Zoom are alternatives.

| App | Reviews downloaded | Reviews passing the first checks |
|---|---:|---:|
| Kahoot! | 34,147 | 15,143 |
| Spotify | 1,000 | 1,000 |
| Zoom | 1,000 | 997 |

The first checks remove blank, very short and repeated reviews, along with texts flagged for possible contact details. The remaining reviews still need a manual check.

The dataset does not need ready-made topics or summaries. Creating and evaluating those results is part of the thesis. I plan to use one app and around 100–225 reviews, with the final size agreed after a small trial.

## Progress

The datasets have been downloaded and checked. The main analysis and comparison have not yet been carried out.

The raw review files are kept locally. This repository contains the findings, source links and scripts needed to download the same files.

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
