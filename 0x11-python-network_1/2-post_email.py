#!/usr/bin/python3
"""Send a POST request with an email as a parameter."""


from urllib import request, parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
