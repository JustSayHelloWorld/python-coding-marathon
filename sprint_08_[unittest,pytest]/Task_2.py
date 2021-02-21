"""You have function divide

Please, write the code with unit tests for the function "divide":
minimum 3 tests
must chek all flows
all test must be pass
no failures
no skip"""

import unittest


class DivideTest(unittest.TestCase):

    def test_int_num_float_result(self):
        expected = 5.0
        actual = divide(10, 2)
        self.assertEqual(actual, expected)

    def test_zero_division(self):
        self.assertRaises(Exception, divide, 3, 0)

    def test_float_num_float_result(self):
        expected = 2.0
        actual = divide(12.2, 6.1)
        self.assertEqual(actual, expected)

    def test_string(self):
        self.assertRaises(Exception, divide, 5, "3")
