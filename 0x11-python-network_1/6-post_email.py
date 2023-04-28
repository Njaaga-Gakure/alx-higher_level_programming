#!/usr/bin/python3
"""Use requests library to send a post request."""

import requests
import sys

if __name__ == "__main__":
    print(requests.post(sys.argv[1], {'email': sys.argv[2]}).text)
