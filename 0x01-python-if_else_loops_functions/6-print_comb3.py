#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if j == 9 and i == j - 1:
            print(f"{i:d}{j:d}")
        else:
            print(f"{i:d}{j:d}, ", end="")
