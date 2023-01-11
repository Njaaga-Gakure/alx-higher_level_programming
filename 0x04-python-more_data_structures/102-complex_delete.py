#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    a_dictionary_cpy = {i: a_dictionary[i] for i in keys}
    for i in a_dictionary_cpy:
        if a_dictionary[i] == value:
            a_dictionary.pop(i, 0)
    return (a_dictionary)
