"""Create function create_account(user_name: string, password: string, secret_words: list). This function should return inner function check.

The function check compares the values of its arguments with password and secret_words: the password must match completely, secret_words may be misspelled (just one element).

Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,  special character and one number.

Otherwise function create_account raises ValueError.



For example:

tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error



If tom = create_account("Tom", "Qwerty1_", ["1", "word"])

then

tom("Qwerty1_",  ["1", "word"]) return True

tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]

tom("Qwerty1_",  ["word", "12"]) return True

tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

"""


def create_account(user_name, password, secret_words):
    import re
    pass_pattern = "^(?=.*\d)(?=.*[\W_])(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$"

    validation = lambda password: True if re.search(pass_pattern, password) != None else False

    if not validation(password):
        raise ValueError

    def check(*args):

        if args[0] == password and len(args[1]) == len(secret_words):

            check_result = True

            set_of_args = set(args[1])
            set_of_secret = set(secret_words)

            if len(set_of_args) != len(set_of_secret) and len(set_of_args) < len(set_of_secret):
                check_result = False
            elif len(set_of_args - set_of_secret) > 1:

                check_result = False

        elif len(args) != 0:

            check_result = False

        return check_result

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])