#!/usr/bin/python3
"""text_indentation module."""


def text_indentation(text):
    """
    Print a text with 2 new lines after '.', '?' and ':'.

    args:
        text (string): string argument
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_list = []
    my_list[:0] = text.strip(' ')

    char = ['.', '?', ':']
    for i in range(0, len(my_list)):
        print(my_list[i], end="")
        for j in range(0, len(char)):
            if my_list[i] == char[j]:
                print("")
                print("")
                if (i != len(my_list) - 1):
                    if (my_list[i + 1] == " "):
                        my_list[i + 1] = ""
