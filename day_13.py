from collections import Counter

from utils import parse_input


def part_one():
    patterns = parse_input("day_13.txt", "\n\n")

    total = 0

    for pattern in patterns:
        row_reflection_points = [0]
        col_reflection_points = [0]

        lines = pattern.strip().split("\n")
        transposed_lines = ["".join(item) for item in list(zip(*lines)) if item]

        for i in range(len(lines) - 1):
            if lines[i] == lines[i + 1]:
                row_reflection_points.append(i + 1)

        for i in range(len(transposed_lines) - 1):
            if transposed_lines[i] == transposed_lines[i + 1]:
                col_reflection_points.append(i + 1)

        num_of_unique_rows = len(lines) - sum([v for v in Counter(lines).values() if v > 1])
        num_of_unique_cols = len(transposed_lines) - sum([v for v in Counter(transposed_lines).values() if v > 1])

        last_row_reflection = max(row_reflection_points)
        last_col_reflection = max(col_reflection_points)

        if num_of_unique_rows <= num_of_unique_cols:
            print("Row: ", last_row_reflection)
            total += 100 * last_row_reflection
        else:
            print("Col: ", last_col_reflection)
            total += last_col_reflection

        print()

    print(total)


def part_two():
    lines = parse_input("test.txt")


if __name__ == "__main__":
    part_one()
    # part_two()
