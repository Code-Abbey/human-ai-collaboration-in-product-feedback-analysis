# Earlier technical feasibility checks

Recorded: 18 October 2026.

These checks were carried out during earlier automated source assessment. They do not mean that the researcher has downloaded the thesis dataset or completed the study preparation. The current research position is recorded in [progress and next steps](../docs/status.md).

- Both Kahoot! files, the Top 15 CSV and the RARE archive were downloaded and opened successfully.
- File checksums matched the recorded values. The Zenodo files also matched the checksums published by the source.
- Downloading the files again in a separate folder produced the same data-check results.
- Local lists of 300 candidate reviews were generated for technical checking. This was an example script setting, not an agreed study size.
- Repeating the Kahoot! selection with the same settings produced the same list.
- Four automated tests passed, covering missing text, repeated text, invalid dates and changed file contents.

The recorded environment used Python 3.9.6 and the versions in `requirements.txt`.

## Small content check

The first six selected reviews for each app were inspected: 18 reviews in total.

- The Kahoot! examples included general praise and a complaint about creating an account.
- The Spotify examples included feedback about downloads, playback, advertising and the interface.
- The Zoom examples included feedback about logging in, meetings, sound, video and teaching.

This small check helped identify possible uses. It does not establish how common each issue is. A larger manual screening sample is still needed.

These checks concern data preparation. The main analysis and participant study have not yet been run. Full technical results are in [audit.json](audit.json).
