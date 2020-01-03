#!/usr/bin/python3
def safe_print_list(value=[], x=0):
    try:
        for elem in range(x):
            print("{:d}".format(value[elem]), end="")
        print("")
        return(elem + 1)
    except:
        print("")

    return(elem)
