from collections import OrderedDict, defaultdict

from utils import parse_input


def part_one():
    lines = parse_input("day_4.txt")

    total = 0

    for line in lines:
        left, right = line.split(" | ")
        _, winning = left.split(": ")
        winning_nums = set(winning.strip().split(" "))
        given_nums = set(right.strip().split(" "))

        x = [i for i in winning_nums.intersection(given_nums) if i != ""]

        if len(x) > 0:
            points = 2 ** (len(x) - 1)
            print(points, x)
            total += points

    print(total)


def count_card(
    current_card: int,
    array: list[int],
    tracker_1_: dict[int, list[int]],
    tracker_2_: dict[int, int],
):
    for val in array:
        if val != current_card:
            if len(tracker_1_[val]) > 0:
                count_card(val, tracker_1_[val], tracker_1_, tracker_2_)
            tracker_2_[val] += 1

    return tracker_2_


def part_two():
    lines = parse_input("test.txt")

    total = 0
    tracker_1 = defaultdict(list)
    tracker_2 = defaultdict(int)
    max_length = len(lines)

    for i in range(max_length):
        line = lines[i]
        left, right = line.split(" | ")
        card, winning = left.split(": ")
        card_num = int(card.replace("Card ", "").strip())
        winning_nums = set(winning.strip().split(" "))
        given_nums = set(right.strip().split(" "))

        x = [i for i in winning_nums.intersection(given_nums) if i != ""]

        # tracker_1[card_num] = [card_num]

        if len(x) > 0:
            tracker_1[card_num].extend(list(range(card_num + 1, min(card_num + len(x) + 2, max_length))))
        else:
            tracker_1[card_num] = []

    for k, v in tracker_1.items():
        # tracker_2[k] += 1
        # print(k, v)
        count_card(k, v, tracker_1, tracker_2)
        # for val in v:
        #     if val != k:
        #         tracker_2[val] += 1
        #         # print(tracker_1[val])
        #         if len(tracker_1[val]) > 1:
        #             for y in tracker_1[val]:
        #                 tracker_2[y] += 1

    print(tracker_2)
    # print(sum(tracker_2.values()))


if __name__ == "__main__":
    # part_one()
    part_two()
