#!/usr/bin/python3
def islower(c):
    for letter in range(93, 123):
        if ord(c) == letter:
            return True
    return False
