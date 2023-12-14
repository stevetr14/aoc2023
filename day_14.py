import time

from utils import parse_input, transpose_list, rotate_matrix_90_anti_clockwise, rotate_matrix_90_clockwise


def part_one():
    lines = parse_input("test.txt")
    total = 0

    for line in transpose_list(lines):
        col_length = len(line)

        new_line = shuffle(line)
        print(new_line)

        for i, c in enumerate(new_line):
            if c == "O":
                total += col_length - i

    print("Part 1: ", total)


def cycle(matrix: list[any]) -> list[any]:
    north = rotate_matrix_90_anti_clockwise(matrix)
    for i, line in enumerate(north):
        north[i] = shuffle(line)

    east = rotate_matrix_90_clockwise(north)
    for i, line in enumerate(east):
        east[i] = shuffle(line)

    south = rotate_matrix_90_clockwise(east)
    for i, line in enumerate(south):
        south[i] = shuffle(line)

    west = rotate_matrix_90_clockwise(south)
    for i, line in enumerate(west):
        west[i] = shuffle(line)

    normal_view = rotate_matrix_90_clockwise(rotate_matrix_90_clockwise(west))

    return normal_view


def shuffle(input_: list[any]) -> list[any]:
    col_length = len(input_)
    old_line = input_.copy()

    for i in range(col_length - 1):
        if input_[i] == "." and input_[i + 1] == "O":
            input_[i] = "O"
            input_[i + 1] = "."

    new_line = input_.copy()

    while new_line != old_line:
        old_line = new_line.copy()

        for i in range(col_length - 1):
            if input_[i] == "." and input_[i + 1] == "O":
                input_[i] = "O"
                input_[i + 1] = "."

        new_line = input_.copy()

    return new_line


def part_two():
    lines = parse_input("day_14.txt")

    total = 0

    cycle_count = 1
    cycle_num = 1_000  # Somehow the answer converges to about this many cycles lol

    start = time.time()

    # You spin my head right round, right round...
    cycled_matrix = cycle(lines)
    while cycle_count < cycle_num:
        cycled_matrix = cycle(cycled_matrix)
        cycle_count += 1

    for line in rotate_matrix_90_anti_clockwise(cycled_matrix):
        col_length = len(line)
        for i, c in enumerate(line):
            if c == "O":
                total += col_length - i

    end = time.time()

    print("Part 2: ", total, end - start)


if __name__ == "__main__":
    # part_one()
    part_two()
