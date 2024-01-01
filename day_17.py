from heapq import heappop, heappush
from typing import NamedTuple

from utils import parse_input


GridPoint = tuple[int, int]
Grid = dict[GridPoint, int]


class Direction:
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


class Position(NamedTuple):
    loc: GridPoint
    direction: str


State = tuple[int, Position, int]


def parse_grid(raw_grid: list[str]) -> Grid:
    """Returns tuples of (row, col) with their value."""
    result = {}

    for row, line in enumerate(raw_grid):
        for col, c in enumerate(line):
            result[row, col] = int(c)

    return result


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


def get_next_position(direction: str, x: int, y: int) -> Position:
    match direction:
        case Direction.RIGHT:
            return Position((x + 1, y), Direction.RIGHT)
        case Direction.LEFT:
            return Position((x - 1, y), Direction.LEFT)
        case Direction.DOWN:
            return Position((x, y + 1), Direction.DOWN)
        case Direction.UP:
            return Position((x, y - 1), Direction.UP)


def part_one():
    lines = parse_input("day_17.txt")
    total = 0

    # Bottom right corner
    target = (len(lines) - 1, len(lines[0]) - 1)

    grid = parse_grid(lines)

    queue: list[State] = [
        (0, Position((0, 0), Direction.DOWN), 0),
        (0, Position((0, 0), Direction.RIGHT), 0),
    ]
    seen: set[tuple[Position, int]] = set()

    while queue:
        cost, pos, num_steps = heappop(queue)

        if pos.loc == target:
            total = cost
            break

        if (pos, num_steps) in seen:
            continue

        seen.add((pos, num_steps))

        x, y = pos.loc
        next_left = get_next_position(rotate_direction_90_left(pos.direction), x, y)
        next_right = get_next_position(rotate_direction_90_right(pos.direction), x, y)
        next_forward = get_next_position(pos.direction, x, y)

        if next_left.loc in grid:
            heappush(queue, (cost + grid[next_left.loc], next_left, 1))

        if next_right.loc in grid:
            heappush(queue, (cost + grid[next_right.loc], next_right, 1))

        if num_steps < 3 and next_forward.loc in grid:
            heappush(queue, (cost + grid[next_forward.loc], next_forward, num_steps + 1))

    print("Part 1: ", total)


def part_two():
    lines = parse_input("day_17.txt")
    total = 0

    # Bottom right corner
    target = (len(lines) - 1, len(lines[0]) - 1)
    min_steps = 4
    max_steps = 10

    grid = parse_grid(lines)

    queue: list[State] = [
        (0, Position((0, 0), Direction.DOWN), 0),
        (0, Position((0, 0), Direction.RIGHT), 0),
    ]
    seen: set[tuple[Position, int]] = set()

    while queue:
        cost, pos, num_steps = heappop(queue)

        if pos.loc == target and num_steps >= min_steps:
            total = cost
            break

        if (pos, num_steps) in seen:
            continue

        seen.add((pos, num_steps))

        x, y = pos.loc
        next_left = get_next_position(rotate_direction_90_left(pos.direction), x, y)
        next_right = get_next_position(rotate_direction_90_right(pos.direction), x, y)
        next_forward = get_next_position(pos.direction, x, y)

        if num_steps >= min_steps and next_left.loc in grid:
            heappush(queue, (cost + grid[next_left.loc], next_left, 1))

        if num_steps >= min_steps and next_right.loc in grid:
            heappush(queue, (cost + grid[next_right.loc], next_right, 1))

        if num_steps < max_steps and next_forward.loc in grid:
            heappush(queue, (cost + grid[next_forward.loc], next_forward, num_steps + 1))

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
