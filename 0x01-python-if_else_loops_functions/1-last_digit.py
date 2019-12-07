#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = abs(number) % 10

print("Last digit of {} ".format(number), end="")
if number > 0 and last > 5:
    print("is {:d} and is greater than 5".format(last), end="")
elif last == 0:
    print("is 0 and is 0", end="")
elif number < 0 and last < 6 and last != 0:
    print("is -{:d} and is less than 6 and not 0".format(last), end="")
print("")
