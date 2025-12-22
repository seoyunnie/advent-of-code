type ParsedInput = list[int]


def parse(puzzle_in: str) -> ParsedInput:
    splitter_key = "^"
    splitter_xs = [x for row in puzzle_in.splitlines() for x, key in enumerate(row) if key == splitter_key]

    timeline_counts = [1] + ([0] * (len(splitter_xs) - 1))

    for i, x in enumerate(splitter_xs):
        for j in range(i - 1, -1, -1):
            prev_x = splitter_xs[j]

            if x == prev_x:
                break

            if abs(x - prev_x) == 1:
                timeline_counts[i] += timeline_counts[j]

    return timeline_counts


def solve_part_1(parsed_in: ParsedInput) -> int:
    return sum(1 for entry in parsed_in if entry > 0)


def solve_part_2(parsed_in: ParsedInput) -> int:
    return sum(parsed_in) + 1
