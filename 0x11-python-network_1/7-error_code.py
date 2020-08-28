#!/usr/bin/python3
"""requests URL and displays body; display HTTP status code"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code > 399:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)
