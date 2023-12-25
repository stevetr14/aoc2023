import time
from functools import cache

from utils import parse_input


@cache
def count_arrangement(arrangement: str, springs: tuple[int, ...]) -> int:
    """This is based off a cached solution online. Mad fast."""
    count = 0

    # Check if there are no springs left then return binary value (equate to 1 or 0)
    if not springs:
        return '#' not in arrangement

    current, remaining = springs[0], springs[1:]
    arrangement_space = len(arrangement) - sum(remaining) - len(remaining) - current + 1

    for i in range(arrangement_space):
        if "#" in arrangement[:i]:
            break

        # Checks if placing the current spring at the current position is valid
        if (
            (next_slot := i + current) <= len(arrangement)
            and "." not in arrangement[i:next_slot]
            and arrangement[next_slot: next_slot + 1] != "#"
        ):
            count += count_arrangement(arrangement[next_slot + 1:], remaining)

    return count


def part_one():
    lines = parse_input("day_12.txt")

    total = 0

    for line in lines:
        arrangement, order = line.split(" ")
        springs = tuple(map(int, order.split(",")))

        total += count_arrangement(arrangement, springs)

    print("Part 1: ",  total)


def part_two():
    lines = parse_input("day_12.txt")

    total = 0

    start = time.time()

    for line in lines:
        arrangement, order = line.split(" ")
        springs = tuple(map(int, order.split(",")))

        # Increase the size of arrangement and springs by 5 times
        total += count_arrangement("?".join([arrangement] * 5), springs * 5)

    end = time.time()

    # Insane cached speed ~ 0.21 secs
    print("Part 2: ", total, "- Time: ", end - start)


if __name__ == "__main__":
    part_one()
    part_two()
