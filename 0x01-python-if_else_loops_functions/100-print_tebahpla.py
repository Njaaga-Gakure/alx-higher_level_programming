#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        x = 0
    else:
        x = 32
    print("{}".format(chr(i - x)), end="")
