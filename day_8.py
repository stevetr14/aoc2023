import math

from utils import parse_input


DIRECTIONS = {
    "L": 0,
    "R": 1,
}


def create_path_mapping(path_rows: list[str]) -> dict[str, tuple[str, str]]:
    """Create a dictionary that maps node to the path tuple that looks similar to the text input."""
    mapping = dict()

    for line in path_rows:
        start, paths = line.split(" = ")
        paths = paths.replace("(", "").replace(")", "")
        mapping[start] = tuple(paths.split(", "))

    return mapping


def part_one():
    lines = parse_input("day_8.txt")
    instructions = lines[0]

    mapping = create_path_mapping(lines[1:])

    count = 0
    instructions_index = 0
    path_index = 0

    # Starting node.
    next_point = "AAA"

    finished = False

    while not finished:
        try:
            instruction = instructions[instructions_index]
        # When getting past the end of the instruction list, reset to the start
        except IndexError:
            instructions_index = 0
            instruction = instructions[instructions_index]

        # Get the tuple index.
        index = DIRECTIONS[instruction]
        # Set new next point from the mapping.
        next_point = mapping[next_point][index]

        instructions_index += 1
        count += 1
        path_index += 1

        # Stop the count when reaching the final node.
        if next_point == "ZZZ":
            finished = True

    print(count)


def part_two():
    lines = parse_input("day_8.txt")
    instructions = lines[0]

    mapping = create_path_mapping(lines[1:])

    # Get all the starting nodes that have "A" at the end.
    start_points = [node for node in mapping.keys() if node[-1] == "A"]
    instructions_index = 0
    all_counts = []

    for next_point in start_points:
        count = 0
        path_index = 0

        finished = False

        while not finished:
            try:
                instruction = instructions[instructions_index]
            # When getting past the end of the instruction list, reset to the start
            except IndexError:
                instructions_index = 0
                instruction = instructions[instructions_index]

            index = DIRECTIONS[instruction]
            next_point = mapping[next_point][index]

            instructions_index += 1
            count += 1
            path_index += 1

            # Stop the count when reaching the final node.
            if next_point[-1] == "Z":
                finished = True

        all_counts.append(count)

    # Didn't even know the built-in math lib has lcm :O
    print(math.lcm(*all_counts))


if __name__ == "__main__":
    part_one()
    part_two()
