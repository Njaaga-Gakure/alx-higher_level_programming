#!/usr/bin/python3
"""matrix_divided module."""


def matrix_divided(matrix, div):
    """
    Return a new matrix with its elements divided by div.

    args:
        matrix: the matrix to be divided
        div: the number to divide the matrix
    Returns:
        the divided matrix

    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for i in range(0, len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        elif len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(0, len(matrix[i])):
            if not isinstance(matrix[i][j], int)\
                    and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    return (list(map(lambda i:
            list(map(lambda j: round(j / div, 2), i)), matrix)))
