"""Synthetic fixtures check exclusion and missing-data semantics, without real reviews."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit import normalise, profile
from download import digest

class AuditTests(unittest.TestCase):
    def test_normalisation_and_missing_text(self):
        s = normalise(pd.Series([' Ａ  useful\nreview ', 'a useful review', None]))
        self.assertEqual(s.tolist(), ['a useful review', 'a useful review', ''])

    def test_candidate_exclusions_are_not_added_independently(self):
        df = pd.DataFrame({'text': [None, 'A useful review about login', ' a useful REVIEW about login ', 'Bad', 'Please email me at a@example.com'], 'rating': [None, 5, 5, 1, 9]})
        out = profile(df, 'text', 'rating')
        self.assertEqual(out['blank_text'], 1)
        self.assertEqual(out['normalised_duplicate_text_excess'], 1)
        self.assertEqual(out['potential_email_url_phone_rows'], 1)
        self.assertEqual(out['mechanically_eligible_rows'], 1)
        self.assertEqual(out['invalid_or_missing_ratings'], 2)

    def test_invalid_dates_remain_visible(self):
        df = pd.DataFrame({'text':['A usable review with words']*2, 'date':['2020-01-01','invalid']})
        self.assertEqual(profile(df,'text',date='date')['missing_or_unparseable_dates'],1)

    def test_checksum_detects_changed_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder)/'fixture'
            p.write_bytes(b'original')
            first = digest(p)
            self.assertEqual(first, hashlib.sha256(b'original').hexdigest())
            p.write_bytes(b'changed')
            self.assertNotEqual(first, digest(p))

if __name__ == '__main__':
    unittest.main()
