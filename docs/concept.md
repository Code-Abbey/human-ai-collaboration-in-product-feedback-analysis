# Concept overview

**Human-AI Collaboration in Product Feedback Analysis: Evaluating AI-Generated Themes, Summaries, and Human Refinement**

Abiodun Michael Adefusi · Bachelor's thesis

This page summarises the concept draft for this thesis. The [research questions and objectives](research-questions.md) retain the submitted wording, and the [study plan](study-plan.md) describes the proposed practical work.

## Topic and motivation

App reviews contain information about bugs, usability problems, feature requests and other needs that can guide product improvement (Dąbrowski et al., 2022). Reading and organising many reviews takes time. AI can help, but its categories, themes and summaries may still need human judgement.

This thesis will compare manual analysis, AI-only analysis and AI-assisted analysis with human refinement. The project brings together Applied AI, Human-Computer Interaction, user experience (UX) and product development.

## Proposed system

The proposed pipeline will clean reviews, classify feedback, group related reviews, write summaries and suggest product improvements. Existing AI/NLP methods will be used rather than training a large language model from scratch (Wei et al., 2023).

Sentence-BERT may help identify reviews with similar meanings (Reimers & Gurevych, 2019). BERTopic may help group reviews into topics (Grootendorst, 2022). InsightBench provides related background on generating insights and suggested actions through several analysis steps (Sahu et al., 2025). These are methods and design ideas to explore, not completed parts of the prototype.

A dashboard will allow users to correct classifications, rename, merge or split themes, move reviews between groups, edit summaries and refine suggested actions. Interactive machine learning and labelling research inform these features (Amershi et al., 2014; Chegini et al., 2019, 2020). Human-AI interaction guidelines and thematic-analysis research will guide user control and human refinement (Amershi et al., 2019; Yan et al., 2023).

## Scope and evaluation

Kahoot! is a candidate dataset, with Spotify and Zoom as alternatives. The researcher has not yet downloaded the thesis dataset. The review count suggested in the concept was an initial proposal, not a fixed limit. The final number may be larger and will be agreed with the supervisor after the dataset has been selected and inspected.

The three approaches will produce comparable feedback reports. Approximately 3–6 experts will assess the reports without being told which approach produced them. The proposed criteria are clarity, usefulness, actionability, relevance to the original reviews, completeness and overall quality. Human corrections, time spent and perceived workload will also be recorded where feasible.

The main outcomes will be a working prototype and an evaluation of the three approaches. The study may identify benefits, limitations or little difference between them.

## Programme relevance

The project connects Applied AI and Machine Learning with Human-Computer Interaction, usability evaluation, interface design, prototyping and software development in the Creative Computing programme.

The [six-month plan](project-plan.md) outlines the work. All ten sources cited in the concept are included in the [concept bibliography](../references/concept-references.md).
