#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    itr = 0

    my_list.sort()
    for row in range(len(my_list) - 1):
        if my_list[itr] == my_list[itr + 1]:
            itr = itr + 1
        else:
            new_list.append(my_list[itr])
            itr = itr + 1
    new_list.append(my_list[itr])

    result = sum(new_list)

    return result
