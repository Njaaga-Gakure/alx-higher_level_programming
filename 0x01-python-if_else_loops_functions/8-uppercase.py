#!/usr/bin/python3
def uppercase(str):
    upperStr = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            char = chr(ord(i) - 32)
        else:
            char = i
        upperStr += char
    print("{}".format(upperStr))
