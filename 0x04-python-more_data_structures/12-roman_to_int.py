#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    hold = ""

    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    for roman_num in roman_string:
        for val in roman:
            if roman_num == "I":
                hold = roman_num
            if val == roman_num:
                sum = sum + roman[val]
                if roman_num == "X" or roman_num == "V":
                    if hold == "I":
                        sum = sum - 2
    return sum
