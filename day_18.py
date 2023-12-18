from shapely import polygons, Point

from utils import parse_input


def part_one():
    lines = parse_input("day_18.txt")

    all_x_values = []
    all_y_values = []
    x = 0
    y = 0

    all_x_values.append(x)
    all_y_values.append(y)

    area = 0

    for line in lines:
        direction, steps, colour = line.split(" ")
        area += int(steps)

        for i in range(int(steps)):
            match direction:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y -= 1
                case "D":
                    y += 1

            all_x_values.append(x)
            all_y_values.append(y)

    max_x = max(all_x_values)
    min_x = min(all_x_values)
    max_y = max(all_y_values)
    min_y = min(all_y_values)

    points = [(i, j) for i, j in zip(all_x_values, all_y_values)]

    polygon = polygons(points)

    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            if polygon.contains(Point(i, j)):
                area += 1

    print("Part 1: ", area)


if __name__ == "__main__":
    part_one()
    # part_two()
