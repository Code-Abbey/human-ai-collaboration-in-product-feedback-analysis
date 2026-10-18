# Current status and next steps

As of 18 October 2026.

## Complete

- Resolved source datasets and linked academic publications.
- Downloaded and parsed both Kahoot! shards, all Top 15 rows and all usable RARE workbooks.
- Verified downloaded SHA-256 checksums and Zenodo publisher MD5 checksums.
- Audited schemas, nulls, ratings, text lengths, duplicate text, dates where available, privacy regex flags and RARE split overlap.
- Prepared reproducible local-only 300-candidate pilot lists for Kahoot!, Spotify and Zoom.
- Documented source licences, discrepancies, task suitability and a proposed human-in-the-loop evaluation.

See [verification log](../reports/verification.md) for executed checks and [measured audit](../reports/audit-summary.md) for counts.

## Pending research decisions

1. **Abiodun + Moh:** confirm Kahoot! versus Spotify, final research question and how the proposed conditions align with the approved concept.
2. **Abiodun:** screen 30–50 pilot candidates, draft a codebook, estimate annotation effort and document exclusions. The prepared candidate sets are not yet approved samples.
3. **Abiodun + Moh:** select annotators and independent evaluators; finalise sampling, metrics, batch design and feasibility of inference.
4. **University process:** confirm storage, model-service handling and any required ethics/data review; set retention dates.
5. **Implementation:** run baselines only after data/splits are frozen, then log human edits and conduct blinded evaluation.
6. **Sharing:** obtain Moh's GitHub username, invite him and verify acceptance. Owner access does not prove supervisor access.

## Explicitly not done

No full GenAI-EdSent audit, exhaustive language or privacy review, near-duplicate clustering, cross-source deduplication, category annotation, model training, summary generation or human-benefit experiment. No source authors contacted. No real review text committed to Git. The files describe historical snapshots, not current app quality.
