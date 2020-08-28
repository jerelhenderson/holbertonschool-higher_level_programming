#!/usr/bin/python3
"""
takes URL and email, sends POST request to passed URL w/ email as parameter and
display response body
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode()
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
