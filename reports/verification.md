# Executed verification

Run date: 18 October 2026. This log separates executed checks from proposed research.

| Check | Observed result |
|---|---|
| Original-source downloads | Four binary/data files downloaded, total 16,297,679 bytes |
| Integrity | All four SHA-256 hashes verified; both Zenodo MD5 checksums matched publisher records |
| Fresh-folder downloader | `download.py --accept-source-terms` fetched all four files independently and passed hash verification |
| Full inspection | Both Kahoot! shards, complete Top 15 CSV and all three usable RARE workbooks parsed successfully |
| Repeat audit | Fresh-folder `audit.json` was byte-for-byte identical to the original run |
| Sampling | 300 candidates generated locally for each of Kahoot!, Spotify and Zoom; no usernames/avatar/review-ID fields exported |
| Sampling reproducibility | Fresh-folder Kahoot! selection using seed 20261018 was byte-for-byte identical |
| Automated checks | Four unit tests passed: missing/normalised text, overlapping exclusion rules, invalid-date reporting, checksum sensitivity |

Python 3.9.6 and the versions in `requirements.txt` were used. PyArrow emitted restricted-system CPU-cache detection warnings in this environment; it nevertheless parsed both Parquet files and the repeated aggregate output matched. Other Python versions and operating systems have not been tested.

## Small qualitative spot check

The first six deterministically selected candidate texts for each of Kahoot!, Spotify and Zoom were read during preparation (18 total). This was a convenience spot check, not a coded random-content study. No verbatim excerpts are committed.

- Kahoot! included generic praise/social references and an account-creation complaint. Passing five tokens does not ensure useful product feedback; the relevant yield remains unmeasured.
- Spotify included reported download/storage problems, playback failures, advertising and interface/playlist feedback, including mixed praise and criticism in one review.
- Zoom included meeting-sync, authentication, version/login and audio/video feedback, plus positive teaching experiences.

These examples justify a larger manual pilot, not topic-frequency estimates or confirmed software defects. No exhaustive English-language, privacy, relevance or factual-fidelity review has been performed.

## What the checks do not prove

No effectiveness experiment has been run. Mechanical filters do not guarantee anonymity, language validity or relevance. Exact normalised overlap checks do not detect every near duplicate. Checksums establish reproducible bytes, not correctness of user claims, representativeness or unrestricted rights.
