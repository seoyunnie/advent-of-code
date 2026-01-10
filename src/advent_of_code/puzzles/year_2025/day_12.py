type ParsedInput = int


def parse(puzzle_in: str) -> ParsedInput:
    dims_sep = "x"

    region_cnt = 0

    for line in puzzle_in.rsplit("\n\n", maxsplit=1)[-1].splitlines():
        dims, *shape_counts = line.split()
        x, y = map(int, dims[:-1].split(dims_sep, maxsplit=1))

        if x * y >= 9 * sum(map(int, shape_counts)):
            region_cnt += 1

    return region_cnt


def solve_part_1(parsed_in: ParsedInput) -> int:
    return parsed_in


def solve_part_2(parsed_in: ParsedInput) -> None:
    pass
