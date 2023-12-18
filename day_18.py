from utils import parse_input


def get_info(x1: int, y1: int, x2: int, y2: int) -> int:
    return x1 * y2 - y1 * x2


def calculate_area(points: list[tuple[int, int]]) -> float:
    n = len(points)
    first_x, first_y = points[0]
    prev_x, prev_y = first_x, first_y
    res = 0

    for i in range(1, n):
        next_x, next_y = points[i]
        res += get_info(prev_x, prev_y, next_x, next_y)
        prev_x = next_x
        prev_y = next_y

    res += get_info(prev_x, prev_y, first_x, first_y)

    return abs(res) / 2.0


def part_one():
    lines = parse_input("test.txt")

    points = [
        (0, 0), (5, 0), (6, 0), (6, 4), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (6, 8), (6, 9),
        (2, 9), (1, 9), (1, 8), (1, 7), (0, 7), (0, 6), (0, 5), (1, 5), (2, 5), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1),
    ]

    # print(calculate_area(points))


if __name__ == "__main__":
    part_one()
    # part_two()
