#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        if i < 8:
            print("{0}{1}".format(i, j), end=", ")
        else:
            print("{}".format(i), end="")
            print("{}".format(j))
