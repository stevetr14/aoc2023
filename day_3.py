from collections import OrderedDict, defaultdict

from utils import parse_input


def is_symbol(value: str) -> bool:
    return not value.isnumeric() and value != "."


def is_gear_symbol(value: str) -> bool:
    return value == "*"


def part_one():
    lines = parse_input("day_3.txt")
    matrix = []

    for line in lines:
        matrix.append(list(line))

    matrix_size = len(matrix)
    total = 0

    for i in range(matrix_size):
        row_size = len(matrix[i])
        num_string = ""
        adjacent_tracker = []

        for j in range(row_size):
            val = matrix[i][j]

            next_number = False

            # Top
            if i == 0:
                if val.isnumeric():
                    num_string += val

                    # Left Edge
                    if j == 0:
                        if (
                            is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j - 1])
                        ):
                            adjacent_tracker.append(True)
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i + 1][j - 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                else:
                    next_number = True

            # Bottom
            elif i == matrix_size - 1:
                if val.isnumeric():
                    num_string += val

                    # Left Edge
                    if j == 0:
                        if (
                            is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j - 1])
                        ):
                            adjacent_tracker.append(True)
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i - 1][j - 1])
                            or is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                else:
                    next_number = True

            # Middle
            elif 0 < i < matrix_size - 1:
                if val.isnumeric():
                    num_string += val

                    # Left edge
                    if j == 0:
                        if (
                            is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j + 1])
                            or is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j - 1])
                            or is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j - 1])
                        ):
                            adjacent_tracker.append(True)
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_symbol(matrix[i - 1][j - 1])
                            or is_symbol(matrix[i - 1][j])
                            or is_symbol(matrix[i - 1][j + 1])
                            or is_symbol(matrix[i][j - 1])
                            or is_symbol(matrix[i][j + 1])
                            or is_symbol(matrix[i + 1][j - 1])
                            or is_symbol(matrix[i + 1][j])
                            or is_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append(True)
                else:
                    next_number = True

            # Reset
            if next_number and num_string:
                print(num_string, adjacent_tracker)
                if adjacent_tracker:
                    total += int(num_string)
                num_string = ""
                adjacent_tracker = []

    print(total)


def part_two():
    lines = parse_input("day_3.txt")
    matrix = []

    for line in lines:
        matrix.append(list(line))

    matrix_size = len(matrix)
    gears = []
    part_numbers = OrderedDict()
    total = 0

    for i in range(matrix_size):
        row_size = len(matrix[i])
        num_string = ""
        adjacent_tracker = []

        for j in range(row_size):
            val = matrix[i][j]

            if is_gear_symbol(val):
                gears.append((i, j))

            next_number = False

            # Top
            if i == 0:
                if val.isnumeric():
                    num_string += val

                    # Left Edge
                    if j == 0:
                        if (
                            is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j - 1])
                        ):
                            adjacent_tracker.append((i, j))
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i + 1][j - 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                else:
                    next_number = True

            # Bottom
            elif i == matrix_size - 1:
                if val.isnumeric():
                    num_string += val

                    # Left Edge
                    if j == 0:
                        if (
                            is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j - 1])
                        ):
                            adjacent_tracker.append((i, j))
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i - 1][j - 1])
                            or is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                else:
                    next_number = True

            # Middle
            elif 0 < i < matrix_size - 1:
                if val.isnumeric():
                    num_string += val

                    # Left edge
                    if j == 0:
                        if (
                            is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j + 1])
                            or is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                    # Right Edge
                    elif j == row_size - 1:
                        if (
                            is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j - 1])
                            or is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j - 1])
                        ):
                            adjacent_tracker.append((i, j))
                        # Last digit so end here
                        next_number = True
                    else:
                        if (
                            is_gear_symbol(matrix[i - 1][j - 1])
                            or is_gear_symbol(matrix[i - 1][j])
                            or is_gear_symbol(matrix[i - 1][j + 1])
                            or is_gear_symbol(matrix[i][j - 1])
                            or is_gear_symbol(matrix[i][j + 1])
                            or is_gear_symbol(matrix[i + 1][j - 1])
                            or is_gear_symbol(matrix[i + 1][j])
                            or is_gear_symbol(matrix[i + 1][j + 1])
                        ):
                            adjacent_tracker.append((i, j))
                else:
                    next_number = True

            # Reset
            if next_number and num_string:
                if adjacent_tracker:
                    part_numbers[(i, j)] = (num_string, adjacent_tracker)
                num_string = ""
                adjacent_tracker = []

    for gear in gears:
        gear_part_mappings = defaultdict(list)
        x, y = gear
        surrounding_coords = {(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)}
        for pair in part_numbers.values():
            (part_number, positions) = pair
            if len(surrounding_coords.intersection(set(positions))) > 0:
                gear_part_mappings[gear].append(part_number)

        parts = gear_part_mappings[gear]
        product = 1
        if len(parts) > 1:
            for part in parts:
                product *= int(part)

        if product != 1:
            total += product

    print(total)


if __name__ == "__main__":
    part_one()
    part_two()
