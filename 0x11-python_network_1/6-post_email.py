#!/usr/bin/python3
"""
takes URL and email, sends POST request to passed URL w/ email as parameter and
display response body
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email]': sys.argv[2]}
    data = parse.urlencode(email)
    req = request.urlopen.Request.read()
    print(response.decode("utf8"))
