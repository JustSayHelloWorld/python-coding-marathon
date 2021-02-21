import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    #Student name: OlehKyrychenko
    #email: howtotextme@gmail.com

    def do_GET(self):
        if self.path == "/reset":
            global USERS_LIST
            USERS_LIST = [
                {
                    "id": 1,
                    "username": "theUser",
                    "firstName": "John",
                    "lastName": "James",
                    "email": "john@email.com",
                    "password": "12345",
                }
            ]
            self._set_response(418)
        elif self.path == "/users":
            status = 200
            self._set_response(status, USERS_LIST)
        else:
            data_to_response = None
            user = re.findall(f"\/\w*\/(\w*)", self.path)
            if len(user) > 0:
                for each in USERS_LIST:
                    if user[0] == each["username"]:
                        data_to_response = each
                        status = 200
                        self._set_response(status, data_to_response)
                        pass
                    else:
                        status = 400
                        data_to_response = {"error": "User not found"}
                        self._set_response(status, data_to_response)
            else:
                self._set_response(418)

    def do_POST(self):
        data = self._pars_body()
        data_to_response = None
        if type(data) is dict:
            if self.path == "/user":
                duplicates = 0
                check_data_fields = data.keys() == USERS_LIST[0].keys()
                if check_data_fields:
                    for each in USERS_LIST:
                        if data["id"] == each["id"]:
                            duplicates += 1
                    if duplicates == 0:
                        USERS_LIST.append(data)
                        data_to_response = data
                        status = 201
                    else:
                        data_to_response = {}
                        status = 400
                else:
                    data_to_response = {}
                    status = 400
            self._set_response(status, data_to_response)

        elif type(data) is list:
            if self.path == "/user/createWithList":
                check_data_fields = True
                duplicates = 0

                for each in data:
                    if not each.keys() == USERS_LIST[0].keys():
                        check_data_fields = False

                if check_data_fields:
                    given_data_id_set = set({})
                    existed_data_id_set = set({})

                    for each in data:
                        given_data_id_set.add(each["id"])
                    for each in USERS_LIST:
                        existed_data_id_set.add(each["id"])
                    duplicates = len(given_data_id_set.intersection(existed_data_id_set))

                if check_data_fields and duplicates == 0:
                    data_to_response = data
                    status = 201
                else:
                    data_to_response = {}
                    status = 400
                self._set_response(status, data_to_response)

    def do_PUT(self):
        data = self._pars_body()
        data_to_response = None
        user = re.findall(f"\/\w*\/(\w*)", self.path)
        if len(user) > 0:
            user = user[0]
            for each in USERS_LIST:
                if each["username"] == user:
                    given_data_keys_set = set(data.keys())
                    existed_data_keys_set = set(each.keys())
                    difference = existed_data_keys_set - given_data_keys_set
                    if difference == {"id"}:
                        for el in data.keys():
                            each[el] = data[el]
                        data_to_response = each
                        status = 200
                        pass
                    else:
                        data_to_response = {"error": "not valid request data"}
                        status = 400
                else:
                    data_to_response = {"error": "User not found"}
                    status = 404

        self._set_response(status, data_to_response, )

    def do_DELETE(self):
        data_to_response = None
        user_id = re.findall(f"\/\w*\/(\w*)", self.path)
        if len(user_id) > 0:
            user_id = user_id[0]
            for each in USERS_LIST:
                if each["id"] == int(user_id):
                    USERS_LIST.remove(each)
                    status = 200
                    data_to_response = {}
                else:
                    status = 404
                    data_to_response = {"error": "User not found"}
        self._set_response(status, data_to_response)


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
