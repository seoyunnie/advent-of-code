import itertools
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

type _IterableOperation = Callable[[Iterable[int]], int]

type ParsedInput = tuple[list[list[str]], list[_IterableOperation]]


def parse(puzzle_in: str) -> ParsedInput:
    *num_lines, ops_line = puzzle_in.splitlines()

    key_to_op: dict[str, _IterableOperation] = {"+": sum, "*": math.prod}

    ops: list[_IterableOperation] = []

    front_indices: list[int] = []

    for i, key in enumerate(ops_line):
        if op := key_to_op.get(key):
            ops.append(op)

            front_indices.append(i)

    rear_indices = [i - 1 for i in front_indices[1:]] + [None]

    return [
        [line[front:rear] for line in num_lines] for front, rear in zip(front_indices, rear_indices, strict=True)
    ], ops


def _sum_worksheet_problems(nums: Iterable[Iterable[str]], ops: Iterable[_IterableOperation]) -> int:
    return sum(op(map(int, num_col)) for op, num_col in zip(ops, nums, strict=True))


def solve_part_1(parsed_in: ParsedInput) -> int:
    return _sum_worksheet_problems(*parsed_in)


def solve_part_2(parsed_in: ParsedInput) -> int:
    nums, ops = parsed_in
    nums = [map("".join, itertools.zip_longest(*num_col, fillvalue=" ")) for num_col in nums]

    return _sum_worksheet_problems(nums, ops)
