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
    patterns = parse_input("day_13.txt", "\n\n")

    total = 0

    for index, pattern in enumerate(patterns, start=1):
        lines = pattern.strip().split("\n")
        transposed_lines = ["".join(item) for item in list(zip(*lines)) if item]

        # Check rows
        num_of_rows = len(lines)
        num_of_cols = len(transposed_lines)

        print(index)

        # Rows
        reflected_rows = []
        for col_i in range(num_of_cols - 1):
            lines_ = ["".join(item) for item in zip(*(transposed_lines[:col_i] + transposed_lines[col_i + 1:]))]
            a = Counter(lines_)

            if a[lines_[0]] >= 2:
                for i in range(num_of_rows - 1):
                    # Short-circuit when any non-reflection is detected in between.
                    if a[lines_[i]] < 2:
                        break

                    if lines_[i] == lines_[i + 1] and a[lines_[i]] < 4:
                        reflected_rows.append(i + 1)
                        break

            # Check row reflection from bottom first
            if a[lines_[-1]] >= 2:
                for i in range(num_of_rows - 1, 1, -1):
                    # Short-circuit when any non-reflection is detected in between.
                    if a[lines_[i]] < 2:
                        break

                    if lines_[i] == lines_[i - 1] and a[lines_[i]] < 4:
                        reflected_rows.append(i)
                        break

        # Columns
        reflected_cols = []
        for row_i in range(num_of_rows - 1):
            transposed_lines_ = ["".join(item) for item in zip(*(lines[:row_i] + lines[row_i + 1:]))]
            b = Counter(transposed_lines_)

            # Check column reflection from right first
            if b[transposed_lines_[0]] >= 2:
                for i in range(num_of_cols - 1):
                    # Short-circuit when any non-reflection is detected in between.
                    if b[transposed_lines_[i]] < 2:
                        break

                    if transposed_lines_[i] == transposed_lines_[i + 1] and b[transposed_lines_[i]] < 4:
                        reflected_cols.append(i + 1)
                        break

            if b[transposed_lines_[-1]] >= 2:
                for i in range(num_of_cols - 1, 1, -1):
                    # Short-circuit when any non-reflection is detected in between.
                    if b[transposed_lines_[i]] < 2:
                        break

                    if transposed_lines_[i] == transposed_lines_[i - 1] and b[transposed_lines_[i]] < 4:
                        reflected_cols.append(i)
                        break

        print("Rows: ", reflected_rows)
        print("Cols: ", reflected_cols)

        reflected_rows_counter = Counter(reflected_rows).items()
        reflected_cols_counter = Counter(reflected_cols).items()

        num_to_add = 0

        if len(reflected_rows_counter) == 2 and num_to_add == 0:
            for k, v in reflected_rows_counter:
                if v == 1:
                    num_to_add = 100 * k
                    print("Row: ", k)
                    break

        if len(reflected_cols_counter) == 2 and num_to_add == 0:
            for k, v in reflected_cols_counter:
                if v == 1:
                    num_to_add = k
                    print("Col: ", k)
                    break

        if not reflected_rows_counter and reflected_cols_counter and num_to_add == 0:
            num_to_add = reflected_cols[0]
            print("Col: ", reflected_cols[0])

        if not reflected_cols_counter and reflected_rows_counter and num_to_add == 0:
            num_to_add = 100 * reflected_rows[0]
            print("Row: ", reflected_rows[0])

        if len(reflected_rows_counter) == len(reflected_cols_counter) and num_to_add == 0:
            if len(reflected_rows) < len(reflected_cols):
                num_to_add = 100 * reflected_rows[0]
                print("Row: ", reflected_rows[0])
            else:
                num_to_add = reflected_cols[0]
                print("Col: ", reflected_cols[0])

        total += num_to_add

        print()

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
