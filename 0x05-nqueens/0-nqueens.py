#!/usr/bin/python3
import sys


"""solves the N queens problem"""
if len(sys.argv) <= 1:
    print("Usage: nqueens N")
    sys.exit(1)


try:
    int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

n = int(sys.argv[1])
board = [[i, j] for i in range(n) for j in range(n)]

print(board)
