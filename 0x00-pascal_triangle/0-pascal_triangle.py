#!/usr/bin/python3
"""Given a number n, pascal_triangle() returns a list of lists of integers
    representing the Pascal’s triangle of n.
"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    of n"""
    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []

        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        triangle.append(row)

    return triangle
