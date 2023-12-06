from utils import parse_input


def part_one():
    lines = parse_input("day_6.txt")
    # 1 ms / 6 ms - 6 mm (1 mm / ms)
    # 2 ms / 5 ms - 10 mm (2 mm / ms)
    # 3 ms / 4 ms - 12 mm ...
    # 4 ms / 3 ms - 12 mm
    # 5 ms / 2 ms - 10 mm
    # 6 ms / 1 ms - 6 mm
    # 7 ms / 0 ms - 0 mm
    time_input = lines[0].split(":")
    time_values = [int(val.strip()) for val in time_input[1].strip().split()]
    distance_input = lines[1].split(":")
    distance_values = [int(val.strip()) for val in distance_input[1].strip().split()]

    product = 1
    for time_value, distance_value in zip(time_values, distance_values):
        count = 0
        for i in range(1, time_value + 1):
            if i * (time_value - i) > distance_value:
                count += 1

        product *= count
        print(distance_value, count)

    print(product)


def part_two():
    lines = parse_input("day_6.txt")

    time_input = lines[0].split(":")
    time_values = [val.strip() for val in time_input[1].strip().split()]
    actual_time = int("".join(time_values))
    distance_input = lines[1].split(":")
    distance_values = [val.strip() for val in distance_input[1].strip().split()]
    actual_distance = int("".join(distance_values))

    count = 0

    for i in range(1, actual_time + 1):
        if i * (actual_time - i) > actual_distance:
            count += 1

    print(count)


if __name__ == "__main__":
    part_one()
    part_two()
