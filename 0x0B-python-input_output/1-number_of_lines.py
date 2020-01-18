#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0

    with open(filename, encoding="UTF8") as my_file:
        for line in my_file:
            count = count + 1
    return(count)
