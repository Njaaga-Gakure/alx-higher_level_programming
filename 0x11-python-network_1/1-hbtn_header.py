#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable."""


from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info().get('X-Request-Id'))
