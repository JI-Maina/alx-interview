#!/usr/bin/python3
"""Defines a function def island_perimeter(grid): that returns the
perimeter of the island described in grid."""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    """
    visit = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))

        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)

        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)

# def island_perimeter(grid):
#    row = len(grid)
#   col = len(grid[0])
#    perimeter = 0
#    for i in range(row):
#        for j in range(col):
#            if grid[i][j] == 0:
#                continue

#            if i == 0 or grid[i-1][j] == 0:
#                perimeter += 1

#            if j == 0 or grid[i][j-1] == 0:
#                perimeter += 1

#            if i == row - 1 or grid[i+1][j] == 0:
#                perimeter += 1

#            if j == col - 1 or grid[i][j+1] == 0:
#                perimeter += 1
#            print(perimeter)

#    return perimeter
