import operator
import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Collection, Sequence

type _Equation = list[int]

type ParsedInput = list[_Equation]


def parse(puzzle_in: str) -> ParsedInput:
    num_pattern = re.compile(r"\d+")

    return [list(map(int, num_pattern.findall(line))) for line in puzzle_in.splitlines()]


type _Operation = Callable[[int, int], int]


def _is_possible(
    start_operand: int,
    remaining_operands: Sequence[int],
    start_op: _Operation,
    ops: Collection[_Operation],
    test_val: int,
) -> bool:
    remaining_operand_cnt = len(remaining_operands)

    op_stack = [(start_op(start_operand, remaining_operands[0]), 1)]

    while op_stack:
        curr_val, next_operand_idx = op_stack.pop()

        if curr_val > test_val:
            continue

        if next_operand_idx == remaining_operand_cnt:
            if curr_val == test_val:
                return True

            continue

        next_operand = remaining_operands[next_operand_idx]

        for op in ops:
            if (next_val := op(curr_val, next_operand)) <= test_val:
                op_stack.append((next_val, next_operand_idx + 1))  # noqa: PERF401

    return False


def _solve(equations: Collection[_Equation], *, concatenate: bool = False) -> int:
    possible_test_vals_sum = 0

    ops: list[_Operation] = [operator.add, operator.mul]

    if concatenate:
        ops.append(lambda a, b: a * (10 ** len(str(b))) + b)

    for equation in equations:
        test_val, start_operand, *remaining_operands = equation

        if any(_is_possible(start_operand, remaining_operands, op, ops, test_val) for op in ops):
            possible_test_vals_sum += test_val

    return possible_test_vals_sum


def solve_part_1(parsed_in: ParsedInput) -> int:
    return _solve(parsed_in)


def solve_part_2(parsed_in: ParsedInput) -> int:
    return _solve(parsed_in, concatenate=True)
