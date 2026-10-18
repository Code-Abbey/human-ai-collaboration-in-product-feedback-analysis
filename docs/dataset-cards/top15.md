# Spotify and Zoom datasets

**Source:** [User Feedback Dataset from the Top 15 Downloaded Mobile Applications](https://doi.org/10.5281/zenodo.10204232).

## What it contains

The downloaded file has **15,000 reviews from 15 apps**, including **1,000 Spotify reviews** and **1,000 Zoom reviews**.

Its seven fields contain the review ID, text, star rating, number of likes, app ID, app name and app version. There are no review dates or ready-made topics and summaries.

## Checks completed

| Check | Spotify | Zoom |
|---|---:|---:|
| Reviews with missing text | 0 | 0 |
| Repeated text after case/spacing checks | 0 | 1 |
| Reviews passing the first selection rules | 1,000 | 997 |

Passing these rules does not replace manual checks for relevant content and personal information.

## Use in the thesis

Both apps have enough reviews for the proposed study. Initial examples cover downloads, playback and interface issues for Spotify, and login, meetings and audio/video for Zoom. These examples are not yet a full analysis.

Missing dates prevent reliable comparisons over time, but do not prevent a comparison of the three analysis approaches.

**Permissions:** the source lists CC BY 4.0, while its description also mentions non-commercial research. The proposed use is non-commercial thesis research; raw reviews are not republished here.

The related paper is listed in the [references](../../references/README.md). Full field details and counts remain in the [data report](../../reports/audit.json).
