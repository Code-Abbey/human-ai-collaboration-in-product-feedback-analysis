# Study plan

## Research question

How does a Human-in-the-Loop AI workflow compare with manual analysis and AI-only analysis in producing clear, useful, and actionable product feedback insights from app reviews?

The full [research questions and objectives](research-questions.md) guide this study. Human-in-the-Loop (HITL) means that a person can check and change the AI-generated results.

## Dataset and study size

Kahoot! reviews are the proposed dataset, with Spotify and Zoom as alternatives. In line with the concept, this thesis will use approximately 100–300 reviews from one app. The final number of reviews and their division into comparable groups will be agreed with the supervisor after a small trial.

Data preparation will remove repeated reviews and check the remaining text for relevance, readability and personal information. The groups should have a similar mix of review lengths, ratings and issues. Each review group will be analysed using all three approaches. A person who completes both a manual task and an AI-assisted task will receive different review groups, so they do not analyse the same reviews twice.

## AI tool and three approaches

The proposed AI/NLP pipeline will assign review categories, group reviews into themes, write summaries and suggest product improvements. NLP means natural language processing, or using software to work with written language. Review categories may include bugs, feature requests, usability issues, performance complaints and positive feedback. Dąbrowski et al. (2022) and Wei et al. (2023) provide background for this work.

Possible methods include Sentence-BERT for identifying reviews with similar meanings (Reimers & Gurevych, 2019), BERTopic for grouping reviews into topics (Grootendorst, 2022), and an existing language model for classification, summaries and suggestions. InsightBench offers related ideas for generating insights and actions in several steps (Sahu et al., 2025). The final combination will be chosen after a small trial. These methods have not yet been implemented in this repository.

The full sources are listed in the [concept bibliography](../references/concept-references.md).

| Approach | What happens |
|---|---|
| Manual | A person reads the reviews and writes the report without AI. |
| AI-only | AI produces the report using the same saved instructions and model settings for each review group. |
| AI with human checking | A person checks the AI-generated report against the reviews and edits it where needed. |

Each report will contain the main themes, a short summary of each theme, references to supporting reviews, and suggested app improvements.

The dashboard will let the person correct review categories, rename themes, merge or split themes, move reviews between groups, and edit summaries or suggested actions. A category describes the type of feedback, such as a bug report or feature request. A theme groups reviews about a common issue, such as login problems.

The interface design will draw on interactive learning and labelling research (Amershi et al., 2014; Chegini et al., 2019, 2020), Human-AI interaction guidelines (Amershi et al., 2019), and human refinement in thematic analysis (Yan et al., 2023). These sources inform the design; a separate active-learning or model-retraining experiment is not required.

The prototype will save the original and edited versions. Each recorded change will include its type, the part changed and a short reason. The analysis will identify the most common refinements and present examples. These observations will answer the second sub-question.

## Comparing the reports

People producing the reports are referred to as analysts. Approximately 3–6 expert reviewers will assess the completed reports alongside the original reviews, as proposed in the concept. The reports will use neutral identifiers, and reviewers will not be told which approach produced each report. Reviewers will score them from 1 (poor) to 5 (very good).

| Criterion | Question for expert reviewers |
|---|---|
| Clarity | Is the report easy to understand? |
| Usefulness | Does the report provide insights that could help someone make product decisions? |
| Actionability | Are the suggested product improvements specific and practical? |
| Relevance to the original reviews | Do the findings and suggestions reflect what the reviews actually say? |
| Completeness | Does the report include the main issues in the review group? |
| Overall quality | How good is the report as a whole? |

Expert reviewers will give a separate score and a short reason for each criterion. These scores will address the first sub-question, while their written explanations will also address the third. Reviewers will receive the same scoring guidance for all reports: 1 means poor, 3 means adequate and 5 means very good, with 2 and 4 representing intermediate scores.

## Perceived workload and time

After each manual or HITL task, the analyst will answer: **How demanding did this task feel?** The proposed scale runs from 1 (very low workload) to 5 (very high workload), with space for a short explanation. This is a proposed simple measure for objective 5. Its use and wording will be checked in the small trial and agreed with the supervisor. The concept makes recording workload, time and corrections subject to feasibility.

Time spent will be recorded separately. A short task can still feel demanding. AI-only analysis has no human analyst performing the analysis task, so it will not receive a participant workload score. Any human setup work will be documented separately.

The number of analysts and the final number of expert reviewers will be agreed with the supervisor after the trial. Reviewers will not assess reports they produced themselves. The order of the manual and AI-assisted tasks will vary between analysts to reduce the effect of practice or fatigue.

## Results and limits

The analysis will compare the six report-quality scores across the three approaches and summarise the experts' written comments. Where collected, refinement records, workload ratings and task times will provide further context. The comparison may show improvements, little difference or disadvantages from human refinement. Several ratings of the same report will be treated as opinions about that report, rather than as separate experiments.

This is a small study of one app. Its results will show what happened in this case and may not apply to every app or user. Initial data checks have been completed. Report generation and evaluation have not yet been carried out.
