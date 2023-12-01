def part_1():
    with open("day_1.txt") as f:
        total = 0
        for line in f.read().split("\n"):
            first = None
            second = None

            for i in line:
                try:
                    first = int(i)
                    break
                except:
                    continue

            for i in reversed(line):
                try:
                    second = int(i)
                    break
                except:
                    continue

            if first and second:
                x = int(f"{first}{second}")
                total += x

        print(total)


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_2():
    with open("day_1.txt") as f:
        total = 0
        for line in f.read().split("\n"):
            first = None
            second = None

            size = len(line)

            for i in range(size):
                for digit, num in digits.items():
                    x = line[i:i + len(digit)]
                    first = digits.get(x)
                    if first is not None:
                        break
                if first is None:
                    try:
                        first = int(line[i])
                        break
                    except:
                        continue
                else:
                    break

            for i in range(size):
                stop = None if i == 0 else -i
                for digit, num in digits.items():
                    y = line[-(i + len(digit)):stop:]
                    second = digits.get(y)
                    if second is not None:
                        break
                if second is None:
                    try:
                        second = int(line[-(i + 1)])
                        break
                    except:
                        continue
                else:
                    break

            if first and second:
                x = int(f"{first}{second}")
                total += x
        print(total)


if __name__ == "__main__":
    part_1()
    part_2()

