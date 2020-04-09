import unittest
import pandas
from assignment_1_1.function_1_1 import convert_names

class Test(unittest.TestCase):
    def test_function(self):
        test_df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        self.assertEqual(test_df.columns.tolist(), ["abbrev"])

if __name__ == "__main__":
    unittest.main()
