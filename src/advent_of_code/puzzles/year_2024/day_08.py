import collections
import itertools

type _AntennaToPositions = dict[str, list[complex]]

type ParsedInput = tuple[int, int, _AntennaToPositions]


def parse(puzzle_in: str) -> ParsedInput:
    map_rows = puzzle_in.splitlines()
    map_empty_keys = {".", "#"}

    antenna_to_positions: collections.defaultdict[str, list[complex]] = collections.defaultdict(list)

    for y, row in enumerate(map_rows):
        for x, key in enumerate(row):
            if key not in map_empty_keys:
                antenna_to_positions[key].append(y + (1j * x))

    return len(map_rows[0]), len(map_rows), antenna_to_positions


def _get_antinode_count(
    map_w: int, map_h: int, antenna_to_positions: _AntennaToPositions, *, ignore_distance: bool = False
) -> int:
    antinodes: set[complex] = set()

    for positions in antenna_to_positions.values():
        if ignore_distance:
            antinodes.update(positions)

        for a, b in itertools.permutations(positions, 2):
            if ignore_distance:
                delta = b - a
                pos = b

                while True:
                    pos += delta

                    if not (0 <= pos.real < map_h and 0 <= pos.imag < map_w):
                        break

                    antinodes.add(pos)
            elif 0 <= (pos := (2 * b) - a).real < map_h and 0 <= pos.imag < map_w:
                antinodes.add(pos)

    return len(antinodes)


def solve_part_1(parsed_in: ParsedInput) -> int:
    return _get_antinode_count(*parsed_in)


def solve_part_2(parsed_in: ParsedInput) -> int:
    return _get_antinode_count(*parsed_in, ignore_distance=True)
