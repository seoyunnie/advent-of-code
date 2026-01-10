import math
import re

type _GameRecord = dict[str, int]

type ParsedInput = list[_GameRecord]


def parse(puzzle_in: str) -> ParsedInput:
    sep_pattern = re.compile(r"[;,:]")

    game_recs: list[_GameRecord] = []

    for line in puzzle_in.splitlines():
        cubes = sep_pattern.sub("", line).split()[2:]
        game_rec: _GameRecord = {}

        for i in range(0, len(cubes), 2):
            if (cnt := int(cubes[i])) > game_rec.get(color := cubes[i + 1], 0):
                game_rec[color] = cnt

        game_recs.append(game_rec)

    return game_recs


_MAX_GAME_RECORD: _GameRecord = {"red": 12, "green": 13, "blue": 14}


def solve_part_1(parsed_in: ParsedInput) -> int:
    return sum(
        i + 1
        for i, game_rec in enumerate(parsed_in)
        if all(cnt <= _MAX_GAME_RECORD[color] for color, cnt in game_rec.items())
    )


def solve_part_2(parsed_in: ParsedInput) -> int:
    return sum(math.prod(game_rec.values()) for game_rec in parsed_in)
