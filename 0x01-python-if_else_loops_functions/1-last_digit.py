#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)


def sign(n) -> str:
    if n > 5:
        return 'and is greater than 5'
    elif n == 0:
        return 'and is 0'
    else:
        return 'and is less than 6 and not 0'


def last(n) -> int:
    if n >= 0:
        return n % 10
    else:
        return -((n * -1) % 10)


print(f"Last digit of {number:d} is {last(number):d} {sign(last(number))}")
