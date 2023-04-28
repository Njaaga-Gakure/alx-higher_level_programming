#!/usr/bin/python3
"""Fetch a url using urllib."""


from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        body = res.read()
        utf8_content = body.decode("utf-8")

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {utf8_content}")
