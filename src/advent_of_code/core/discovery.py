import importlib
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from typing import Any

    from .puzzle import Puzzle

OLD_EVENT_DAY_COUNT = 25
NEW_EVENT_DAY_COUNT = 12
TRANSITION_YEAR = 2025


class PuzzleDayOutOfRangeError(Exception):
    year: int
    day: int

    def __init__(self, year: int, day: int) -> None:
        super().__init__(f"Puzzle day out of range: Day {day} ({year})")

        self.year = year
        self.day = day


class PuzzleNotSolvedError(Exception):
    year: int
    day: int

    def __init__(self, year: int, day: int) -> None:
        super().__init__(f"Puzzle not solved: Day {day} ({year})")

        self.year = year
        self.day = day


def load_puzzle(year: int, day: int) -> Puzzle[Any]:
    if day < 1 or day > OLD_EVENT_DAY_COUNT or (year >= TRANSITION_YEAR and day > NEW_EVENT_DAY_COUNT):
        raise PuzzleDayOutOfRangeError(year, day)

    try:
        return cast("Puzzle[Any]", importlib.import_module(f"advent_of_code.puzzles.year_{year}.day_{day:02d}"))
    except ModuleNotFoundError as e:
        raise PuzzleNotSolvedError(year, day) from e
