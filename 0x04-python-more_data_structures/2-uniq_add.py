#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0

    new_list = set(my_list)
    for i in new_list:
        result = result + i
    return result
