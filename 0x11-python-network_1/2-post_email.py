#!/usr/bin/python3
"""
takes URL and email, sends POST request to passed URL w/ email as parameter and
display response body
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    resp = request.urlopen(req).read()
    print(resp.decode("utf8"))
