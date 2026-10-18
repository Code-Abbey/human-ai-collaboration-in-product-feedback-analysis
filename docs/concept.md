# Concept overview

**Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement**

Abiodun Michael Adefusi · Bachelor's thesis

This page summarises my concept draft. The [research questions and objectives](research-questions.md) retain the submitted wording, and the [study plan](study-plan.md) describes the proposed practical work.

## Topic and motivation

App reviews contain information about bugs, usability problems, feature requests and other needs that can guide product improvement (Dąbrowski et al., 2022). Reading and organising many reviews takes time. AI can help, but its categories, themes and summaries may still need human judgement.

My thesis will compare manual analysis, AI-only analysis and AI-assisted analysis with human refinement. My interest in Applied AI, Human-Computer Interaction, UX and product development motivates the project.

## Proposed system

I will build a small pipeline that cleans reviews, classifies feedback, groups related reviews, writes summaries and suggests product improvements. Existing AI/NLP methods will be used rather than training a large language model from scratch (Wei et al., 2023).

Sentence-BERT may help identify reviews with similar meanings (Reimers & Gurevych, 2019). BERTopic may help group reviews into topics (Grootendorst, 2022). InsightBench provides related background on generating insights and suggested actions through several analysis steps (Sahu et al., 2025). These are methods and design ideas to explore, not completed parts of the prototype.

A dashboard will allow users to correct classifications, rename, merge or split themes, move reviews between groups, edit summaries and refine suggested actions. Interactive machine learning and labelling research inform these features (Amershi et al., 2014; Chegini et al., 2019, 2020). Human-AI interaction guidelines and thematic-analysis research will guide user control and human refinement (Amershi et al., 2019; Yan et al., 2023).

## Scope and evaluation

The study will use approximately 100–300 reviews from a selected app. Kahoot! is the current proposal following the dataset checks; Spotify and Zoom are alternatives. The final dataset and evaluation details will be agreed with my supervisor.

The three approaches will produce comparable feedback reports. Approximately 3–6 experts will assess the reports without being told which approach produced them. The proposed criteria are clarity, usefulness, actionability, relevance to the original reviews, completeness and overall quality. Human corrections, time spent and perceived workload will also be recorded where feasible.

The main outcomes will be a working prototype and an evaluation of the three approaches. The study may identify benefits, limitations or little difference between them.

## Programme relevance

The project connects Applied AI and Machine Learning with Human-Computer Interaction, usability evaluation, interface design, prototyping and software development in the Creative Computing programme.

The [six-month plan](project-plan.md) outlines the work. All ten sources cited in the concept are included in the [concept bibliography](../references/concept-references.md).
