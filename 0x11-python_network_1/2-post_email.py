#!/usr/bin/python3
"""
take and send request to URL and display body of response
"""
from urllib import request, parse
from urllib import error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf8"))
    except urllib.error.HTTPerror as error:
        print("Error code: {}".format(error.code))
