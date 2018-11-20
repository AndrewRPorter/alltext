import re
from functools import partial


def format(operation, text):
    if operation not in operations:
        return ""

    return execute(partial(operations[operation], text))


def execute(operation):
    return operation()


def tabs_to_spaces(data: str):
    return data.replace("\t", " " * 4)


def remove_spaces(data: str):
    print('here')
    return data.replace(" ", "")


def remove_whitespace(data: str):
    """
        Removes all white space characaters in a string according to
        https://infohost.nmt.edu/tcc/help/pubs/python/web/whitespace.html
    """
    for char in [" ", "\n", "\r", "\t", "\f", "\v"]:
        data = data.replace(char, "")
    return data


def reverse(data: str):
    return data[::-1]


operations = {
    "tabs_to_spaces": tabs_to_spaces,
    "remove_spaces": remove_spaces,
    "remove_whitespace": remove_whitespace,
    "reverse": reverse,
}
