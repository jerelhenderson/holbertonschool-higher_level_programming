#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0

    new_list = set(my_list)
    for i in range(len(new_list) + 1):
        result = result + i
    return result
