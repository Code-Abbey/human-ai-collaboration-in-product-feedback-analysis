"""Summarise data quality without publishing review text or reviewer details."""
import io
import json
import re
import zipfile
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw'
PATTERN = r'(?i)(?:\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b|https?://\S+|\b(?:\+?\d[\d ()-]{7,}\d)\b)'

def normalise(series):
    return series.fillna('').astype(str).str.normalize('NFKC').str.casefold().str.replace(r'\s+', ' ', regex=True).str.strip()

def load_sources():
    k = pd.concat([pd.read_parquet(RAW / f'kahoot-{i}.parquet') for i in range(2)], ignore_index=True)
    t = pd.read_csv(RAW / 'top15.csv')
    rare = {}
    with zipfile.ZipFile(RAW / 'rare.zip') as z:
        for name in sorted(z.namelist()):
            if name.endswith('.xlsx') and not Path(name).name.startswith('~$'):
                rare[Path(name).stem] = pd.read_excel(io.BytesIO(z.read(name)))
    return k, t, rare

def profile(df, text, rating=None, date=None, identifier=None, app=None):
    s = df[text].fillna('').astype(str)
    n = normalise(s)
    lengths = s.str.split().str.len()
    eligible = n.ne('') & lengths.ge(5) & ~n.duplicated() & ~s.str.contains(PATTERN, regex=True)
    out = {
        'rows': len(df), 'columns': {c: str(df[c].dtype) for c in df},
        'nulls': {c: int(df[c].isna().sum()) for c in df},
        'text_column': text, 'blank_text': int(n.eq('').sum()),
        'exact_duplicate_text_excess': int(s.duplicated().sum()),
        'normalised_duplicate_text_excess': int(n.duplicated().sum()),
        'under_5_whitespace_tokens': int(lengths.lt(5).sum()),
        'token_length_quantiles': {str(q): float(lengths.quantile(q)) for q in [0, .25, .5, .75, .95, 1]},
        'potential_email_url_phone_rows': int(s.str.contains(PATTERN, regex=True).sum()),
        'mechanically_eligible_rows': int(eligible.sum()),
    }
    if rating:
        out['rating_counts'] = {str(a): int(b) for a,b in df[rating].value_counts(dropna=False).sort_index().items()}
        out['invalid_or_missing_ratings'] = int((~df[rating].isin([1,2,3,4,5])).sum())
    if date:
        dates = pd.to_datetime(df[date], errors='coerce', utc=True)
        out['date_range'] = [str(dates.min()), str(dates.max())]
        out['missing_or_unparseable_dates'] = int(dates.isna().sum())
    if identifier:
        out['duplicate_id_excess'] = int(df[identifier].duplicated().sum())
    if app:
        out['app_counts'] = {str(a):int(b) for a,b in df[app].value_counts().items()}
    return out

def main():
    k,t,rare = load_sources()
    out = {'definitions': {
        'duplicates': 'Repeated rows after the first occurrence, including repeated blank text. This count does not identify fake reviews.',
        'normalisation': 'Standardise character forms, ignore capitalisation, and remove extra spaces. Punctuation is kept.',
        'eligible': 'Reviews with text, at least five items separated by spaces, no earlier occurrence of the standardised text, and no automatic email, web-link or phone-number flag. Language, relevance and personal information still need manual checks.',
        'privacy': 'Automatic checks can miss personal information or flag harmless text. Names and personal stories still need manual review.',
    }, 'datasets': {}}
    out['datasets']['kahoot'] = profile(k,'review_content','review_score','review_at','review_reviewId','app_name')
    out['datasets']['top15'] = profile(t,'content','score',identifier='review_id',app='app_name')
    for name in ['Spotify','Zoom']:
        out['datasets'][name.lower()] = profile(t[t.app_name.eq(name)],'content','score',identifier='review_id')
    for name,df in rare.items():
        out['datasets'][name] = profile(df,'Extracted_Review',app='App_Name')
        target = 'Gold_Standard' if 'Gold_Standard' in df else 'Refined_Review'
        out['datasets'][name]['target_blank'] = int(normalise(df[target]).eq('').sum())
        out['datasets'][name]['unchanged_normalised_pairs'] = int((normalise(df[target]) == normalise(df.Extracted_Review)).sum())
    out['rare_overlap_unique_normalised_originals'] = {}
    names = list(rare)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            out['rare_overlap_unique_normalised_originals'][a+' vs '+b] = len(set(normalise(rare[a].Extracted_Review)) & set(normalise(rare[b].Extracted_Review)))
    (ROOT/'reports/audit.json').write_text(json.dumps(out,indent=2)+'\n')
    labels = {
        'kahoot': 'Kahoot!', 'top15': 'Top 15 (all apps)',
        'spotify': 'Spotify', 'zoom': 'Zoom',
        'Gold_Corpus_5k_Testing': 'RARE: gold test set',
        'Gold_Corpus_5k_Training': 'RARE: gold training set',
        'Silver_Corpus_10k': 'RARE: silver set',
    }
    lines = ['# Data-check results', '',
        'These results were generated from the downloaded files using `scripts/audit.py`. They describe the available data before the final study sample is selected.', '',
        '| Dataset | Total reviews | No text | Repeated text | Under 5 words | Possible contact details | Passing initial checks |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for name,p in out['datasets'].items():
        lines.append(f"| {labels.get(name, name)} | {p['rows']:,} | {p['blank_text']:,} | {p['normalised_duplicate_text_excess']:,} | {p['under_5_whitespace_tokens']:,} | {p['potential_email_url_phone_rows']:,} | {p['mechanically_eligible_rows']:,} |")
    lines += ['', '## What the checks mean', '',
        '- **Repeated text:** reviews matching an earlier review after standardising character forms, capitalisation and spacing.',
        '- **Under 5 words:** the script counts items separated by spaces. Short reviews may still contain useful feedback, so this is an initial selection rule.',
        '- **Possible contact details:** text flagged by an automatic check for email addresses, web links or telephone numbers. It can miss personal information or flag harmless text.',
        '- **Passing initial checks:** reviews with text, at least five words, no earlier matching text and no contact-detail flag. They still need manual checks for language, relevance and privacy.', '',
        'The problem counts overlap, so they should not be added together. The Top 15 total already includes the Spotify and Zoom rows shown separately. Star ratings are user opinions, not verified labels for review topics or software faults.', '',
        '## Repeated reviews across RARE files', '',
        'Some original review texts appear in more than one RARE file. The counts below show the number of different matching texts after the same formatting checks:', '']
    for key,value in out['rare_overlap_unique_normalised_originals'].items():
        a, b = key.split(' vs ')
        lines.append(f'- {labels.get(a, a)} and {labels.get(b, b)}: {value} matching texts.')
    lines += ['', 'This matters if RARE is used to train and test a model, because test reviews should be separate from training reviews. RARE is background material for the main thesis study.', '',
        'The [full data report](audit.json) contains the column names, missing values, star-rating counts, available dates and other technical details.']
    (ROOT/'reports/audit-summary.md').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))

if __name__ == '__main__':
    main()
