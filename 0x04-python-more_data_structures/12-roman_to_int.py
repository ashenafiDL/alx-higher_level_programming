#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
    }
    res = 0
    i = 0

    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman[roman_string[i + 1]] > roman[roman_string[i]]:
            res += roman[roman_string[i + 1]] - roman[roman_string[i]]
            i += 2
        else:
            res += roman[roman_string[i]]
            i += 1
    return res
