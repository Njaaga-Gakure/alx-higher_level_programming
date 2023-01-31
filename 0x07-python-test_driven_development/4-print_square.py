#!/usr/bin/python3
"""print_square module."""


def print_square(size):
    """
    Print a square with the character '#'.

    args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
