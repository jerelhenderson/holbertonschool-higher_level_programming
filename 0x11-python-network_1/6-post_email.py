#!/usr/bin/python3
"""sends POST req to a URL w email as param, displays body of response"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
