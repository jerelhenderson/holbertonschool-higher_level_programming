#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            num = "Fizz Buzz"
        elif num % 3 == 0:
            num = "Fizz"
        elif num % 5 == 0:
            num = "Buzz"
        print ("{} ".format(num), end="")
