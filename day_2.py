from utils import parse_input


def part_one():
    games = parse_input("day_2.txt")
    config = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0

    for game in games:
        game_n, outputs = game.split(":")
        game_id = game_n.replace("Game ", "")
        outputs_list = [i for o in outputs.split(";") for i in o.strip().split(",")]

        invalid = False
        for item in outputs_list:
            n, colour = item.strip().split(" ")
            if int(n) > config[colour]:
                invalid = True
                break

        if invalid:
            continue
        else:
            total += int(game_id)

    print("Part 1", total)


def part_two():
    games = parse_input("day_2.txt")
    total = 0

    for game in games:
        _, outputs = game.split(":")
        outputs_list = [i for o in outputs.split(";") for i in o.strip().split(",")]

        cubes = {
            "red": 0, "green": 0, "blue": 0
        }

        for item in outputs_list:
            n, colour = item.strip().split(" ")
            if cubes[colour] < int(n):
                cubes[colour] = int(n)

        total += cubes["red"] * cubes["green"] * cubes["blue"]

    print("Part 2", total)


if __name__ == "__main__":
    part_one()
    part_two()
