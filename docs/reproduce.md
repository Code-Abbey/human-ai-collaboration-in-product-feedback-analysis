# Download and run instructions

The recorded checks used Python 3.9.6 and the package versions in `requirements.txt`.

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

The scripts download the source files, produce summary checks and create a local list of candidate reviews. The 300 candidates are a preparation list, not the final study sample. Raw files and candidate reviews are excluded from Git.

Source permissions are described in [data permissions and privacy](rights-and-privacy.md). The completed technical checks are recorded in the [verification report](../reports/verification.md).
