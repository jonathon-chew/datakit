import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "datakit"

if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ProfileColumn # type: ignore
import Top # type: ignore
from correlation import correlation # type: ignore

class AnalysisHelpersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture_dir = ROOT / "tests"
        cls.classification_df = pd.read_csv(cls.fixture_dir / "classification_signals.csv")
        cls.correlation_df = pd.read_csv(cls.fixture_dir / "correlation_signals.csv")

    def test_top_returns_most_frequent_values_first(self) -> None:
        values = self.classification_df["status_tier"].tolist()

        self.assertEqual(Top.Top(values, 2), ["bronze", "silver"])

    def test_correlation_handles_positive_and_negative_relationships(self) -> None:
        base = self.correlation_df["base_users"].tolist()
        expanded = self.correlation_df["expanded_users"].tolist()
        inverse = self.correlation_df["inverse_signal"].tolist()

        self.assertAlmostEqual(correlation(base, expanded), 1.0, places=9)
        self.assertAlmostEqual(correlation(base, inverse), -1.0, places=9)

    def test_correlation_rejects_mismatched_lengths(self) -> None:
        with self.assertRaises(ValueError):
            correlation([1, 2, 3], [1, 2])

    def test_profile_column_detects_identifier(self) -> None:
        profile = ProfileColumn.ProfileColumn(
            self.classification_df,
            "customer_id",
            len(self.classification_df.index),
            top=3,
        )

        self.assertEqual(profile["kind"], "numeric")
        self.assertEqual(profile["role"], "identifier")
        self.assertEqual(profile["uniqueCount"], 20)

    def test_profile_column_detects_categorical_boolean_constant_and_sparse(self) -> None:
        row_count = len(self.classification_df.index)

        tier_profile = ProfileColumn.ProfileColumn(self.classification_df, "status_tier", row_count, top=3)
        active_profile = ProfileColumn.ProfileColumn(self.classification_df, "is_active", row_count, top=3)
        constant_profile = ProfileColumn.ProfileColumn(self.classification_df, "constant_source", row_count, top=3)
        sparse_profile = ProfileColumn.ProfileColumn(self.classification_df, "sparse_score", row_count, top=3)

        self.assertEqual(tier_profile["kind"], "categorical")
        self.assertEqual(tier_profile["role"], "feature")
        self.assertEqual(tier_profile["TopValues"], ["bronze", "silver", "gold"])

        self.assertEqual(active_profile["kind"], "boolean")
        self.assertEqual(active_profile["role"], "feature")

        self.assertEqual(constant_profile["role"], "constant")
        self.assertIn("api", constant_profile["imbalence"])

        self.assertEqual(sparse_profile["kind"], "numeric")
        self.assertEqual(sparse_profile["role"], "sparse")
        self.assertEqual(sparse_profile["missing"], 70.0)
        self.assertEqual(
            sparse_profile["stats"],
            {"min": 10.0, "max": 60.0, "mean": 35.0, "range": 50.0},
        )


if __name__ == "__main__":
    unittest.main()
