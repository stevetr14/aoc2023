from pprint import pprint

from utils import parse_input


LEFT_RIGHT = ["<", ">"]
UP_DOWN = ["^", "v"]


def rotate_direction_90_left(direction: str) -> str:
    match direction:
        case "^":
            return "<"
        case ">":
            return "^"
        case "<":
            return "v"
        case "v":
            return ">"


def rotate_direction_90_right(direction: str) -> str:
    match direction:
        case "^":
            return ">"
        case ">":
            return "v"
        case "<":
            return "^"
        case "v":
            return "<"


def part_one():
    lines = parse_input("test.txt")
    count = 0

    direction = ">"

    col_size = len(lines[0])
    row_size = len(lines)

    matrix = [[" " for i in range(col_size)] for j in range(row_size)]

    # pprint(matrix)
    next_position = (0, 0)

    while count < 20:
        i, j = next_position
        char = lines[j][i]

        match char:
            case ".":
                if direction == ">":
                    for x in range(i, col_size):
                        if lines[j][x] == ".":
                            matrix[j][x] = direction
                            count += 1
                        else:
                            next_position = (x, j)
                            break
                elif direction == "<":
                    for x in range(i, 0, -1):
                        if lines[j][x] == ".":
                            matrix[j][x] = direction
                            count += 1
                        else:
                            next_position = (x, j)
                            break
            case "|":
                matrix[j][i] = "|"
                if direction in LEFT_RIGHT:
                    # Going down
                    for y in range(j + 1, row_size):
                        if lines[y][i] == ".":
                            matrix[y][i] = "v"
                            count += 1
                        else:
                            next_position = (i, y)
                            direction = "v"
                            break
                    # Going up
                    for y in range(j - 1, 0, -1):
                        if lines[y][i] == ".":
                            matrix[y][i] = "^"
                            count += 1
                        else:
                            next_position = (i, y)
                            direction = "^"
                            break
            case "-":
                matrix[j][i] = "-"
                if direction in UP_DOWN:
                    # Going right
                    for x in range(i + 1, row_size):
                        if lines[j][x] == ".":
                            matrix[j][x] = ">"
                            count += 1
                        else:
                            next_position = (x, j)
                            break
                    # Going left
                    for x in range(i - 1, 0, -1):
                        if lines[j][x] == ".":
                            matrix[j][x] = "<"
                            count += 1
                        else:
                            next_position = (x, j)
                            break

            case _:
                count += 1

    pprint(matrix)

    print("Part 1: ", count)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 3: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
