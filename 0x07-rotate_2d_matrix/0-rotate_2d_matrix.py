#!/usr/bin/python3
"""Defines a function that rotates a given 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix, 90 degrees clockwise
    """
    rows = len(matrix)
    cols = len(matrix[0])

    c = 0
    r = rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
