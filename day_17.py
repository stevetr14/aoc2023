import sys
from pprint import pprint

from utils import parse_input


def min_path(x: int, y: int, z: int) -> int:
    if x < y:
        return x if (x < z) else z
    else:
        return y if (y < z) else z


def min_cost(matrix: list[list[int]], m: int, n: int, col_size: int, row_size: int) -> int:
    tc = [[0 for x in range(col_size)] for x in range(row_size)]

    tc[0][0] = matrix[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + matrix[i][0]

    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + matrix[0][j]

    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j],
                           tc[i][j - 1]) + matrix[i][j]

    return tc[m][n]


def part_one():
    lines = parse_input("test.txt")
    total = 0

    row_size = len(lines)
    col_size = len(lines[0])

    matrix = [[int(c) for c in line] for line in lines]
    # pprint(matrix)

    cost = min_cost(matrix, m=row_size - 1, n=col_size - 1, row_size=row_size, col_size=col_size)

    print(cost)

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 3: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
