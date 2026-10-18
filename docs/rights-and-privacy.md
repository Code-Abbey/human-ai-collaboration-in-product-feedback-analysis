# Source rights and research-data handling

Reviewed 18 October 2026. This records the publisher's terms and our handling decisions; it is not a claim to own user-written reviews.

| Source | Observed declaration | Repository decision |
|---|---|---|
| [GenAI-EdSent](https://huggingface.co/datasets/Erfan-Nourbakhsh/GenAI-EdSent) | CC BY-NC 4.0 for data; MIT for code | Non-commercial research; original download route; no raw review redistribution |
| [Top 15](https://zenodo.org/records/10204232) | API: CC BY 4.0; prose: scientific research/non-commercial | Preserve both statements; use within their common non-commercial scope; clarify before broader reuse |
| [RARE v2](https://zenodo.org/records/13939427) | CC BY 4.0 | Attribute source/paper; download locally; keep real text out of Git |

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) require attribution and indication of changes. NC additionally limits commercial use. These licences do not guarantee all necessary privacy, publicity or other third-party permissions. Dataset availability is not blanket permission to republish personal information. An MIT code licence does not replace the dataset licence.

## Practical handling

- Download only published dataset files; no new Google Play scraping is used.
- Keep immutable originals under ignored `data/raw/`. Never force-add these files to Git.
- Keep only text and rating in pilot annotation exports. Exclude source usernames, avatars, review IDs, replies and developer contact fields.
- Manually review text for names, contact details, school/workplace clues, sensitive stories and other identifiable content. Regex screening catches only some patterns. Education-app reviews may involve children; do not infer or annotate reviewer ages or identities.
- Generated candidate IDs are deterministic text hashes for local tracking, **not anonymisation**. Text can be searchable even after removing names. Candidate IDs and text remain local-only.
- Store annotations on the university-approved restricted storage chosen for the project. Do not upload them to third-party LLM services until the data-handling arrangement is agreed. No such uploads occurred in this work.
- Prefer aggregate counts and paraphrased examples in the thesis; assess any necessary verbatim quotation separately. Preserve attribution without identifying individual reviewers.
- Record exclusions/redactions, who can access data and a retention/deletion date in the study protocol before recruitment or annotation. No university-specific retention rule is invented here.

## Attribution and derivatives

The manifest identifies original sources and exact downloaded bytes. The audit reports derived statistics. Candidate selection normalises text for duplicate detection, filters rows and removes metadata columns; source text itself is retained unchanged locally. Any later redaction must be logged. Cite the dataset record and its linked paper from `references/references.bib`.

The repository contains our scripts/documentation and source metadata, not a sublicense of third-party review data. Private visibility does not remove source obligations. If publication is later requested, review the tracked files and history before changing visibility.
