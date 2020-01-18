#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="UTF8") as my_file:
        for line in my_file:
            print(line, end="")
