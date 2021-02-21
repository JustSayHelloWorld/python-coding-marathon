"""Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException
Create class TriangleTest with parametrized unittest for class Triangle
test data:
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]
"""

import unittest


class TriangleNotValidArgumentException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f"Not valid arguments"


class TriangleNotExistException(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return f"Can`t create triangle with this arguments"


class Triangle:

    def __init__(self, points):
        try:
            if len(points) != 3:
                raise TypeError
            elif type(points) is not list:
                if type(points) is not tuple:
                    raise TypeError
            self.points = []
            for each in points:
                self.points.append(each + 0)
            self.semi_perimeter = sum(self.points) / 2

            if not self.points[0] < self.points[1] + self.points[2]:
                raise TriangleNotExistException
            elif not self.points[1] < self.points[0] + self.points[2]:
                raise TriangleNotExistException
            elif not self.points[2] < self.points[0] + self.points[1]:
                raise TriangleNotExistException
        except TypeError:
            raise TriangleNotValidArgumentException

    def get_area(self):
        a = self.semi_perimeter - self.points[0]
        b = self.semi_perimeter - self.points[1]
        c = self.semi_perimeter - self.points[2]
        area = (self.semi_perimeter * (a * b * c)) ** 0.5
        return area


class TriangleTest(unittest.TestCase):

    def setUp(self):
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        self.not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]

        self.not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

    def test_area_for_valid_data(self):
        for each in self.valid_test_data:
            points = each[0]
            result = each[1]
        self.assertEqual(Triangle(points).get_area(), result)

    def test_not_valid_triangle(self):
        for each in self.not_valid_triangle:
            self.assertRaises(Exception, Triangle, each)

    def test_not_valid_args(self):
        for each in self.not_valid_arguments:
            self.assertRaises(Exception, Triangle, each)

    def tearDown(self):
        self.not_valid_arguments = None
        self.not_valid_triangle = None
        self.valid_test_data = None



