#!/usr/bin/python3
"""
Fetch https://intranet.hbtn.io/status
"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        url = response.read()
        print ("Body response:")
        print ("\t- type: {}".format(type(url)))
        print ("\t- content: {}".format(url))
        print ("\t- utf8 contet: {}".format(url.decode('utf8')))
