"""Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without comlex solution.

Write unit tests for this function with QuadraticEquationTest class

Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0"""

import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError

    D = (b ** 2) - (4 * a * c)

    if D < 0:
        result = None
    elif D == 0:
        x1 = (b - b - b + (D ** 0.5)) / (2 * a)
        result = x1
    else:
        x1 = (b - b - b + (D ** 0.5)) / (2 * a)
        x2 = (b - b - b - (D ** 0.5)) / (2 * a)
        result = (x1, x2)
    return result


class QuadraticEquationTest(unittest.TestCase):

    def test_with_no_roots(self):
        expected = None
        actual = quadratic_equation(4, 1, 2)
        self.assertEqual(actual, expected)

    def test_with_two_roots(self):
        expected = (0.5, -1.0)
        actual = quadratic_equation(2, 1, -1)
        self.assertEqual(actual, expected)

    def test_with_one_roots(self):
        expected = 2.0
        actual = quadratic_equation(1, -4, 4)
        self.assertEqual(actual, expected)

    def test_zero_error(self):
        self.assertRaises(Exception, quadratic_equation, 0, 1, 2)

    def test_value_error(self):
        self.assertRaises(Exception, quadratic_equation, "0", "123s", 2)