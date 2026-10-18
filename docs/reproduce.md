# Download and run instructions

The data checks were run using Python 3.9.6 and the package versions listed in `requirements.txt`. The following commands are run from the main repository folder after downloading or cloning the repository.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/download.py --accept-source-terms
python scripts/download.py --verify-only
python scripts/audit.py
python scripts/sample.py --app kahoot --n 300 --seed 20261018
python -m unittest discover -s tests -v
```

The [download list](../data/manifest.json) records the original URLs, dataset versions and file checksums. A checksum is a file fingerprint used to check that the same data were downloaded.

The scripts download the source files, summarise the data checks and create a local list of reviews for manual screening. The example command selects 300 possible reviews to check before choosing the final study sample. Original data files and selected review lists are excluded from Git, so they are not uploaded to GitHub.

Source permissions are described in [data permissions and privacy](rights-and-privacy.md). The completed technical checks are recorded in the [verification report](../reports/verification.md).
