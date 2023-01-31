#!/usr/bin/python3
"""Addition function."""


def add_integer(a, b=98):
    """
    Add integers a and b.

    args:
        a (int): first argument
        b (int): second argument
    Returns:
        the sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
