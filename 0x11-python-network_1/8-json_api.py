#!/usr/bin/python3
"""
takes in letter ands ends POST request with letter as parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = argv[1]

    if len(argv[1]) == 0:
        q = ""

    data = {'q': q}
    req = requests.post(url, data)

    try:
        if 'id' in req and 'name' in req:
            print ("[{}]".format(req['id']))
        else:
            print ("No result")
    except ValueError:
        print ("Not a valid JSON")
