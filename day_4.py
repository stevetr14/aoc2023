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
    lines = parse_input("day_4.txt")

    tracker = dict()
    max_length = len(lines)

    for i in range(max_length):
        line = lines[i]
        left, right = line.split(" | ")
        card, winning = left.split(": ")
        card_num = int(card.replace("Card ", "").strip())
        winning_nums = set(winning.strip().split(" "))
        given_nums = set(right.strip().split(" "))

        matched_wins = [i for i in winning_nums.intersection(given_nums) if i != ""]

        tracker[card_num] = []

        num_of_win = len(matched_wins)
        if num_of_win > 0:
            max_card_upper = min(card_num + num_of_win + 1, max_length)
            copies = list(range(card_num + 1, max_card_upper + 1))
            tracker[card_num].extend(copies[:num_of_win])

    # Generate scratch copies for each entry
    def get_copies(mapping: dict) -> dict:
        for k, v in mapping.items():
            test = {item: tracker.get(item, []) for item in v}
            mapping[k] = get_copies(test)

        return mapping

    # Flatten a given dict into a list of all keys and values
    def flatten(mapping: dict) -> list[int]:
        result = []

        for key in sorted(mapping.keys()):
            result.append(key)
            result.extend(flatten(mapping[key]))

        return result

    flattened = flatten(get_copies(tracker))
    print(len(flattened))


if __name__ == "__main__":
    part_one()
    part_two()
