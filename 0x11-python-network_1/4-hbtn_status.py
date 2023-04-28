#!/usr/bin/python3
"""Fetch using requests."""


import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
