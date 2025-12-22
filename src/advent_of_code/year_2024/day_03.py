# ruff: noqa: FURB118

import re
from typing import cast

type ParsedInput = tuple[int, int]


def parse(puzzle_in: str) -> ParsedInput:
    is_multiplying = True

    results_sum = 0
    enabled_results_sum = 0

    for instruction, multiplier, multiplicand in cast(
        "list[tuple[str, str, str]]", re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", puzzle_in)
    ):
        if instruction.startswith("mul"):
            results_sum += (product := int(multiplier) * int(multiplicand))

            if is_multiplying:
                enabled_results_sum += product
        else:
            is_multiplying = instruction == "do()"

    return results_sum, enabled_results_sum


def solve_part_1(parsed_in: ParsedInput) -> int:
    return parsed_in[0]


def solve_part_2(parsed_in: ParsedInput) -> int:
    return parsed_in[1]
