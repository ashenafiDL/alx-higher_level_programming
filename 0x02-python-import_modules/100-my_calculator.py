#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def main():
    operators = [
            ['+', add],
            ['-', sub],
            ['*', mul],
            ['/', div],
            ]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Availabel operators: +, -, * and /")
        exit(1)
    else:
        i = 0
        for j in operators:
            if argv[2] == operators[i][0]:
                result = operators[i][1](int(argv[1]), int(argv[3]))
                break
            i += 1
        print("{} {} {} = {}".format(
            int(argv[1]),
            argv[2],
            int(argv[3]),
            result))


if __name__ == '__main__':
    main()
