import itertools
from typing import cast

from shapely import Polygon, box

type _Coordinates = tuple[int, int]

type ParsedInput = tuple[list[_Coordinates], list[tuple[int, int, int, int]], list[int]]


def parse(puzzle_in: str) -> ParsedInput:
    coord_sep = ","
    coords = cast("list[_Coordinates]", [tuple(map(int, line.split(coord_sep))) for line in puzzle_in.splitlines()])

    bounds = [
        (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in itertools.combinations(coords, 2)
    ]
    areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in bounds]

    return coords, bounds, areas


def solve_part_1(parsed_in: ParsedInput) -> int:
    _, _, areas = parsed_in

    return max(areas)


def solve_part_2(parsed_in: ParsedInput) -> int:
    coords, bounds, areas = parsed_in

    pol = Polygon(coords)
    min_x, min_y, max_x, max_y = pol.bounds

    largest_area = 0

    for (x1, y1, x2, y2), area in zip(bounds, areas, strict=True):
        if x1 < min_x or y1 < min_y or x2 > max_x or y2 > max_y or area <= largest_area:
            continue

        if pol.contains(box(x1, y1, x2, y2)):
            largest_area = area

    return largest_area
