#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = dict()

    for row in my_dict:
        new_dict[row] = my_dict[row] * 2
    return new_dict
