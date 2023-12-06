from itertools import islice


def parse_input(file_name: str, split_char: str = "\n") -> list[str]:
    with open(file_name) as f:
        return [section for section in f.read().split(split_char) if section.strip() != ""]


def batched(iterable, n):
    """
    Implementation of batched for python < 3.12 (https://docs.python.org/3/library/itertools.html#itertools.batched).
    """
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch
