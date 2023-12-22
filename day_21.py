from collections import Counter

from utils import parse_input


def get_marked_plots(
    matrix: list[list[str]],
    tracked_positions: set[tuple[int, int]],
    max_x: int,
    max_y: int,
) -> tuple[list[list[str]], set[tuple[int, int]]]:
    new_tracked_positions = set()

    for position in tracked_positions:
        x, y = position

        # Wrap around using mod on the matrix
        if matrix[y % max_y][(x + 1) % max_x] != "#":
            new_tracked_positions.add((x + 1, y))
        if matrix[y % max_y][(x - 1) % max_x] != "#":
            new_tracked_positions.add((x - 1, y))
        if matrix[(y + 1) % max_y][x % max_y] != "#":
            new_tracked_positions.add((x, y + 1))
        if matrix[(y - 1) % max_y][x % max_y] != "#":
            new_tracked_positions.add((x, y - 1))

    return matrix, new_tracked_positions


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
    lines = parse_input("day_21.txt")
    matrix = [list(line) for line in lines]

    max_length = len(matrix)
    starting_index = int(max_length / 2)

    total = 0

    # S always starts at the center
    tracked_positions = {(starting_index, starting_index)}

    matrix, tracked_positions = get_marked_plots(matrix, tracked_positions, max_length, max_length)
    steps = 1

    a = []

    for i in range(2, 64):
        while steps != i:
            matrix, tracked_positions = get_marked_plots(matrix, tracked_positions, max_length, max_length)
            steps += 1

            print(i, len(tracked_positions))
            a.append(len(tracked_positions))

    for item in tracked_positions:
        x, y = item
        matrix[y][x] = "O"

    for row in matrix:
        print("".join(row))

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
