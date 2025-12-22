import argparse

from colorama import just_fix_windows_console

from . import year_2023, year_2024, year_2025
from .utils import Solution, print_message

_OLD_EVENT_DAY_COUNT = 25
_NEW_EVENT_DAY_COUNT = 12
_TRANSITION_YEAR = 2025


def main() -> None:
    solutions_by_year = {2023: year_2023, 2024: year_2024, 2025: year_2025}

    evt_years = tuple(solutions_by_year.keys())
    evt_days = tuple(range(1, _OLD_EVENT_DAY_COUNT + 1))

    parser = argparse.ArgumentParser(description="Shows the answers to Advent of Code puzzles")
    parser.add_argument(
        "-y",
        "--year",
        nargs="+",
        type=int,
        choices=evt_years,
        required=True,
        help="set the years to get the puzzles from",
        metavar="YEAR",
    )
    parser.add_argument(
        "-d",
        "--day",
        nargs="+",
        type=int,
        choices=evt_days,
        required=True,
        help="set the days to show the answers of",
        metavar="DAY",
    )

    args = parser.parse_args()

    just_fix_windows_console()

    for i, year in enumerate(args.year):
        solutions = next(v for k, v in solutions_by_year.items() if k == year)

        for day in args.day:
            try:
                Solution(year, day, getattr(solutions, f"day_{day:02d}")).run()
            except AttributeError:
                print_message(
                    year,
                    day,
                    f"The number of event days had been reduced to {_NEW_EVENT_DAY_COUNT} since {_TRANSITION_YEAR}"
                    if year >= _TRANSITION_YEAR and day > _NEW_EVENT_DAY_COUNT
                    else "The puzzle has not been solved",
                    is_err=True,
                )

        if i < len(args.year) - 1:
            print()
