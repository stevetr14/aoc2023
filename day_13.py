from collections import Counter
from pprint import pprint

from utils import parse_input


def part_one():
    patterns = parse_input("day_13.txt", "\n\n")

    total = 0

    for index, pattern in enumerate(patterns, start=1):
        lines = pattern.strip().split("\n")
        transposed_lines = ["".join(item) for item in list(zip(*lines)) if item]

        # Check rows
        num_of_rows = len(lines)
        num_of_cols = len(transposed_lines)

        a = Counter(lines)
        b = Counter(transposed_lines)

        print(index)

        num_to_add = 0

        # Check row reflection from bottom first
        if a[lines[-1]] >= 2:
            for i in range(num_of_rows - 1, 0, -1):
                # Short-circuit when any non-reflection is detected in between.
                if a[lines[i]] < 2:
                    break

                if lines[i] == lines[i - 1]:
                    print("Row <-", i - 1)
                    num_to_add = 100 * i
                    break

        if a[lines[0]] >= 2 and num_to_add == 0:
            for i in range(num_of_rows - 1):
                # Short-circuit when any non-reflection is detected in between.
                if a[lines[i]] < 2:
                    break

                if lines[i] == lines[i + 1]:
                    print("Row ->", i)
                    num_to_add = 100 * (i + 1)
                    break

        # Check column reflection from right first
        if b[transposed_lines[-1]] >= 2 and num_to_add == 0:
            for i in range(num_of_cols - 1, 0, -1):
                # Short-circuit when any non-reflection is detected in between.
                if b[transposed_lines[i]] < 2:
                    break

                if transposed_lines[i] == transposed_lines[i - 1]:
                    print("Col <-", i - 1)
                    num_to_add = i
                    break

        if b[transposed_lines[0]] >= 2 and num_to_add == 0:
            for i in range(num_of_cols - 1):
                # Short-circuit when any non-reflection is detected in between.
                if b[transposed_lines[i]] < 2:
                    break

                if transposed_lines[i] == transposed_lines[i + 1]:
                    print("Col ->", i)
                    num_to_add = i + 1
                    break

        total += num_to_add
        print()

    print(total)


def part_two():
    lines = parse_input("test.txt")


if __name__ == "__main__":
    part_one()
    # part_two()
