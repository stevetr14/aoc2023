import time

from utils import parse_input, batched


def construct_plan():
    sections = parse_input("day_5.txt", "\n\n")
    plan = dict()

    for section in sections:
        label, value = section.split(":")
        # Convert to a list containing lists of numbers
        cleaned_value = [[int(num) for num in item.split(" ")] for item in value.strip().split("\n")]

        plan[label] = cleaned_value

    return plan


def get_target_from_seed(seed: int, rows_: list[list[int, int, int]]) -> int:
    for row in rows_:
        destination, source, length = row
        if seed < source:
            continue

        # Check for inclusive range
        if source <= seed <= source + length - 1:
            if seed > source:
                target = seed - source + destination
            elif seed == source:
                target = destination
            else:
                target = destination + seed
            return target
    else:
        return seed


def get_seed_from_target(target: int, rows_: list[list[int, int, int]]) -> int:
    for row in rows_:
        destination, source, length = row
        if target > destination + length:
            continue

        # Check for inclusive range
        if destination <= target <= destination + length - 1:
            if target > destination:
                seed = target - destination + source
            elif target == destination:
                seed = source
            else:
                seed = destination - target + source
            return seed
    else:
        return target


def part_one():
    start_time = time.time()

    plan = construct_plan()

    seeds = plan["seeds"][0]

    seed_to_soil = plan["seed-to-soil map"]
    soil_to_fertilizer = plan["soil-to-fertilizer map"]
    fertiliser_to_water = plan["fertilizer-to-water map"]
    water_to_light = plan["water-to-light map"]
    light_to_temp = plan["light-to-temperature map"]
    temp_to_humidity = plan["temperature-to-humidity map"]
    # Location is the objective goal
    humidity_to_location = plan["humidity-to-location map"]

    locations = []

    for seed in seeds:
        a = get_target_from_seed(seed, seed_to_soil)
        b = get_target_from_seed(a, soil_to_fertilizer)
        c = get_target_from_seed(b, fertiliser_to_water)
        d = get_target_from_seed(c, water_to_light)
        e = get_target_from_seed(d, light_to_temp)
        f = get_target_from_seed(e, temp_to_humidity)
        location = get_target_from_seed(f, humidity_to_location)
        print(seed, a, b, c, d, e, f, location)

        locations.append(location)

    print("Lowest location", min(locations))

    end_time = time.time()
    print("\nSeconds taken: ", end_time - start_time)


def part_two():
    start_time = time.time()

    plan = construct_plan()

    seed_to_soil = plan["seed-to-soil map"]
    soil_to_fertilizer = plan["soil-to-fertilizer map"]
    fertiliser_to_water = plan["fertilizer-to-water map"]
    water_to_light = plan["water-to-light map"]
    light_to_temp = plan["light-to-temperature map"]
    temp_to_humidity = plan["temperature-to-humidity map"]
    humidity_to_location = plan["humidity-to-location map"]

    batched_pairs = list(batched(plan["seeds"][0], 2))

    # Inspect by 👀
    # TODO: Get the lowest location range via comparison instead
    lowest_location_range = humidity_to_location[4]
    destination, _, range_length = lowest_location_range

    found = False

    # Start from the lowest location destination value in the input (something like 0 100000000 200000000)
    for i in range(destination, destination + range_length - 1):
        humidity = get_seed_from_target(i, humidity_to_location)
        f = get_seed_from_target(humidity, temp_to_humidity)
        e = get_seed_from_target(f, light_to_temp)
        d = get_seed_from_target(e, water_to_light)
        c = get_seed_from_target(d, fertiliser_to_water)
        b = get_seed_from_target(c, soil_to_fertilizer)
        # Get seed back by calculating backwards from location
        seed = get_seed_from_target(b, seed_to_soil)

        for pair in batched_pairs:
            start_, length = pair
            # If the computed seed is within the range of any pair from the input then the location is valid
            if start_ <= seed <= start_ + length - 1:
                found = True
                # Display the first location found
                print(i)
                break

        if found:
            break

    end_time = time.time()
    print("\nSeconds taken: ", end_time - start_time)


def test_day_5():
    rows = [
        # D, S, R
        [0, 69, 1],
        [18, 25, 70],
        [70, 72, 80],
        [210, 200, 1],
        [250, 252, 1],
        [3300, 300, 1600],
        [230_758_172, 30_039_204, 163_596_268],
    ]

    assert get_target_from_seed(49, rows) == 42
    assert get_target_from_seed(69, rows) == 0
    assert get_target_from_seed(140, rows) == 138
    assert get_target_from_seed(252, rows) == 250
    assert get_target_from_seed(306, rows) == 3306
    assert get_target_from_seed(30_039_210, rows) == 230_758_178

    assert get_seed_from_target(42, rows) == 49
    assert get_seed_from_target(0, rows) == 69
    assert get_seed_from_target(138, rows) == 140
    assert get_seed_from_target(250, rows) == 252
    assert get_seed_from_target(3306, rows) == 306
    assert get_seed_from_target(230_758_178, rows) == 30_039_210


if __name__ == "__main__":
    part_one()
    part_two()
    # test_day_5()
