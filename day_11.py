from itertools import combinations

from utils import parse_input

from typing import Iterable


def calculate_total_distance(input_: list[Iterable]) ->  int:
    galaxies = []
    total_distance = 0

    for row_idx, row in enumerate(input_):
        for col_idx, char in enumerate(row):
            if char == "#":
                galaxies.append((row_idx, col_idx))

    for item in list(combinations(galaxies, 2)):
        start, end = item
        xy_diff = tuple(abs(b - a) for a, b in zip(start, end))
        total_distance += sum(xy_diff)

    return total_distance


def get_double_space_expanded_universe(input_: list[Iterable]) -> list[Iterable]:
    expanded_rows = []
    expanded_transposed_rows = []

    for line in input_:
        expanded_rows.append(line)
        if len(set(line)) == 1:
            expanded_rows.append(line)

    for row in list(map(list, zip(*expanded_rows))):
        expanded_transposed_rows.append(row)
        if len(set(row)) == 1:
            expanded_transposed_rows.append(row)

    return list(map(list, zip(*expanded_transposed_rows)))


def part_one():
    lines = parse_input("day_11.txt")

    expanded_universe = get_double_space_expanded_universe(lines)
    total_distance = calculate_total_distance(expanded_universe)
    print("Part 1: ", total_distance)


def part_two():
    lines = parse_input("day_11.txt")
    base_universe_total_distance = calculate_total_distance(lines)
    double_space_expanded_universe = get_double_space_expanded_universe(lines)
    double_space_total_distance = calculate_total_distance(double_space_expanded_universe)

    # For double space case -> n * 2 -> diff * (2 - 1)
    base_diff = double_space_total_distance - base_universe_total_distance

    # For 1,000,000 times case, get the scaled diff and add to the base total distance
    final_diff = base_diff * (1_000_000 - 1) + base_universe_total_distance

    print("Part 2: ", final_diff)


if __name__ == "__main__":
    part_one()
    part_two()
