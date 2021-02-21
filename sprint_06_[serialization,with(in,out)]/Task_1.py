"""Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find("3.json", "password") returns ["1234qweQWE"]"""


def find(file, key):
    data = unpack_json(file)
    result = []

    if type(data) is list:
        for each in data:
            if key in each.keys():
                if type(each[key]) is not list and each[key] not in result:
                    result.append(each[key])
                else:
                    for el in each[key]:
                        if el not in result:
                            result.append(el)
    else:
        if key in data.keys():
            if type(data[key]) is not list and data[key] not in result:
                result.append(data[key])
            else:
                for el in data[key]:
                    if el not in result:
                        result.append(el)

    return result


def unpack_json(file):
    import json

    with open(file) as json_file:
        data = json.load(json_file)
        return data