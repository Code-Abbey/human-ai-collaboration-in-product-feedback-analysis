# Top 15 mobile applications: Spotify and Zoom

## Provenance

Original [Zenodo record 10204232](https://doi.org/10.5281/zenodo.10204232), version 1.0.0, published 24 November 2023. Creators: Mohammad Hamid Asnawi, Anindya Apriliyanti Pravitasari, Tutut Herawan and Triyani Hendrawati. Associated IEEE Access paper: [10.1109/ACCESS.2023.3332644](https://doi.org/10.1109/ACCESS.2023.3332644). Use this original source rather than an unverified mirror.

## Actual contents

Downloaded `UserFeedbackData.csv`: **15,000 rows, seven columns, exactly 1,000 per app**. Apps observed: TikTok, Instagram, Facebook, WhatsApp, Telegram, Zoom, Snapchat, Facebook Messenger, CapCut, Spotify, YouTube, **HBO Now**, Cash App, Subway Surfers and Roblox. The source description says HBO Max; preserve the actual HBO Now value and document any mapping.

| Column | Meaning and observed type |
|---|---|
| `review_id` | Source review identifier; string |
| `content` | Written review; string |
| `score` | Integer star rating 1–5 |
| `TU_count` | Integer thumbs-up count |
| `app_id` | App identifier; string |
| `app_name` | App label; string |
| `RC_ver` | Review-created version; string, sometimes missing |

There is **no date column, username column, human topic label or reference summary**. A review version is not a reliable substitute for its date. Do not claim a measured 2018–2023 date range from this CSV.

## Measured quality

The complete file has no blank review text or repeated review IDs, 17 excess normalised duplicate texts, 27 missing `RC_ver` values and 15 regex privacy flags. Every text has at least five whitespace tokens; that alone does not prove a particular upstream filtering method.

| Observation | Spotify | Zoom |
|---|---:|---:|
| Rows | 1,000 | 1,000 |
| Normalised duplicate excess | 0 | 1 |
| Missing version | 0 | 24 |
| Regex privacy flags | 0 | 2 |
| Mechanical candidates | 1,000 | 997 |
| 1★ / 2★ / 3★ / 4★ / 5★ | 451 / 197 / 164 / 104 / 84 | 370 / 126 / 151 / 137 / 216 |

## Uses and limits

Spotify offers a manageable alternative for analysing complaints and requests. Zoom could support a communication/workflow case study. Both have enough initial candidates for a 150–300-review study, subject to screening. The fixed per-app counts are useful for controlled comparisons but cannot estimate market-wide issue prevalence. Avoid pooling all apps into the main study if Moh expects one app.

The 2023 publication and absent timestamps limit recency and temporal analysis. No supplied gold labels support direct category/summary accuracy scoring. Create an independent human reference for the selected task.

## Rights status

The Zenodo API declares **CC BY 4.0**, while its description states scientific research and non-commercial use. This is a source-level ambiguity. Keep use within non-commercial thesis research, cite both dataset and paper, and seek clarification before broader redistribution or commercial reuse. This repository provides a reproducible original-source download, not a copy of its review text. [Rights details](../rights-and-privacy.md).
