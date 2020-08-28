#!/usr/bin/python3
"""
takes in letter ands ends POST request with letter as parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    req = requests.get(url, (username, password))

    print (req.json().get('id'))
