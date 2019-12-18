#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    temp = 0
    chars = len(my_string)

    while idx < chars:
        if my_string[idx] != "c" and my_string[idx] != "C":
            idx = idx + 1
        else:
            new_string = my_string[temp:idx]
            temp = idx + 1
            idx = idx + 1
    return(new_string + my_string[temp:])
