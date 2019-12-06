#!/usr/bin/python3
itr1 = 0
itr2 = 1

while itr1 in range(0, 8):
    while itr2 in range(0, 9):
            print("{}{}".format(itr1, itr2), end="")
            print(", ", end="")
            itr1 += 1
            itr2 += 1
print("")
