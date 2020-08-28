#!/usr/bin/python3
"""
takes in letter ands ends POST request with letter as parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://swapi.co/api/people/1/"

    data = {'search': argv[1]}
    req = requests.get(url, data)

    req_dict = req.json()
    print ("Number of results: {}".format(req_dict.get('count')))
    for result in req_dict.get("results"):
        print (result.get("name"))
