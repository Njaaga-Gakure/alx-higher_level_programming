#!/usr/bin/python3
"""Display your id using  GitHub API."""


import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get('id'))
