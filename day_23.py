import sys

from utils import parse_input


# TODO: Figure out a non hacky way that requires bypassing recursion limit.
sys.setrecursionlimit(10000)


# def is_valid(row: int, col: int, row_size: int, col_size: int, visited: list[list[str]]) -> bool:
#     if row < 0 or col < 0 or row >= row_size or col >= col_size or visited[row][col] != " ":
#         return False
#     return True
#
#
# def dfs(grid: list[list[str]], row_size: int, col_size: int) -> int:
#     # Direction vectors
#     direction_row = [0, 1, 0, -1]
#     direction_col = [1, 0, -1, 0]
#
#     destination_x = row_size - 2  # destination x
#     destination_y = col_size - 1  # destination y
#
#     # starting point
#     stack = [(0, 1)]
#
#     visited = [[" " for i in entry] for entry in grid]
#
#     while len(stack) > 0 and stack[-1] != (destination_x, destination_y):
#         curr_index = len(stack) - 1
#         curr = stack[curr_index]
#         stack.remove(stack[curr_index])
#         row = curr[0]
#         col = curr[1]
#
#         if not is_valid(row, col, row_size, col_size, visited) or grid[row][col] == "#":
#             continue
#
#         visited[row][col] = "O"
#
#         for i in range(4):
#             adj_x = row + direction_row[i]
#             adj_y = col + direction_col[i]
#             stack.append((adj_x, adj_y))
#
#     for r in visited:
#         print("".join(r))
#
#     count = 0
#     for v in visited:
#         count += v.count("O")
#
#     return count


def search(
    sy: int,
    sx: int,
    dy: int,
    dx: int,
    grid: list[list[str]],
    path: list[tuple[int, int]] | None = None,
    direction: str | None = None,
):
    path = path or list()

    current_trail = grid[sy][sx]

    if sy < 0 or sx < 0 or sy >= len(grid) or sx >= len(grid[0]):
        return
    if (sy, sx) in path or current_trail == "#":
        return

    if current_trail in ["^", "v", ">", "<"]:
        direction = current_trail

    if (
        (direction == ">" and grid[sy][sx + 1] == "#")
        | (direction == "<" and grid[sy][sx - 1] == "#")
        | (direction == "v" and grid[sy + 1][sx] == "#")
        | (direction == "^" and grid[sy - 1][sx] == "#")
    ):
        direction = None

    path.append((sy, sx))

    if (sy, sx) == (dy, dx):
        yield path
    else:
        try:
            if direction is None or direction == "v":
                for possible_path in search(sy + 1, sx, dy, dx, grid, list(path)):
                    yield possible_path
            if direction is None or direction == "^":
                for possible_path in search(sy - 1, sx, dy, dx, grid, list(path)):
                    yield possible_path
            if direction is None or direction == ">":
                for possible_path in search(sy, sx + 1, dy, dx, grid, list(path)):
                    yield possible_path
            if direction is None or direction == "<":
                for possible_path in search(sy, sx - 1, dy, dx, grid, list(path)):
                    yield possible_path
        except RecursionError:
            yield path


def part_one():
    lines = parse_input("day_23.txt")

    row_size = len(lines)
    col_size = len(lines[0])

    # find path
    sx = 1  # source x
    sy = 0  # source y
    dx = row_size - 2  # destination x
    dy = col_size - 1  # destination y

    matrix = [list(line) for line in lines]

    print("Part 1:", max(list(search(sy, sx, dy, dx, matrix))))


def part_two():
    lines = parse_input("day_23.txt")

    matrix = [list(line) for line in lines]

    row_size = len(lines)
    col_size = len(lines[0])

    # sx = 1  # source x
    # sy = 0  # source y
    # dx = row_size - 2  # destination x
    # dy = col_size - 1  # destination y

    print("Part 2: ")


if __name__ == "__main__":
    part_one()
    # part_two()
