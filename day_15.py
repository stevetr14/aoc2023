import re
from collections import defaultdict

from utils import parse_input


MULTIPLIER = 17
RANGE_SIZE = 256


def apply_hash_algorithm(line: str) -> int:
    current_value = 0
    for c in line.strip():
        current_value += ord(c)
        current_value *= MULTIPLIER
        current_value %= RANGE_SIZE

    return current_value


def part_one():
    lines = parse_input("day_15.txt", ",")

    total = 0
    for line in lines:
        current_value = apply_hash_algorithm(line)
        total += current_value

    print("Part 1: ", total)


def part_two():
    lines = parse_input("day_15.txt", ",")
    box_map = defaultdict(dict)

    total = 0

    for line in lines:
        # Need to learn how to regex better
        label, value, _ = re.split(r"([^a-z]+)", line.strip())
        # Yikes
        sign_value = [item for item in re.split(r"(\d+)", value) if item]

        # We know if there is only 1 item then it's the "-" operation
        if len(sign_value) == 1:
            try:
                box_map[apply_hash_algorithm(label)].pop(label)
            except KeyError:
                continue
        if len(sign_value) == 2:
            box_map[apply_hash_algorithm(label)][label] = int(sign_value[1])

    for box_idx, box_content in box_map.items():
        box_value = box_idx + 1
        for i, v in enumerate(box_content.values(), start=1):
            total += box_value * i * v

    print("Part 2: ", total)


if __name__ == "__main__":
    part_one()
    part_two()
