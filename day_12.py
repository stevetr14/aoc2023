from utils import parse_input


def part_one():
    lines = parse_input("test.txt")

    for line in lines:
        arrangement, order = line.split(" ")
        # items = [len(item) for item in arrangement.split(".") if item]
        values = [int(item) for item in order.split(",")]

        test = ""
        for num in values:
            for i in range(num):
                test += "#"
            test += " "

        x = [c for c in test.split(" ") if c]
        y = [c for c in arrangement.split(".") if c]

        if len(y) < len(x):
            print(x)
            print(y.split("#"))


def part_two():
    pass


if __name__ == "__main__":
    part_one()
    # part_two()
