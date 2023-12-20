from collections import OrderedDict, defaultdict

from utils import parse_input


def part_one():
    lines = parse_input("test.txt")

    src_destination_map = OrderedDict()
    module_states = defaultdict(list)

    # False = low and True = high
    pulse = False

    for line in lines:
        src, destination = line.split(" -> ")
        destination_list = destination.split(", ")
        # src_destination_map[src] = destination_list
        if src == "broadcaster":
            src_destination_map[src] = destination_list
        else:
            prefix = src[0]
            src_name = src[1:]
            src_destination_map[src_name] = [prefix] + destination_list

    print(src_destination_map)

    broadcaster_destinations = src_destination_map.pop("broadcaster")

    for d in broadcaster_destinations:
        module_states[d].append(False)

    for d in broadcaster_destinations:
        if module_states.get(d):
            print(src_destination_map[d])

    # print(module_states)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
