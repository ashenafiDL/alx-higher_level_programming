#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv) - 1
    print("{} {}".format(
        n,
        "argument:" if n == 1 else "arguments:" if n > 1 else "arguments."))

    j = 1
    for i in argv[1:]:
        print("{}: {}".format(j, i))
        j += 1


if __name__ == '__main__':
    main()
