#!/usr/bin/python3
"""Send a letter as a parameter during a POST request."""

import requests
import sys

if __name__ == "__main__":
    q = ""
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        q = sys.argv[1]

    res = requests.post(url, data={'q': q})

    if res.headers.get('content-type') == 'application/json':
        if (res.json()):
            print(f"[{res.json().get('id')}] {res.json().get('name')}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
