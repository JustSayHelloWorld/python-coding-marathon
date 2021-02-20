"""Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type. 
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, fileType).
This function should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String""""

import json
import pickle
from enum import Enum


class SerializeManager:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype
        self.file = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()

    def serialize(self, object_to_work):
        if self.filetype.value == 1:
            self.file = open(self.filename, 'ab')
            pickle.dump(object_to_work, self.file)
        else:
            self.file = open(self.filename, 'a')
            json.dump(object_to_work, self.file)


class FileType(Enum):
    JSON = 0
    BYTE = 1


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)

