"""In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],

in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...].

Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:

header line - user, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception

To validate instances create function validate_json(data, schema)"""

import json
import jsonschema
import csv


def unpack_json(file):
    import json

    with open(file) as json_file:
        data = json.load(json_file)
        return data


def validate_json(data, schema, data_type):
    from jsonschema import validate
    try:
        validate(data, schema)

    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(data_type)


def user_with_department(csv_file, user_json, department_json):
    schema_user = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["department_id", "name", "id"]
    }

    schema_dep = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["name", "id"]
    }

    user_data = unpack_json(user_json)
    department_data = unpack_json(department_json)
    try:
        with open(csv_file, mode="w") as csv_result:
            headers = {"name": None, "department": None}
            writer = csv.writer(csv_result, delimiter=",")
            writer.writerow(headers.keys())
            for each in user_data:

                validate_json(each, schema_user, "user")

                headers["name"] = each["name"]
                dep_id = each["department_id"]
                dep_id_check = False
                for el in department_data:
                    validate_json(el, schema_dep, "department")

                    if el["id"] == dep_id:
                        headers["department"] = el["name"]
                        writer.writerow(headers.values())
                        dep_id_check = True
                if not dep_id_check:
                    raise DepartmentName(dep_id)
    except DepartmentName as e:
        print(e)
    except InvalidInstanceError as b:
        print(b)


class DepartmentName(Exception):

    def __init__(self, dep_id):
        self.dep_id = dep_id

    def __str__(self):
        return f"Department with id {self.dep_id} doesn't exists"


class InvalidInstanceError(Exception):

    def __init__(self, data_type):
        self.data_type = data_type

    def __str__(self):
        return f"Error in {self.data_type} schema"






