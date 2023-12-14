from collections import Counter
from pprint import pprint

from utils import parse_input, transpose_list


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
            for i in range(num_of_rows - 1, 1, -1):
                # Short-circuit when any non-reflection is detected in between.
                if a[lines[i]] < 2:
                    break

                if lines[i] == lines[i - 1] and a[lines[i]] < 4:
                    print("Row <-", i - 1)
                    num_to_add = 100 * i
                    break

        if a[lines[0]] >= 2 and num_to_add == 0:
            for i in range(num_of_rows - 1):
                # Short-circuit when any non-reflection is detected in between.
                if a[lines[i]] < 2:
                    break

                if lines[i] == lines[i + 1] and a[lines[i]] < 4:
                    print("Row ->", i)
                    num_to_add = 100 * (i + 1)
                    break

        # Check column reflection from right first
        if b[transposed_lines[-1]] >= 2 and num_to_add == 0:
            for i in range(num_of_cols - 1, 1, -1):
                # Short-circuit when any non-reflection is detected in between.
                if b[transposed_lines[i]] < 2:
                    break

                if transposed_lines[i] == transposed_lines[i - 1] and b[transposed_lines[i]] < 4:
                    print("Col <-", i - 1)
                    num_to_add = i
                    break

        if b[transposed_lines[0]] >= 2 and num_to_add == 0:
            for i in range(num_of_cols - 1):
                # Short-circuit when any non-reflection is detected in between.
                if b[transposed_lines[i]] < 2:
                    break

                if transposed_lines[i] == transposed_lines[i + 1] and b[transposed_lines[i]] < 4:
                    print("Col ->", i)
                    num_to_add = i + 1
                    break

        total += num_to_add
        print()

    print("Part 1: ", total)


def part_two():
    patterns = parse_input("test.txt", "\n\n")

    total = 0

    for index, pattern in enumerate(patterns, start=1):
        lines = pattern.strip().split("\n")
        transposed_lines = ["".join(item) for item in list(zip(*lines)) if item]

        num_of_cols = len(transposed_lines)

        print(index)

        # Rows
        reflected_rows = []
        reflected_cols = []
        for col_i in range(num_of_cols - 1):
            lines_ = ["".join(item) for item in zip(*(transposed_lines[:col_i] + transposed_lines[col_i + 1:]))]
            transposed_lines_ = ["".join(item) for item in transpose_list(lines_)]

            for row in lines_:
                print(row)

            print()

            for col in transposed_lines_:
                print(col)

            print(col_i, "\n")

            a = Counter(lines_)
            b = Counter(transposed_lines_)
            num_of_rows_ = len(lines_)
            num_of_cols_ = len(transposed_lines_)

            if a[lines_[0]] >= 2:
                for i in range(num_of_rows_ - 1):
                    # Short-circuit when any non-reflection is detected in between.
                    if a[lines_[i]] < 2:
                        break

                    if lines_[i] == lines_[i + 1] and a[lines_[i]] < 4:
                        reflected_rows.append(i + 1)
                        break

            # Check row reflection from bottom first
            if a[lines_[-1]] >= 2:
                for i in range(num_of_rows_ - 1, 1, -1):
                    # Short-circuit when any non-reflection is detected in between.
                    if a[lines_[i]] < 2:
                        break

                    if lines_[i] == lines_[i - 1] and a[lines_[i]] < 4:
                        reflected_rows.append(i)
                        break

            if b[transposed_lines_[0]] >= 2:
                for i in range(num_of_cols_ - 1):
                    # Short-circuit when any non-reflection is detected in between.
                    if b[transposed_lines_[i]] < 2:
                        break

                    if transposed_lines_[i] == transposed_lines_[i + 1] and b[transposed_lines_[i]] < 4:
                        reflected_cols.append(i + 1)
                        break

            if b[transposed_lines_[-1]] >= 2:
                for i in range(num_of_cols_ - 1, 1, -1):
                    # Short-circuit when any non-reflection is detected in between.
                    if b[transposed_lines_[i]] < 2:
                        break

                    if transposed_lines_[i] == transposed_lines_[i - 1] and b[transposed_lines_[i]] < 4:
                        reflected_cols.append(i)
                        break

        print("Rows: ", reflected_rows)
        print("Cols: ", reflected_cols)

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
