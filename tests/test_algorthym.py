import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "datakit"

if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ProfileColumn # type: ignore
import Top # type: ignore
from correlation import correlation as c # type: ignore

class AlgorthymHelpersTests(unittest.TestCase):
    def test_Correlation(self):
        x = [40, 25, 22, 54]
        y = [99, 79, 69, 89]

        result = c(x, y)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 0.725312798712089)


if __name__ == "__main__":
    unittest.main()