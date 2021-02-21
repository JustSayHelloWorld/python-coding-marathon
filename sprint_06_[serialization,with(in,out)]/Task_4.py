"""Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.

Make both classes JSON serializable.

Json-files represent information about student (students).

Create methods:

Student.from_json(json_file) that return Student instance from attributes from json-file;

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension)."""


import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, jsonfile):
        with open(jsonfile) as jsonfile:
            data = json.load(jsonfile)
            return cls(data["full_name"], data["avg_rank"], data["courses"])

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students
        if type(self.students) is dict:
            self.students = [students]

    def __str__(self):
        list_of_stud = []
        if type(self.students) is list:
            for each in self.students:
                fullname = each["full_name"]
                avgrank = each["avg_rank"]
                courses = each["courses"]
                list_of_stud.append(f"{fullname} ({avgrank}): {courses}")
        else:
            fullname = self.students["full_name"]
            avgrank = self.students["avg_rank"]
            courses = self.students["courses"]
            list_of_stud.append(f"{fullname} ({avgrank}): {courses}")

        return f"{self.title}: {list_of_stud}"

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, "a") as f:
            list_to_dump = []
            for each in list_of_groups:
                group_info = each.__dict__
                list_to_dump.append({'title': group_info["title"], 'students': group_info["students"]})
            json.dump(list_to_dump, f)

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as group_file:
            data = json.load(group_file)

            return cls(group_file.name[:-5], data)


