# Academic sources and how to use them

Verified 18 October 2026 against original repositories, ACL Anthology, arXiv and Crossref DOI metadata. Read the full papers before final thesis citation. No citation-count-based claim of quality is made.

| Source | Type / DOI | Why it matters here | What it does not establish |
|---|---|---|---|
| Mazaherian & Nourbakhsh (2025), *Unveiling User Perceptions in the Generative AI Era: A Sentiment-Driven Evaluation of AI Educational Apps' Role in Digital Transformation of e-Teaching* | arXiv preprint, [10.48550/arXiv.2512.11934](https://doi.org/10.48550/arXiv.2512.11934) | Closest provenance/context for GenAI-EdSent and educational-app feedback analysis | Peer review was not verified; model-derived analysis is not independent human ground truth |
| Asnawi, Pravitasari, Herawan & Hendrawati (2023), *The Combination of Contextualized Topic Model and MPNet for User Feedback Topic Modeling* | IEEE Access 11, 130272–130286, [10.1109/ACCESS.2023.3332644](https://doi.org/10.1109/ACCESS.2023.3332644) | Direct linked paper for Top 15; relevant topic-modelling comparator | Its method does not validate human correction benefit in our proposed study |
| Asnawi et al. (2023), *User Feedback Dataset from the Top 15 Downloaded Mobile Applications* | Dataset v1.0.0, [10.5281/zenodo.10204232](https://doi.org/10.5281/zenodo.10204232) | Exact downloadable source, schema and attribution | Licence metadata and prose differ; no dates in the actual CSV |
| Singh, Jain, Chaudhary & Anish (2024), *Refining App Reviews: Dataset, Methodology, and Evaluation* | EMNLP Industry Track, 595–608, [10.18653/v1/2024.emnlp-industry.44](https://doi.org/10.18653/v1/2024.emnlp-industry.44) | Strongest direct source for human-checked review refinement and paired reference text | Refinement quality is not the same as downstream report usefulness; our audit found split overlap |
| Singh (2024), *RARE (Repository for App review REfinement)* | Dataset v2, [10.5281/zenodo.13939427](https://doi.org/10.5281/zenodo.13939427) | Versioned source for the paired corpora | Silver outputs are not independent human references |
| Maalej & Nabil (2015), *Bug report, feature request, or simply praise? On automatically classifying app reviews* | IEEE RE, 116–125, [10.1109/RE.2015.7320414](https://doi.org/10.1109/RE.2015.7320414) | Foundation for choosing feedback categories and a classification baseline | A related-task source, not the origin of our downloaded datasets |
| Guzman & Maalej (2014), *How Do Users Like This Feature? A Fine Grained Sentiment Analysis of App Reviews* | IEEE RE, 153–162, [10.1109/RE.2014.6912257](https://doi.org/10.1109/RE.2014.6912257) | Supports distinguishing feature-level feedback from whole-app ratings | Does not make star ratings valid gold labels for individual themes |

## Citation priorities

For a Kahoot! thesis, cite GenAI-EdSent's source URL, pinned revision, access date and associated preprint. No separate GenAI-EdSent dataset DOI was verified; do not present the arXiv paper DOI as a dataset DOI.

For Spotify/Zoom Top 15, cite **both** the Zenodo dataset DOI and IEEE paper. For RARE, cite **both** the exact v2 dataset DOI and EMNLP paper. Cite methodological papers only for the methods/claims actually used; they do not grant data rights.

## Verification sources

- [GenAI-EdSent source card](https://huggingface.co/datasets/Erfan-Nourbakhsh/GenAI-EdSent/blob/32783444ddc6b56cc95996d77d0923d6eb075164/README.md) and [arXiv record](https://arxiv.org/abs/2512.11934).
- [Top 15 original metadata API](https://zenodo.org/api/records/10204232) and [Crossref paper metadata](https://api.crossref.org/works/10.1109/ACCESS.2023.3332644).
- [RARE metadata API](https://zenodo.org/api/records/13939427), [ACL record](https://aclanthology.org/2024.emnlp-industry.44/) and its publisher-supplied BibTeX.
- [Classification DOI metadata](https://api.crossref.org/works/10.1109/RE.2015.7320414).
- [Feature-level analysis institutional record](https://research.vu.nl/en/publications/how-do-users-like-this-feature-a-fine-grained-sentiment-analysis-/).

Observed file quality takes precedence over broad marketing-style dataset descriptions. Publication venue, data provenance, label independence and relevance are separate considerations.
