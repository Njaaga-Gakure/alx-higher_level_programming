#!/usr/bin/python3
"""say_my_name module."""


def say_my_name(first_name, last_name=""):
    """
    Print, My name is <first name> <last name>.

    args:
        first_name (str): first name
        last_name (str): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
