import math

from shapely import polygons, Point

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


def get_closed_loop_points(lines: list[str]) -> tuple[int, list[tuple[int, int]]]:
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

    return steps, seen


def part_one():
    lines = parse_input("day_10.txt")

    steps, seen = get_closed_loop_points(lines)

    # Floor to handle odd number? (not sure if that would ever happen)
    print("Part 1: ", math.floor(steps / 2))


def part_two():
    lines = parse_input("day_10.txt")

    _, seen = get_closed_loop_points(lines)
    polygon = polygons(seen)
    count = 0

    for y, line in enumerate(lines):
        row = ""
        for x, char in enumerate(line):
            if (x, y) in seen:
                row += "-"
            elif polygon.contains(Point(x, y)):
                row += "I"
                count += 1
            else:
                row += "O"
        print(row)

    print("Part 2: ", count)


if __name__ == "__main__":
    # part_one()
    part_two()
