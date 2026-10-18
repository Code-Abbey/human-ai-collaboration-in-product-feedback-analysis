# Data provenance, licences and handling

Assessment date: 18 October 2026.

| Dataset | Source declaration | Research handling |
|---|---|---|
| [GenAI-EdSent](https://huggingface.co/datasets/Erfan-Nourbakhsh/GenAI-EdSent) | CC BY-NC 4.0 for data; MIT for code | Non-commercial thesis research; attribution and version recorded |
| [Top 15](https://zenodo.org/records/10204232) | CC BY 4.0 in metadata; scientific/non-commercial use in the description | Use restricted to non-commercial research while the differing declarations remain unresolved |
| [RARE v2](https://zenodo.org/records/13939427) | CC BY 4.0 | Source attribution and transformation records retained |

The relevant licence links are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Source licences apply to third-party data independently of the repository's code licence. Other rights, including privacy rights, may still apply to review text.

## Data minimisation

The public repository contains source metadata, scripts, aggregate statistics and research documentation. Raw reviews, real-text candidate files and participant records are excluded from Git. The original data remain reproducible through versioned download URLs and checksums.

Pilot annotation exports retain review text, rating and a local candidate identifier. Usernames, avatars, original review IDs, developer replies and developer contact fields are omitted. Deterministic candidate identifiers support tracking but do not anonymise the text.

The automatic screening expression flags possible email addresses, URLs and telephone numbers. Manual screening remains necessary for names, contextual identifiers and sensitive content. Review text will be checked before inclusion in study materials or submission to an external model service. The final protocol will specify storage, access and retention arrangements for the selected corpus and participant records.

## Transformation records

Original downloaded files remain unchanged. Duplicate detection uses Unicode, case and whitespace normalisation. Candidate selection filters rows and removes metadata columns while preserving the selected source text locally. Subsequent redactions and exclusions will be recorded alongside the study data.

The dataset and associated publication are cited separately in the [bibliography](../references/references.bib). Published results will use aggregate findings and appropriately reviewed examples.
