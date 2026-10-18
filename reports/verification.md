# Checks completed

Date: 18 October 2026.

- Both Kahoot! files, the Top 15 CSV and the RARE archive were downloaded and opened successfully.
- File checksums matched the recorded values. The Zenodo files also matched the source's checksums.
- Downloading the files again in a separate folder produced the same data-check results.
- Local lists of 300 candidate reviews were prepared for Kahoot!, Spotify and Zoom.
- Repeating the Kahoot! selection with the same settings produced the same list.
- Four automated tests passed, covering missing text, repeated text, invalid dates and changed file contents.

The recorded environment used Python 3.9.6 and the versions in `requirements.txt`.

## Small content check

The first six selected reviews for each app were inspected: 18 reviews in total.

- Kahoot! included general praise and an account-creation complaint.
- Spotify included downloads, playback, advertising and interface feedback.
- Zoom included login, meeting, audio/video and teaching feedback.

This small check helped identify possible uses. It does not establish how common each issue is. A larger manual screening sample is still needed.

These checks concern data preparation. The main analysis and participant study have not yet been run. Full technical results are in [audit.json](audit.json).
