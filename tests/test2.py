import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "tests"

class DatasetFixtureTests(unittest.TestCase):
    def test_added_csv_fixtures_load_cleanly(self) -> None:
        expected_files = [
            "classification_signals.csv",
            "correlation_signals.csv",
            "customer_segments.csv",
            "fake_customer_data.csv",
            "sparse_operations.csv",
        ]

        for fixture_name in expected_files:
            with self.subTest(fixture=fixture_name):
                df = pd.read_csv(FIXTURE_DIR / fixture_name)
                self.assertEqual(len(df.columns), 12)
                self.assertGreaterEqual(len(df.index), 18)
                self.assertTrue(df.select_dtypes(include=["number"]).shape[1] >= 3)
                self.assertTrue(df.select_dtypes(exclude=["number"]).shape[1] >= 3)

    def test_sparse_fixture_contains_missing_values_for_edge_case_work(self) -> None:
        df = pd.read_csv(FIXTURE_DIR / "sparse_operations.csv")

        self.assertGreater(df["assigned_to"].isna().sum(), 0)
        self.assertGreater(df["csat_score"].isna().sum(), 0)
        self.assertGreater(df["notes"].isna().sum(), 0)


if __name__ == "__main__":
    unittest.main()
