# ruff: noqa: FURB118

type ParsedInput = tuple[int, int]


def parse(puzzle_in: str) -> ParsedInput:
    rng_sep = "-"

    invalid_ids_sum_1 = 0
    invalid_ids_sum_2 = 0

    for rng in puzzle_in.split(","):
        start, stop = rng.split(rng_sep, maxsplit=1)

        for i in range(int(start), int(stop) + 1):
            str_num = str(i)
            str_num_len = len(str_num)
            str_num_mid_idx = str_num_len // 2

            if str_num_len % 2 == 0 and str_num[str_num_mid_idx:] == str_num[:str_num_mid_idx]:
                invalid_ids_sum_1 += i

            if str_num_len > 1 and str_num in (str_num + str_num)[1:-1]:
                invalid_ids_sum_2 += i

    return invalid_ids_sum_1, invalid_ids_sum_2


def solve_part_1(parsed_in: ParsedInput) -> int:
    return parsed_in[0]


def solve_part_2(parsed_in: ParsedInput) -> int:
    return parsed_in[1]
