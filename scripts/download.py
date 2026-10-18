"""Download the recorded dataset versions and check that the files match their saved checksums."""
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accept-source-terms', action='store_true')
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if not args.verify_only and not args.accept_source_terms:
        parser.error('Read docs/rights-and-privacy.md, then pass --accept-source-terms.')
    records = []
    for item in json.loads((ROOT / 'data/manifest.json').read_text())['files']:
        dest = ROOT / item['path']
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() and not args.verify_only:
            temp = dest.with_suffix(dest.suffix + '.part')
            try:
                req = Request(item['url'], headers={'User-Agent': 'ThesisFeasibility/1.0'})
                with urlopen(req, timeout=120) as response, temp.open('wb') as f:
                    while chunk := response.read(1024 * 1024):
                        f.write(chunk)
                if digest(temp) != item['sha256']:
                    raise ValueError('Downloaded checksum differs: ' + item['path'])
                os.replace(temp, dest)
            finally:
                temp.unlink(missing_ok=True)
        if not dest.exists() or digest(dest) != item['sha256']:
            raise ValueError('Missing or changed file: ' + item['path'])
        records.append({'path': item['path'], 'sha256': item['sha256'], 'verified': True})
        print('Verified', item['path'])
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports/download-log.json').write_text(json.dumps({
        'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'files': records}, indent=2)+'\n')

if __name__ == '__main__':
    main()
