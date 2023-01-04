#!/usr/bin/python3
def remove_char_at(str, n):
    x = -1
    newStr = ''
    for i in str:
        x = x + 1
        if x == n:
            continue
        else:
            newStr += i
    return (newStr)
