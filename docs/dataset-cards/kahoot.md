# Kahoot! dataset

**Source:** [GenAI-EdSent on Hugging Face](https://huggingface.co/datasets/Erfan-Nourbakhsh/GenAI-EdSent).

## What it contains

The downloaded Kahoot! files contain **34,147 reviews**. They include review text, star ratings, dates, app versions and other app information. The observed review dates range from December 2013 to August 2025.

The files do not contain ready-made topic labels or summaries. These will be produced during the thesis work.

## Checks completed

- Five reviews have no text.
- 9,905 rows repeat earlier text after differences in case and spacing are removed.
- 18,873 reviews contain fewer than five words.
- Most reviews give five stars.
- 15,143 reviews pass the first selection rules. They still need a manual check for useful content and personal information.

These counts overlap: for example, a short review can also be repeated.

## Use in the thesis

Kahoot! is the proposed main app. It provides enough reviews for a small study, although many comments are short or general. The reviews describe past experiences, rather than the app's current condition.

**Data licence:** CC BY-NC 4.0, for non-commercial use with attribution. The related paper and DOI are listed in the [references](../../references/README.md). Full field details and counts remain in the [data report](../../reports/audit.json).
