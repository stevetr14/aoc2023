def parse_input(file_name: str, split_char: str = "\n") -> list[str]:
    with open(file_name) as f:
        return [section for section in f.read().split(split_char) if section.strip() != ""]
