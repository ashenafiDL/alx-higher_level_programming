#!/usr/bin/python3
def print_last_digit(number) -> int:
    if number >= 0:
        last = number % 10
    else:
        last = (number * -1) % 10
    print(f"{last:d}", end="")
    return (last)
