#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    r_num = {'I': 1, 'V': 5, 'X': 10,
             'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(roman_string)):
        if i > 0 and r_num[roman_string[i]] > r_num[roman_string[i - 1]]:
            integer += r_num[roman_string[i]]
            integer -= 2 * r_num[roman_string[i - 1]]
        else:
            integer += r_num[roman_string[i]]
    return integer
