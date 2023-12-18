import matplotlib.pyplot as plt
from shapely import polygons, Point

from utils import parse_input


def part_one():
    lines = parse_input("day_18.txt")

    all_x_values = []
    all_y_values = []
    x = 0
    y = 0

    area = 0

    points = []

    for line in lines:
        direction, steps, _ = line.split(" ")
        steps = int(steps)
        area += steps

        match direction:
            case "R":
                points.append((x, y))
                x += steps
            case "L":
                points.append((x, y))
                x -= steps
            case "U":
                points.append((x, y))
                y += steps
            case "D":
                points.append((x, y))
                y -= steps

        all_x_values.append(x)
        all_y_values.append(y)

    max_x = max(all_x_values)
    min_x = min(all_x_values)
    max_y = max(all_y_values)
    min_y = min(all_y_values)

    polygon = polygons(points)

    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            if polygon.contains(Point(i, j)):
                area += 1

    print("Part 1: ", area)


DIRECTION = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def part_two():
    lines = parse_input("test.txt")

    points = []
    all_x_values = []
    all_y_values = []

    x = 0
    y = 0

    area = 0

    for line in lines:
        _, _, colour = line.split(" ")

        colour_value = colour.replace("#", "").replace("(", "").replace(")", "")
        steps = int(colour_value[:5], 16)
        direction = DIRECTION[colour_value[-1]]

        area += steps

        match direction:
            case "R":
                points.append((x, y))
                x += steps
            case "L":
                points.append((x, y))
                x -= steps
            case "U":
                points.append((x, y))
                y += steps
            case "D":
                points.append((x, y))
                y -= steps

        points.append((x, y))
        all_x_values.append(x)
        all_y_values.append(y)

    points.append((x, y))

    polygon = polygons(points)
    a, b = polygon.exterior.xy

    plt.plot(a, b)
    plt.show()


if __name__ == "__main__":
    part_one()
    # part_two()
