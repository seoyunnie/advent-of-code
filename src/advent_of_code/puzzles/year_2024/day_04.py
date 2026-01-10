type ParsedInput = dict[complex, str]


def parse(puzzle_in: str) -> ParsedInput:
    return {y + (1j * x): char for y, row in enumerate(puzzle_in.splitlines()) for x, char in enumerate(row)}


def solve_part_1(parsed_in: ParsedInput) -> int:
    adjacent_coord_deltas = (-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j)

    word_chars = ("X", "M", "A", "S")
    word_len = len(word_chars)

    word_cnt = 0

    for coord in parsed_in:
        for delta in adjacent_coord_deltas:
            for i in range(word_len):
                if parsed_in.get(coord + (i * delta)) != word_chars[i]:
                    break
            else:
                word_cnt += 1

    return word_cnt


def solve_part_2(parsed_in: ParsedInput) -> int:
    word_mid_char = "A"
    word_corner_chars = {"M", "S"}

    word_cnt = 0

    for coord in parsed_in:
        if parsed_in[coord] == word_mid_char and (
            set(
                corners := (
                    parsed_in.get(coord - 1 - 1j),
                    parsed_in.get(coord - 1 + 1j),
                    parsed_in.get(coord + 1 + 1j),
                    parsed_in.get(coord + 1 - 1j),
                )
            )
            == word_corner_chars
            and corners[0] != corners[2]
        ):
            word_cnt += 1

    return word_cnt
