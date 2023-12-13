import itertools
import math
import re
from collections import Counter
from pprint import pprint

from utils import parse_input


def get_starting_point(rows: list[str]) -> tuple[int, int]:
    for y, line in enumerate(rows):
        if "S" not in line:
            continue

        for x, char in enumerate(line):
            if char == "S":
                return x, y

    return 0, 0


def is_top_path_valid(current_pipe_: str, next_pipe_: str) -> bool:
    # Check if current pip is blocking top.
    if current_pipe_ in "-7F.":
        return False

    # Pipes that can connect to the given x, y coordinate from the top.
    return next_pipe_ in "|7F"


def is_bottom_path_valid(current_pipe_: str, next_pipe_: str) -> bool:
    # Check if current pip is blocking bottom.
    if current_pipe_ in "-LJ.":
        return False

    # Pipes that can connect to the given x, y coordinate from the bottom.
    return next_pipe_ in "|LJ"


def is_left_path_valid(current_pipe_: str, next_pipe_: str) -> bool:
    # Check if current pip is blocking left.
    if current_pipe_ in "|LF.":
        return False

    # Pipes that can connect to the given x, y coordinate from the left.
    return next_pipe_ in "-LF"


def is_right_path_valid(current_pipe_: str, next_pipe_: str) -> bool:
    # Check if current pip is blocking right.
    if current_pipe_ in "|7J.":
        return False

    # Pipes that can connect to the given x, y coordinate from the right.
    return next_pipe_ in "-7J"


def part_one():
    lines = parse_input("day_10.txt")

    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    x, y = get_starting_point(lines)
    steps = 0

    seen = []
    is_loop_closed = False

    while not is_loop_closed:
        current_pipe = lines[y][x]

        # Reset next point, any valid path should change this to be not None.
        next_point = None

        if is_top_path_valid(current_pipe, lines[y - 1][x]) and (x, y - 1) not in seen:
            next_point = lines[y - 1][x]
            # Go up
            y -= 1
            steps += 1
        elif x < max_x and is_right_path_valid(current_pipe, lines[y][x + 1]) and (x + 1, y) not in seen:
            next_point = lines[y][x + 1]
            # Go right
            x += 1
            steps += 1
        elif y < max_y and is_bottom_path_valid(current_pipe, lines[y + 1][x]) and (x, y + 1) not in seen:
            next_point = lines[y + 1][x]
            # Go down
            y += 1
            steps += 1
        elif is_left_path_valid(current_pipe, lines[y][x - 1]) and (x - 1, y) not in seen:
            next_point = lines[y][x - 1]
            # Go left
            x -= 1
            steps += 1

        # If there is more valid path, that means we hit the starting point "S" again. Add 1 step and end the loop.
        if next_point is None:
            steps += 1
            is_loop_closed = True

        seen.append((x, y))
        print(f"At point {x}-{y} {lines[y][x]}")

    # Floor to handle odd number? (not sure if that would ever happen)
    print(math.floor(steps / 2))


def part_two():
    lines = parse_input("test.txt")

    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    x, y = get_starting_point(lines)
    steps = 0

    seen = []
    is_loop_closed = False

    while not is_loop_closed:
        current_pipe = lines[y][x]

        # Reset next point, any valid path should change this to be not None.
        next_point = None

        if is_top_path_valid(current_pipe, lines[y - 1][x]) and (x, y - 1) not in seen:
            next_point = lines[y - 1][x]
            # Go up
            y -= 1
            steps += 1
        elif x < max_x and is_right_path_valid(current_pipe, lines[y][x + 1]) and (x + 1, y) not in seen:
            next_point = lines[y][x + 1]
            # Go right
            x += 1
            steps += 1
        elif y < max_y and is_bottom_path_valid(current_pipe, lines[y + 1][x]) and (x, y + 1) not in seen:
            next_point = lines[y + 1][x]
            # Go down
            y += 1
            steps += 1
        elif is_left_path_valid(current_pipe, lines[y][x - 1]) and (x - 1, y) not in seen:
            next_point = lines[y][x - 1]
            # Go left
            x -= 1
            steps += 1

        # If there is more valid path, that means we hit the starting point "S" again. Add 1 step and end the loop.
        if next_point is None:
            steps += 1
            is_loop_closed = True
            seen.append(get_starting_point(lines))

        seen.append((x, y))

    count = 0
    for y, line in enumerate(lines):
        row = ""
        for x, char in enumerate(line):
            if (x, y) in seen:
                row += "-"
            else:
                row += "o"

        test_1 = list(re.findall(r"-(o+)-", row))
        test_2 = [len(item) for item in re.findall(r"-+", row)]
        test_3 = list(zip(test_1, list(itertools.pairwise(test_2))))

        for item in test_3:
            mark, walls = item
            if any(n % 2 == 1 for n in walls):
                print(row, len(mark))
                count += len(mark)

    print(count)


if __name__ == "__main__":
    # part_one()
    part_two()
