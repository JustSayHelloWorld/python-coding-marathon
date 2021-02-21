"""As input data, you have a list of strings.

Write a method double_string() for counting the number of strings from
the list, represented in the form of the concatenation of two strings from this arguments  list"""


def double_string(data):
    counter = 0
    for string in data:
        if "{}".format(string * 2) in data:
            counter += 1
    return counter
