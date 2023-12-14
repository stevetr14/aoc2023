from utils import parse_input, transpose_list


def part_one():
    lines = parse_input("day_14.txt")

    total = 0

    for line in transpose_list(lines):
        col_length = len(line)

        old_line = line.copy()

        for i in range(col_length - 1):
            if line[i] == "." and line[i + 1] == "O":
                line[i] = "O"
                line[i + 1] = "."

        new_line = line.copy()

        while new_line != old_line:
            old_line = new_line.copy()

            for i in range(col_length - 1):
                if line[i] == "." and line[i + 1] == "O":
                    line[i] = "O"
                    line[i + 1] = "."

            new_line = line.copy()

        print(new_line)

        for i, c in enumerate(new_line):
            if c == "O":
                total += col_length - i

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    # part_one()
    part_two()
