import math

from utils import parse_input


def get_num_of_win(t: int, d: int):
    """
    Our quadratic equation is x^2 - tx - d = 0.
    a = 1, b = -t, c = -1
    """
    # We want the minimum time that will give us a distance > the goal to actually beat the record.
    d_to_win = d + 1
    # Ignore negative sign for t in both places since it will be positive anyway
    x_upper = math.floor((t + math.sqrt(math.pow(t, 2) - 4 * d_to_win)) / 2)
    x_lower = math.ceil((t - math.sqrt(math.pow(t, 2) - 4 * d_to_win)) / 2)

    # Subtract 1 for the inclusive range
    return x_upper - x_lower + 1


def part_one():
    lines = parse_input("test.txt")
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
        # count = 0
        # for i in range(1, time_value + 1):
        #     if i * (time_value - i) > distance_value:
        #         count += 1
        #
        # product *= count

        # Solve properly
        count = get_num_of_win(time_value, distance_value)
        product *= count

    print(product)


def part_two():
    lines = parse_input("day_6.txt")

    time_input = lines[0].split(":")
    time_values = [val.strip() for val in time_input[1].strip().split()]
    actual_time = int("".join(time_values))
    distance_input = lines[1].split(":")
    distance_values = [val.strip() for val in distance_input[1].strip().split()]
    actual_distance = int("".join(distance_values))

    # count = 0
    #
    # for i in range(1, actual_time + 1):
    #     if i * (actual_time - i) > actual_distance:
    #         count += 1
    #
    # print(count)

    # Solve properly
    print(get_num_of_win(actual_time, actual_distance))


if __name__ == "__main__":
    part_one()
    part_two()
