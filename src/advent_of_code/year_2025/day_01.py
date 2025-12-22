# ruff: noqa: FURB118

type ParsedInput = tuple[int, int]

_INITIAL_DIAL_POSITION = 50


def parse(puzzle_in: str) -> ParsedInput:
    anticlockwise_key = "L"

    dial_pos = _INITIAL_DIAL_POSITION

    zero_crosses = 0
    zero_hits = 0

    for line in puzzle_in.splitlines():
        rotation = int(line[1:])

        if line[0] == anticlockwise_key:
            rotation = -rotation

        if rotation > 0:
            zero_hits += ((rotation - (100 - dial_pos)) // 100) + 1
        else:
            zero_hits += (abs(rotation) - dial_pos) // 100

            if dial_pos != 0:
                zero_hits += 1

        dial_pos = (dial_pos + rotation) % 100

        if dial_pos == 0:
            zero_crosses += 1

    return zero_crosses, zero_hits


def solve_part_1(parsed_in: ParsedInput) -> int:
    return parsed_in[0]


def solve_part_2(parsed_in: ParsedInput) -> int:
    return parsed_in[1]
