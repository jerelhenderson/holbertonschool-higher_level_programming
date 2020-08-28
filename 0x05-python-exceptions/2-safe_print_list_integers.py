#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0

    while i < x:
        try:
            isnum = my_list[i]
            if type(isnum) is int:
                print("{}".format(my_list[i]), end="")
                count = count + 1
            i = i + 1
        except:
            pass
    print("")
    return count
