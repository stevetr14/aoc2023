from utils import parse_input


def get_differences(row: list[int]) -> list[int]:
    return [j - i for i, j in zip(row[:-1], row[1:])]


def part_one():
    lines = parse_input("day_9.txt")

    total = 0

    for line in lines:
        numbers = [int(n) for n in line.split(" ")]
        differences = get_differences(numbers)

        # Get the last values from the original row and the first difference row.
        last_diffs = [numbers[-1], differences[-1]]

        # Don't need to go all the way to 0 here, this check should pass the first time we get all same numbers.
        is_uniform = len(set(differences)) == 1

        while not is_uniform:
            differences = get_differences(differences)
            is_uniform = len(set(differences)) == 1
            last_diffs.append(differences[-1])

        # The prediction is calculated by adding the last value of the original row and all the differences.
        total += sum(last_diffs)

    print("Part 1:", total)


def part_two():
    lines = parse_input("day_9.txt")

    total = 0

    for line in lines:
        numbers = [int(n) for n in line.split(" ")]
        differences = get_differences(numbers)

        # Get the first values from the original row and the first difference row.
        first_diffs = [numbers[0], differences[0]]

        # Don't need to go all the way to 0 here, this check should pass the first time we get all same numbers.
        is_uniform = len(set(differences)) == 1

        while not is_uniform:
            differences = get_differences(differences)
            is_uniform = len(set(differences)) == 1
            first_diffs.append(differences[0])

        # Get the difference of the second last and last values first.
        diff = first_diffs[-2] - first_diffs[-1]

        # Going backwards and subtract the result (e.g. [3, 2, 1, 0] -> 3 - (2 - (1 - 0)) = 2)
        for i in reversed(range(2, len(first_diffs))):
            diff = first_diffs[i - 2] - diff

        total += diff

    print("Part 2:", total)


if __name__ == "__main__":
    part_one()
    part_two()
