"""Create class Worker with fields name and salary. If salary negative raise ValueError

Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next step:

less then 1000 - 0%
1001 - 3000 - 10%
3001 - 5000 - 15%
5001 - 10000 - 21%
10001 - 20000 - 30%
20001 - 50000 - 40%
more than 50000 - 47%
Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. Don`t use assertRaises in tests."""

import unittest


class Worker:

    def init(self, name, salary=0.0):
        self.name = name

        self.salary = salary
        if self.salary < 0:
            raise ValueError('ValueError')

    def get_tax_value(self):

        tax = 0.0
        profit = self.salary

        if profit > 50000:
            tax += ((profit - 50000) * 0.47)
            profit = 50000
        if 2000 < profit <= 50000:
            tax += ((profit - 20000) * 0.4)
            profit = 20000
        if 10000 < profit <= 20000:
            tax += ((profit - 10000) * 0.3)
            profit = 10000
        if 5000 < profit <= 10000:
            tax += ((profit - 5000) * 0.21)
            profit = 5000
        if 3000 < profit <= 5000:
            tax += ((profit - 3000) * 0.15)
            profit = 3000
        if 1000 < profit <= 3000:
            tax += ((profit - 1000) * 0.1)
            profit = 1000
        if profit <= 1000:
            tax += 0.0

        return tax


class WorkerTest(unittest.TestCase):

    def test_check_correct_value(self):
        expected = 0.1
        actual = Worker('Anna', 1001).get_tax_value()
        self.assertEqual(actual, expected)

    @unittest.expectedFailure
    def test_raises(self):
        with self.assertRaises(ValueError) as context:
            Worker('Anna', -1).get_tax_value()
        self.assertFalse('ValueError' in str(context.exception))