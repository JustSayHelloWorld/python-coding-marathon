"""The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral"""

import re


def figure_perimetr(data):
    coordinates_dict = {}
    p = 0

    for coordinate in re.findall(r'\w{2}\d:\d', data):
        point_name = re.findall(r'\w{2}', coordinate)[0]
        point = re.findall(r'\d', coordinate)
        coordinates_dict[point_name] = point

    keys = coordinates_dict.keys()
    opposite_point = ""

    for key in keys:
        if key == "LB":
            opposite_point = "RB"
        elif key == "LT":
            opposite_point = "RT"
        elif key == "RB":
            opposite_point = "RT"
        else:
            key = "LB"
            opposite_point = "LT"

        xy1 = coordinates_dict.get(key)
        xy2 = coordinates_dict.get(opposite_point)

        p += ((int(xy2[0]) - int(xy1[0])) ** 2 + (int(xy2[1]) - int(xy1[1])) ** 2) ** 0.5

    return p