#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0

    with open(filename, encoding="UTF8") as my_file:
        for line in my_file:
            print(line, end="")
            count = count + 1

        if nb_lines <= 0 or nb_lines >= count:
            print(my_file.read(), end="")
            pass
