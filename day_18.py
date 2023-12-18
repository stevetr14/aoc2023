import matplotlib.pyplot as plt
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


DIRECTION = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def part_two():
    lines = parse_input("test.txt")

    points = []

    x = 0
    y = 0

    _, _, first_colour = lines[0].split(" ")
    first_colour_value = first_colour.replace("#", "").replace("(", "").replace(")", "")
    first_steps = int(first_colour_value[:5], 16)
    first_direction = DIRECTION[first_colour_value[-1]]

    match first_direction:
        case "R":
            x += first_steps
        case "L":
            x -= first_steps
        case "U":
            y += first_steps
        case "D":
            y -= first_steps

    points.append((x, y))

    for line in lines[1:-1]:
        _, _, colour = line.split(" ")

        colour_value = colour.replace("#", "").replace("(", "").replace(")", "")
        steps = int(colour_value[:5], 16)
        direction = DIRECTION[colour_value[-1]]

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

    # Handle last point
    _, _, last_colour = lines[-1].split(" ")
    last_colour_value = last_colour.replace("#", "").replace("(", "").replace(")", "")
    last_steps = int(last_colour_value[:5], 16)
    last_direction = DIRECTION[last_colour_value[-1]]

    match last_direction:
        case "R":
            x += last_steps
        case "L":
            x -= last_steps
        case "U":
            y += last_steps
        case "D":
            y -= last_steps

    points.append((x, y))

    polygon = polygons(points)
    print(polygon.area)
    print(polygon.length)

    a, b = polygon.exterior.xy
    plt.plot(a, b)
    plt.show()


if __name__ == "__main__":
    # part_one()
    part_two()
