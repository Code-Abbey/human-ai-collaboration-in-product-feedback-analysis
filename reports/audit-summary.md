# Data-check results

These results were generated from the downloaded files using `scripts/audit.py`. They describe the available data before the final study sample is selected.

| Dataset | Total reviews | No text | Repeated text | Under 5 words | Possible contact details | Passing initial checks |
|---|---:|---:|---:|---:|---:|---:|
| Kahoot! | 34,147 | 5 | 9,905 | 18,873 | 7 | 15,143 |
| Top 15 (all apps) | 15,000 | 0 | 17 | 0 | 15 | 14,968 |
| Spotify | 1,000 | 0 | 0 | 0 | 0 | 1,000 |
| Zoom | 1,000 | 0 | 1 | 0 | 2 | 997 |
| RARE: gold test set | 5,000 | 0 | 12 | 0 | 1 | 4,987 |
| RARE: gold training set | 5,000 | 0 | 126 | 0 | 1 | 4,873 |
| RARE: silver set | 10,000 | 0 | 2 | 0 | 5 | 9,993 |

## What the checks mean

- **Repeated text:** reviews matching an earlier review after standardising character forms, capitalisation and spacing.
- **Under 5 words:** the script counts items separated by spaces. Short reviews may still contain useful feedback, so this is an initial selection rule.
- **Possible contact details:** text flagged by an automatic check for email addresses, web links or telephone numbers. It can miss personal information or flag harmless text.
- **Passing initial checks:** reviews with text, at least five words, no earlier matching text and no contact-detail flag. They still need manual checks for language, relevance and privacy.

The problem counts overlap, so they should not be added together. The Top 15 total already includes the Spotify and Zoom rows shown separately. Star ratings are user opinions, not verified labels for review topics or software faults.

## Repeated reviews across RARE files

Some original review texts appear in more than one RARE file. The counts below show the number of different matching texts after the same formatting checks:

- RARE: gold test set and RARE: gold training set: 130 matching texts.
- RARE: gold test set and RARE: silver set: 8 matching texts.
- RARE: gold training set and RARE: silver set: 155 matching texts.

This matters if RARE is used to train and test a model, because test reviews should be separate from training reviews. RARE is background material for the main thesis study.

The [full data report](audit.json) contains the column names, missing values, star-rating counts, available dates and other technical details.
