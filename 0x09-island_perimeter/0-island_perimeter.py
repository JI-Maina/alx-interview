#!/usr/bin/python3
"""Defines a function def island_perimeter(grid): that returns the
perimeter of the island described in grid."""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    """
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                continue

            if i == 0 or grid[i-1][j] == 0:
                perimeter += 1

            if j == 0 or grid[i][j-1] == 0:
                perimeter += 1

            if i == row - 1 or grid[i+1][j] == 0:
                perimeter += 1

            if j == col - 1 or grid[i][j+1] == 0:
                perimeter += 1
            print(perimeter)

    return perimeter
