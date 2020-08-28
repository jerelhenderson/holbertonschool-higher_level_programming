#!/usr/bin/python3
"""
takes in letter ands ends POST request with letter as parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(argv[1]) == 0:
        q = ""
    else:
        q = argv[1]

    data = {'q': q}
    req = requests.post(url, data)

    try:
        req_dict = req.json()
        if 'id' in req_dict and 'name' in req_dict:
            print ("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
        else:
            print ("No result")
    except ValueError:
        print ("Not a valid JSON")
