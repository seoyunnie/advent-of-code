# ruff: noqa: FURB118

import itertools
import math
from typing import cast

from scipy.cluster import hierarchy

type ParsedInput = tuple[int, int]

type _Coordinates3D = tuple[int, int, int]

_BOX_PAIR_COUNT = 1000
_TEST_BOX_PAIR_COUNT = 10


def parse(puzzle_in: str, *, is_testing: bool = False) -> ParsedInput:
    box_coords = cast("list[_Coordinates3D]", [tuple(map(int, line.split(","))) for line in puzzle_in.splitlines()])

    connections = sorted(itertools.combinations(box_coords, 2), key=lambda p: math.dist(*p))

    circuits = hierarchy.DisjointSet(box_coords)
    circuit_sizes_product: int | None = None

    conn: tuple[_Coordinates3D, _Coordinates3D] | None = None

    for i, conn in enumerate(connections):
        if i == (_TEST_BOX_PAIR_COUNT if is_testing else _BOX_PAIR_COUNT):
            circuit_sizes_product = math.prod(sorted(map(len, circuits.subsets()))[-3:])

        circuits.merge(*conn)

        if circuits.n_subsets == 1:
            break

    if circuit_sizes_product is None or conn is None:
        assertion_msg = "Impossible under normal circumstances"

        raise AssertionError(assertion_msg)

    return circuit_sizes_product, conn[0][0] * conn[1][0]


def solve_part_1(parsed_in: ParsedInput) -> int:
    return parsed_in[0]


def solve_part_2(parsed_in: ParsedInput) -> int:
    return parsed_in[1]
