#!/usr/bin/python3
"""Defines a function that returns a pascal triangles of `n`"""


def pascal_triangle(n) -> list:
    """returns a pascal triangles of siz `n`

    Args:
        n (int): the size of triangle

    Returns:
        list: pascal's triangle
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j] + triangle[i-1][j-1])
        triangle.append(row)

    return triangle
