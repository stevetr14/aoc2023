from sympy import symbols, Eq, solve

from utils import parse_input


TEST_LOWER_BOUND = 7
TEST_UPPER_BOUND = 27

REAL_LOWER_BOUND = 200000000000000
REAL_UPPER_BOUND = 400000000000000


def get_positions_and_velocities(lines: list[str]) -> tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]]:
    positions = list()
    velocities = list()

    for line in lines:
        position, velocity = line.split(" @ ")
        px, py, pz = [int(c) for c in position.split(", ")]
        vx, vy, vz = [int(c) for c in velocity.split(", ")]

        positions.append((px, py, pz))
        velocities.append((vx, vy, vz))

    return positions, velocities


def part_one():
    lines = parse_input("day_24.txt")
    total = 0

    # lower_bound = TEST_LOWER_BOUND
    # upper_bound = TEST_UPPER_BOUND
    lower_bound = REAL_LOWER_BOUND
    upper_bound = REAL_UPPER_BOUND

    last_index = len(lines) - 1
    current_index = 0

    positions, velocities = get_positions_and_velocities(lines)

    while current_index < last_index:
        for i in range(current_index + 1, len(lines)):
            px_1, py_1 = positions[current_index][:2]
            vx_1, vy_1 = velocities[current_index][:2]

            px_2, py_2 = positions[i][:2]
            vx_2, vy_2 = velocities[i][:2]

            # Set up linear equations to solve for two unknowns (these represent time for each plane)
            s, t = symbols("s t")

            eq_1 = Eq(px_1 + vx_1 * s, px_2 + vx_2 * t)
            eq_2 = Eq(py_1 + vy_1 * s, py_2 + vy_2 * t)

            solved = solve((eq_1, eq_2), (s, t))

            if not solved:
                continue

            # Don't count intersections from the past
            if float(dict(solved)[s]) < 0 or float(dict(solved)[t]) < 0:
                continue

            # Calculate the intersected x and y positions
            intersect_x = px_1 + vx_1 * float(dict(solved)[s])
            intersect_y = py_2 + vy_2 * float(dict(solved)[t])

            if lower_bound <= intersect_x <= upper_bound and lower_bound <= intersect_y <= upper_bound:
                print(round(intersect_x, 3), round(intersect_y, 3))
                total += 1

        current_index += 1

    print("Part 1: ", total)


def part_two():
    lines = parse_input("test.txt")
    total = 0

    print("Part 2: ", total)


if __name__ == "__main__":
    part_one()
    # part_two()
