#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    C = ord("C")

    for i in my_string:
        if i != "C" and i != "c":
            new_string = new_string + i
    return new_string
