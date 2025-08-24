#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def detonate(grid):
    r, c = len(grid), len(grid[0])
    result = [["O"] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "O":
                result[i][j] = "."
                if i > 0: result[i-1][j] = "."
                if i < r-1: result[i+1][j] = "."
                if j > 0: result[i][j-1] = "."
                if j < c-1: result[i][j+1] = "."
    return ["".join(row) for row in result]

def bomberMan(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ["O" * len(grid[0]) for _ in range(len(grid))]

    # First detonation (after t = 3)
    first = detonate(grid)
    if n % 4 == 3:
        return first
    
    # Second detonation (after t = 5)
    second = detonate(first)
    return second
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
