#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number *= -1

last = number % 10

print("Last digit of {} ".format(number), end="")
print("is {} ".format(last), end="")
if last > 5:
    print("and is greater than 5", end="")
elif last == 0:
    print("and is 0", end="")
elif (last < 6) and (last != 0):
    print("and is less than 6 and not 0", end="")
print("")
