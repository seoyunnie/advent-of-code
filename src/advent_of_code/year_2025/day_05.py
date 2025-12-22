type _Range = tuple[int, int]

type ParsedInput = tuple[list[_Range], tuple[int, ...]]


def parse(puzzle_in: str) -> ParsedInput:
    fresh_id_range_lines, id_lines = puzzle_in.split("\n\n")

    rng_sep = "-"

    return (
        [
            (int(start), int(end))
            for start, end in (line.split(rng_sep, maxsplit=1) for line in fresh_id_range_lines.splitlines())
        ],
        tuple(map(int, id_lines.splitlines())),
    )


def solve_part_1(parsed_in: ParsedInput) -> int:
    fresh_id_ranges, ids = parsed_in

    return sum(1 for i in ids if any(start <= i <= end for start, end in fresh_id_ranges))


type _MutableRange = list[int]


def solve_part_2(parsed_in: ParsedInput) -> int:
    fresh_id_ranges, _ = parsed_in
    fresh_id_ranges.sort()

    merged_ranges: list[_MutableRange] = []

    for start, end in fresh_id_ranges:
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    return sum((end - start) + 1 for start, end in merged_ranges)
