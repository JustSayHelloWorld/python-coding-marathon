"""Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name") by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it).


If the function cannot find input files we need to log information with error level

root - ERROR - File <file name> doesn't exists

For example:
user1.json :
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
]

user2.json :
[{"name": "Bob1", "rate": 25, “languages": ["French"]},
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]

If we execute parse_user(user3.json, user1.json, user2.json)
then file user3.json should contain information:
[{"name": "Bob1", "rate": 1, “languages": ["English"]},
{"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
{"name": "Bob3", "rate": 78, "languages": ["Germany"]}
]"""

import json

def parse_user(output_file, *args):
    data = []

    for each in args:
        json = unpack_json(each)
        if json != None:
            for el in json:
                if "name" in el.keys():
                    repeated = 0
                    if len(data) > 0:
                        for each in data:
                            if el["name"] == each["name"]:
                                repeated += 1
                    if repeated == 0:
                        data.append(el)
    create_json(output_file, data)


def unpack_json(file):
    import logging
    import json
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    try:
        with open(file) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f"File {file} doesn't exists")


def create_json(file, data):
    import json

    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4)

    return file