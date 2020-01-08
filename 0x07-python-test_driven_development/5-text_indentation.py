#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char is "." or char is "?" or char is ":":
            print("\n")
