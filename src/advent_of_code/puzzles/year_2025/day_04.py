type ParsedInput = list[int]

_MAX_ADJACENT_ROLL_COUNT = 4


def parse(puzzle_in: str) -> ParsedInput:
    roll_key = "@"
    roll_positions = {
        y + (1j * x) for y, row in enumerate(puzzle_in.splitlines()) for x, key in enumerate(row) if key == roll_key
    }

    adjacent_pos_deltas: set[complex] = {-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j}

    removed_roll_counts: list[int] = []

    while removable_roll_positions := {
        pos
        for pos in roll_positions
        if len({pos + delta for delta in adjacent_pos_deltas} & roll_positions) < _MAX_ADJACENT_ROLL_COUNT
    }:
        removed_roll_counts.append(len(removable_roll_positions))
        roll_positions -= removable_roll_positions

    return removed_roll_counts


def solve_part_1(parsed_in: ParsedInput) -> int:  # noqa: FURB118
    return parsed_in[0]


def solve_part_2(parsed_in: ParsedInput) -> int:
    return sum(parsed_in)
