#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = 0
    i = -1
    rev_list = []

    while count < len(my_list):
        print("{}".format(my_list[i]))
        rev_list = my_list[i]
        count = count + 1
        i = i - 1
