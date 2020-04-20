#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0
    for roman_num in roman_string:
        for val in roman:
            if val == roman_num:
                sum = sum + roman[val]
                break
    return sum
