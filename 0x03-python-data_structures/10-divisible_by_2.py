#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list

    for itr in range(len(my_list)):
        if itr % 2 is 0:
            new_list.append(True)
        else:
            if itr % 2 is not 0:
                new_list.append(False)
    return new_list
