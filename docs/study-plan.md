# Study plan

## Research question

How does a Human-in-the-Loop AI workflow compare with manual analysis and AI-only analysis in producing clear, useful, and actionable product feedback insights from app reviews?

The full [research questions and objectives](research-questions.md) guide this study. Human-in-the-Loop (HITL) means that a person can check and change the AI-generated results.

## Dataset and study size

I propose using Kahoot! reviews. Spotify and Zoom are alternatives. I will choose one app and prepare two or three similar groups of 50–75 reviews, giving around 100–225 reviews in total. A small trial will help determine the final number of reviews.

I will remove repeated reviews, check that the text is relevant and understandable, and check for personal information. The groups should have a similar mix of review lengths, ratings and issues. Each review group will be analysed using all three approaches. A person who completes both a manual task and an AI-assisted task will receive different review groups, so they do not analyse the same reviews twice.

## AI tool and three approaches

I will build a small AI/NLP pipeline: a sequence of steps that assigns review categories, groups reviews into themes, writes summaries and suggests product improvements. NLP means natural language processing, or using software to work with written language. The design will draw on Dąbrowski et al. (2022) and Yan et al. (2023), listed in the [references](../references/README.md).

| Approach | What happens |
|---|---|
| Manual | A person reads the reviews and writes the report without AI. |
| AI-only | AI produces the report using the same saved instructions and model settings for each review group. |
| AI with human checking | A person checks the AI-generated report against the reviews and edits it where needed. |

Each report will contain the main topics, a short summary of each topic, references to supporting reviews, and suggested app improvements.

During human checking, the person can correct review categories, edit wording, merge related themes, split broad themes and revise summaries or suggested actions. A category describes the type of feedback, such as a bug report or feature request. A theme groups reviews about a common issue, such as login problems.

I will save the original and edited versions. For each change, I will record its type, the part changed and a short reason. I will count which refinements occur most often and include examples. These observations will answer the second sub-question.

## Comparing the reports

People producing the reports are referred to as analysts. Separate expert reviewers will assess the completed reports alongside the original reviews. The report labels will not reveal which approach produced them. Reviewers will score them from 1 (poor) to 5 (very good).

| Criterion | Question for expert reviewers |
|---|---|
| Clarity | Is the report easy to understand? |
| Usefulness | Does the report provide insights that could help someone make product decisions? |
| Actionability | Are the suggested product improvements specific and practical? |
| Relevance to the original reviews | Do the findings and suggestions reflect what the reviews actually say? |

Expert reviewers will give a separate score and a short reason for each criterion. These scores will address the first sub-question, while their written explanations will also address the third. Reviewers will receive the same scoring guidance for all reports: 1 means poor, 3 means adequate and 5 means very good, with 2 and 4 representing intermediate scores.

## Perceived workload and time

After each manual or HITL task, the analyst will answer: **How demanding did this task feel?** The proposed scale runs from 1 (very low workload) to 5 (very high workload), with space for a short explanation. This simple self-report will measure perceived workload, as required by objective 5. The question and scale will be checked in the small trial.

Time spent will be recorded separately. A short task can still feel demanding. AI-only analysis has no human analyst performing the analysis task, so it will not receive a participant workload score. Any human setup work will be documented separately.

The number of analysts and reviewers will be agreed with my supervisor after the trial. Reviewers will not assess reports they produced themselves. The order of the manual and AI-assisted tasks will vary between analysts to reduce the effect of practice or fatigue.

## Results and limits

I will compare the four report-quality scores across the three approaches and summarise the experts' written comments. I will also report the most common types of human refinement, the participants' workload ratings and the time spent. The comparison may show improvements, little difference or disadvantages from human refinement. Several ratings of the same report will be treated as opinions about that report, rather than as separate experiments.

This is a small study of one app. Its results will show what happened in this case and may not apply to every app or user. Initial data checks have been completed. Report generation and evaluation have not yet been carried out.
