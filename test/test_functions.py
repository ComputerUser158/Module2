"""
Author: Rawley Collins
Program: camper_age_input


Program takes value from user as integer for years of age and returns age in integer for age in months.
"""

import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, camper_age_input.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()
