import argparse
import pathlib

from colorama import just_fix_windows_console

from .core.discovery import (
    NEW_EVENT_DAY_COUNT,
    OLD_EVENT_DAY_COUNT,
    TRANSITION_YEAR,
    PuzzleDayOutOfRangeError,
    PuzzleNotSolvedError,
    load_puzzle,
)
from .core.puzzle import PuzzleRunner
from .core.utils import print_section


def _format_error(err: PuzzleDayOutOfRangeError | PuzzleNotSolvedError) -> str:
    match err:
        case PuzzleDayOutOfRangeError(year=year, day=day):
            if year >= TRANSITION_YEAR and day <= OLD_EVENT_DAY_COUNT:
                return f"There are now only {NEW_EVENT_DAY_COUNT} event days since {TRANSITION_YEAR}"

            return f"There is no puzzle on day {day}"
        case PuzzleNotSolvedError():
            return "This puzzle has not been solved"


def main() -> None:
    parser = argparse.ArgumentParser(description="Shows the answers to Advent of Code puzzles")
    parser.add_argument(
        "-y", "--year", nargs="+", type=int, required=True, help="set the years to get the puzzles from"
    )
    parser.add_argument("-d", "--day", nargs="+", type=int, required=True, help="set the days to show the answers of")

    args = parser.parse_args()
    years, days = args.year, args.day

    just_fix_windows_console()

    inputs_dir = pathlib.Path("inputs").resolve()

    for i, year in enumerate(years):
        for day in days:
            try:
                PuzzleRunner(year, day, load_puzzle(year, day), inputs_dir).run()
            except (PuzzleDayOutOfRangeError, PuzzleNotSolvedError) as e:
                print_section(year, day, _format_error(e), is_err=True)

        if i < len(years) - 1:
            print()
