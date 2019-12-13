#!/usr/bin/python3
def max_integer(my_list=[]):
    idx = 0

    if len(my_list) is 0:
        return None
    else:
        biggest = my_list[0]
        while idx < len(my_list):
            if biggest < my_list[idx]:
                biggest = my_list[idx]
            idx = idx + 1

    return biggest
