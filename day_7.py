from collections import Counter

from utils import parse_input


CARD_ORDER = "23456789TJQKA"
"""Card order from lowest to highest labels."""

CARD_ORDER_PART_2 = "J23456789TQKA"


def is_five_of_a_kind(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 5:
            return sorted(list(counter.values())) == [5]
        elif j_card == 4 or j_card == 1:
            return sorted(counter.values()) == [1, 4]
        elif j_card == 3 or j_card == 2:
            return sorted(counter.values()) == [2, 3]

    return list(Counter(hand_).values()) == [5]


def is_four_of_a_kind(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 4:
            return sorted(list(counter.values())) == [1, 4]
        elif j_card == 3 or j_card == 1:
            return sorted(counter.values()) == [1, 1, 3]
        elif j_card == 2:
            return sorted(list(counter.values())) == [1, 2, 2]

    return sorted(list(counter.values())) == [1, 4]


def is_full_house(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 3:
            return sorted(list(counter.values())) == [2, 3]
        elif j_card == 2 or j_card == 1:
            return sorted(counter.values()) == [1, 2, 2]

    return sorted(list(Counter(hand_).values())) == [2, 3]


def is_three_of_a_kind(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 3:
            return sorted(list(counter.values())) == [1, 1, 3]
        elif j_card == 2 or j_card == 1:
            return sorted(counter.values()) == [1, 1, 1, 2]

    return sorted(list(Counter(hand_).values())) == [1, 1, 3]


def is_two_pair(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 2:
            return sorted(list(counter.values())) == [1, 2, 2]
        if j_card == 1:
            return sorted(list(counter.values())) == [1, 1, 1, 2]

    return sorted(list(counter.values())) == [1, 2, 2]


def is_one_pair(hand_: str, use_joker: bool = False) -> bool:
    counter = Counter(hand_)
    j_card = counter.get("J")

    if use_joker:
        if j_card == 2:
            return sorted(list(counter.values())) == [1, 1, 1, 2]
        elif j_card == 1:
            return sorted(list(counter.values())) == [1, 1, 1, 1, 1]

    return sorted(list(counter.values())) == [1, 1, 1, 2]


def get_sorted_cards(cards: list[tuple[str, int]], use_joker: bool = False) -> list[tuple[str, int]]:
    card_order = CARD_ORDER_PART_2 if use_joker else CARD_ORDER
    return sorted(cards, key=lambda x: [card_order.index(c) for c in x[0]])


def part_one():
    lines = parse_input("day_7.txt")

    five_of_a_kind_cards = []
    four_of_a_kind_cards = []
    full_house_cards = []
    three_of_a_kind_cards = []
    two_pair_cards = []
    one_pair_cards = []
    high_cards = []

    total = 0

    for line in lines:
        hand, bid = line.split(" ")

        if is_five_of_a_kind(hand):
            five_of_a_kind_cards.append((hand, int(bid)))
        elif is_four_of_a_kind(hand):
            four_of_a_kind_cards.append((hand, int(bid)))
        elif is_full_house(hand):
            full_house_cards.append((hand, int(bid)))
        elif is_three_of_a_kind(hand):
            three_of_a_kind_cards.append((hand, int(bid)))
        elif is_two_pair(hand):
            two_pair_cards.append((hand, int(bid)))
        elif is_one_pair(hand):
            one_pair_cards.append((hand, int(bid)))
        else:
            high_cards.append((hand, int(bid)))

    sorted_cards = (
        get_sorted_cards(high_cards)
        + get_sorted_cards(one_pair_cards)
        + get_sorted_cards(two_pair_cards)
        + get_sorted_cards(three_of_a_kind_cards)
        + get_sorted_cards(full_house_cards)
        + get_sorted_cards(four_of_a_kind_cards)
        + get_sorted_cards(five_of_a_kind_cards)
    )

    # The lowest card start from rank 1
    for index, (card, bid) in enumerate(sorted_cards, start=1):
        total += bid * index
        print(index, card, bid)

    print("Part 1", total)


def part_two():
    lines = parse_input("day_7.txt")

    five_of_a_kind_cards = []
    four_of_a_kind_cards = []
    full_house_cards = []
    three_of_a_kind_cards = []
    two_pair_cards = []
    one_pair_cards = []
    high_cards = []

    total = 0

    for line in lines:
        hand, bid = line.split(" ")

        if is_five_of_a_kind(hand, use_joker=True):
            five_of_a_kind_cards.append((hand, int(bid)))
        elif is_four_of_a_kind(hand, use_joker=True):
            four_of_a_kind_cards.append((hand, int(bid)))
        elif is_full_house(hand, use_joker=True):
            full_house_cards.append((hand, int(bid)))
        elif is_three_of_a_kind(hand, use_joker=True):
            three_of_a_kind_cards.append((hand, int(bid)))
        elif is_two_pair(hand, use_joker=True):
            two_pair_cards.append((hand, int(bid)))
        elif is_one_pair(hand, use_joker=True):
            one_pair_cards.append((hand, int(bid)))
        else:
            high_cards.append((hand, int(bid)))

    sorted_cards = (
        get_sorted_cards(high_cards, use_joker=True)
        + get_sorted_cards(one_pair_cards, use_joker=True)
        + get_sorted_cards(two_pair_cards, use_joker=True)
        + get_sorted_cards(three_of_a_kind_cards, use_joker=True)
        + get_sorted_cards(full_house_cards, use_joker=True)
        + get_sorted_cards(four_of_a_kind_cards, use_joker=True)
        + get_sorted_cards(five_of_a_kind_cards, use_joker=True)
    )

    # The lowest card start from rank 1
    for index, (card, bid) in enumerate(sorted_cards, start=1):
        total += bid * index
        print(index, card, bid)

    print("Part 2", total)


if __name__ == "__main__":
    part_one()
    part_two()
