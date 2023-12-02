def parse_input(file_name: str) -> list[str]:
    with open(file_name) as f:
        return [line for line in f.read().split("\n") if line.strip() != ""]
