"""Prepare a repeatable local list of reviews for manual screening before the study."""
import argparse
import hashlib
import json
from audit import ROOT, PATTERN, load_sources, normalise

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--app', choices=['kahoot','spotify','zoom'], default='kahoot')
    p.add_argument('--n', type=int, default=300)
    p.add_argument('--seed', type=int, default=20261018)
    args = p.parse_args()
    if args.n < 1:
        p.error('--n must be positive')
    k,t,_ = load_sources()
    if args.app == 'kahoot':
        df = k[['review_content','review_score']].rename(columns={'review_content':'text','review_score':'rating'})
    else:
        df = t[t.app_name.str.lower().eq(args.app)][['content','score']].rename(columns={'content':'text','score':'rating'})
    df = df.copy()
    norm = normalise(df.text)
    keep = norm.ne('') & df.text.fillna('').str.split().str.len().ge(5) & ~norm.duplicated() & ~df.text.fillna('').str.contains(PATTERN,regex=True)
    df = df[keep].copy()
    # A salted deterministic ordering avoids dependency-specific RNG behaviour.
    df['candidate_id'] = df.text.map(lambda x: hashlib.sha256((str(args.seed)+'\0'+x).encode()).hexdigest())
    df = df.sort_values('candidate_id')
    if len(df) < args.n:
        raise ValueError(f'Only {len(df)} candidates available; requested {args.n}')
    selected = df.head(args.n)
    folder = ROOT/'data/annotation'
    folder.mkdir(parents=True,exist_ok=True)
    path = folder/(args.app+'-candidates.jsonl')
    with path.open('w') as f:
        for row in selected.to_dict('records'):
            row.update({'language_ok': None, 'privacy_ok': None, 'relevant': None, 'labels': [], 'split': None})
            f.write(json.dumps(row,ensure_ascii=False)+'\n')
    (folder/(args.app+'-sampling.json')).write_text(json.dumps({'app':args.app,'seed':args.seed,'n':args.n,'eligible':len(df),'method':'unstratified SHA256 deterministic ordering; manual screening pending','candidate_ids':selected.candidate_id.tolist()},indent=2)+'\n')
    print(f'Saved {len(selected)} reviews for manual screening to {path.relative_to(ROOT)}. This file is excluded from Git.')

if __name__ == '__main__':
    main()
