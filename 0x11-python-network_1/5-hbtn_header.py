#!/usr/bin/python3
"""Use requests library to display value of a header."""

import requests
import sys

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
