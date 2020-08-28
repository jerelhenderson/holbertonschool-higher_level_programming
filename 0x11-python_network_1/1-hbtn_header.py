#!/usr/bin/python3
"""
take and send to URL and display value of `X-Request-Id`
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
