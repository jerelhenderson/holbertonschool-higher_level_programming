#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    args = len(argv)
    i = 1
    sum = 0

    if args == 1:
        print(0)
    else:
        while i < args:
            sum = sum + int(argv[i])
            i = i + 1
        print(sum)
