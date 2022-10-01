#!/usr/bin/python3
def roman_to_int(roman_string):
    n = len(roman_string)
    r = {
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

    if isinstance(roman_string, str):
        while i < n:
            if i < n - 1 and r[roman_string[i + 1]] > r[roman_string[i]]:
                res += r[roman_string[i + 1]] - r[roman_string[i]]
                i += 2
            else:
                res += r[roman_string[i]]
                i += 1
    return res
