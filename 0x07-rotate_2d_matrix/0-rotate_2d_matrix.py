#!/usr/bin/python3
"""Defines a function that rotates a given 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix, 90 degrees clockwise
    """

    ln = len(matrix)
    x = y = matrix[ln - 1][0]

    for i in range(ln):
        x = y + i
        for j in range(ln):
            matrix[i][j] = x
            x = x - ln

    return matrix
