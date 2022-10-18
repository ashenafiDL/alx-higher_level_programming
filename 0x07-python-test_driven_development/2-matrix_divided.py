#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div) -> list:
    """Divides all the elements of the matrix by div

    Args:
        matrix (list): list of lists containig integers or floats(matrix)
        div (int/float): the denomenator number

    Returns:
        list: a new matrix after the division
    """
    if (not isinstance(matrix, list)
        or not isinstance(matrix[0], list)
            or not isinstance(matrix[1], list)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        sub_matrix = []
        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
                        of integers/floats")
            sub_matrix.append(round(n / div, ndigits=2))
        new_matrix.append(sub_matrix)

    return new_matrix
