#!/usr/bin/python3
"""
take and send to URL and display value of `X-Request-Id`
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-ID"))
