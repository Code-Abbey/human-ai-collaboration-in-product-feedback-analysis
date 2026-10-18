# Spotify and Zoom datasets

**Source:** [User Feedback Dataset from the Top 15 Downloaded Mobile Applications](https://doi.org/10.5281/zenodo.10204232).

## What it contains

The downloaded file has **15,000 reviews from 15 apps**, including **1,000 Spotify reviews** and **1,000 Zoom reviews**.

Its seven columns contain the review identifier, review text, star rating, number of likes, app identifier, app name and app version. The file does not include review dates, topic labels or summaries.

## Checks completed

| Check | Spotify | Zoom |
|---|---:|---:|
| Reviews with missing text | 0 | 0 |
| Repeated text after standardising its format | 0 | 1 |
| Reviews passing the first selection rules | 1,000 | 997 |

Reviews that pass these checks still need to be checked manually for relevant content and personal information.

## Use in the thesis

Both apps have enough reviews for the proposed study. The examples checked so far include download, playback and interface issues for Spotify, and login, meeting, sound and video issues for Zoom. These examples come from a small initial check, not a full analysis.

Missing dates prevent reliable comparisons over time, but do not prevent a comparison of the three analysis approaches.

**Permissions:** the source lists CC BY 4.0, while its description also mentions non-commercial research. The planned use is non-commercial thesis research. The original reviews are not republished in this repository.

The related paper is listed in the [references](../../references/README.md). Full field details and counts remain in the [data report](../../reports/audit.json).
