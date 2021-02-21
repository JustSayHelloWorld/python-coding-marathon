"""Create function create with one string argument. This function should return anonymous function that checks if the argument of function is equals to the argument of outer function.



For example:

 tom = create("pass_for_Tom")

 tom("pass_for_Tom") returns true

 tom("pass_for_tom") returns false"""


def create(string):
    return lambda user_input: True if string == user_input else False