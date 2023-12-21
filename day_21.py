from collections import Counter
from itertools import pairwise

from utils import parse_input


def mark_garden_plots(
    matrix: list[list[str]], tracked_positions: list[tuple[int, int]],
) -> tuple[list[list[str]], list[tuple[int, int]]]:
    new_tracked_positions = []
    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if (x, y) in tracked_positions:
                matrix[y][x] = "."

                if x < len(row) - 1 and matrix[y][x + 1] != "#":
                    matrix[y][x + 1] = "O"
                    new_tracked_positions.append((x + 1, y))
                if x > 0 and matrix[y][x - 1] != "#":
                    matrix[y][x - 1] = "O"
                    new_tracked_positions.append((x - 1, y))
                if y < len(matrix) - 1 and matrix[y + 1][x] != "#":
                    matrix[y + 1][x] = "O"
                    new_tracked_positions.append((x, y + 1))
                if y > 0 and matrix[y - 1][x] != "#":
                    matrix[y - 1][x] = "O"
                    new_tracked_positions.append((x, y - 1))

    return matrix, new_tracked_positions


def part_one():
    lines = parse_input("day_21.txt")
    matrix = [list(line) for line in lines]

    tracked_positions = []

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                tracked_positions.append((j, i))
                break

    matrix, tracked_positions = mark_garden_plots(matrix, tracked_positions)
    total = 0
    steps = 1

    while steps != 64:
        matrix, tracked_positions = mark_garden_plots(matrix, tracked_positions)
        steps += 1

    for row in matrix:
        print("".join(row))
        total += Counter(row)["O"]

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    matrix = [list(line) for line in lines]

    total = 0
    tracked_positions = []

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                tracked_positions.append((j, i))
                break

    matrix, tracked_positions = mark_garden_plots(matrix, tracked_positions)
    steps = 1

    a = []
    indices = []

    for i in range(2, 121):
        test = 0

        while steps != i:
            matrix, tracked_positions = mark_garden_plots(matrix, tracked_positions)
            steps += 1

        for row in matrix:
            if i == 100:
                print("".join(row))
            test += Counter(row)["O"]

        a.append(test)
        indices.append(i)
        # print(i, "-", test)

    b = [j - i for i, j in pairwise(a)]
    print(a)
    print(indices)
    print(b)

    # print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
