#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        count = len(my_list) * -1
        idx = -1

        if count is None:
            return None

        while count < 0:
                print("{:d}".format(my_list[idx]))
                idx = idx - 1
                count = count + 1
