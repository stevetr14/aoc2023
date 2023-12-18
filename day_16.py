from utils import parse_input


class Direction:
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


LEFT_RIGHT = [Direction.LEFT, Direction.RIGHT]
UP_DOWN = [Direction.UP, Direction.DOWN]


def rotate_direction_90_left(direction: str) -> str:
    match direction:
        case Direction.UP:
            return Direction.LEFT
        case Direction.RIGHT:
            return Direction.UP
        case Direction.LEFT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.RIGHT


def rotate_direction_90_right(direction: str) -> str:
    match direction:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.LEFT:
            return Direction.UP
        case Direction.DOWN:
            return Direction.LEFT


def get_next_position(direction: str, x: int, y: int) -> tuple[int, int]:
    match direction:
        case Direction.RIGHT:
            return x + 1, y
        case Direction.LEFT:
            return x - 1, y
        case Direction.DOWN:
            return x, y + 1
        case Direction.UP:
            return x, y - 1


def get_direction_bounced_from_mirror(mirror: str, direction: str) -> str:
    match mirror:
        case "/":
            match direction:
                case Direction.UP | Direction.DOWN:
                    return rotate_direction_90_right(direction)
                case Direction.LEFT | Direction.RIGHT:
                    return rotate_direction_90_left(direction)
        case "\\":
            match direction:
                case Direction.UP | Direction.DOWN:
                    return rotate_direction_90_left(direction)
                case Direction.LEFT | Direction.RIGHT:
                    return rotate_direction_90_right(direction)


def traverse_direction(
    matrix: list[list[str]],
    lines: list[str],
    direction: str,
    starting_position: tuple[int, int],
    tracked: list[tuple[int, int]] | None = None,
) -> list[list[str]]:
    col_size = len(lines[0])
    row_size = len(lines)

    tracked = tracked or []

    next_position = starting_position
    out_of_bound = False
    loop_count = 0

    while not out_of_bound:
        x, y = next_position

        if (x, y) in tracked:
            loop_count += 1

        if x < 0 or y < 0 or x > col_size or y > row_size or loop_count == 1:
            return matrix

        try:
            char = lines[y][x]

            match char:
                case ".":
                    matrix[y][x] = direction
                    next_position = get_next_position(direction, x, y)
                case "|":
                    matrix[y][x] = "|"

                    if direction in LEFT_RIGHT:
                        # Go up
                        tracked.append((x, y))
                        direction = Direction.UP
                        next_position = get_next_position(direction, x, y)
                        matrix = traverse_direction(matrix, lines, direction, next_position, tracked)
                        # tracked.remove((x, y))

                        # Go down
                        tracked.append((x, y))
                        direction = Direction.DOWN
                        next_position = get_next_position(direction, x, y)
                        matrix = traverse_direction(matrix, lines, direction, next_position, tracked)
                        # tracked.remove((x, y))
                    else:
                        next_position = get_next_position(direction, x, y)
                case "-":
                    matrix[y][x] = "-"

                    if direction in UP_DOWN:
                        # Go left
                        tracked.append((x, y))
                        direction = Direction.LEFT
                        next_position = get_next_position(direction, x, y)
                        matrix = traverse_direction(matrix, lines, direction, next_position, tracked)

                        # Go right
                        tracked.append((x, y))
                        direction = Direction.RIGHT
                        next_position = get_next_position(direction, x, y)
                        matrix = traverse_direction(matrix, lines, direction, next_position, tracked)
                    else:
                        next_position = get_next_position(direction, x, y)
                case "/":
                    matrix[y][x] = "/"
                    direction = get_direction_bounced_from_mirror("/", direction)
                    next_position = get_next_position(direction, x, y)
                case "\\":
                    matrix[y][x] = "\\"
                    direction = get_direction_bounced_from_mirror("\\", direction)
                    next_position = get_next_position(direction, x, y)

        except IndexError:
            out_of_bound = True

    return matrix


def part_one():
    lines = parse_input("day_16.txt")
    count = 0

    direction = Direction.RIGHT

    col_size = len(lines[0])
    row_size = len(lines)

    matrix = [[" " for i in range(col_size)] for j in range(row_size)]

    traversed_matrix = traverse_direction(
        matrix=matrix,
        lines=lines,
        direction=direction,
        starting_position=(0, 0),
    )

    for row in traversed_matrix:
        energized_tiles = ["#" if item != " " else " " for item in row]
        count += len([item for item in energized_tiles if item == "#"])
        print(energized_tiles)

    print("Part 1: ", count)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 3: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
