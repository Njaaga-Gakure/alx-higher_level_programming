#!/usr/bin/python3
"""Send request and display body of response."""


from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as error:
        print(f"Error code: {error.code}")
