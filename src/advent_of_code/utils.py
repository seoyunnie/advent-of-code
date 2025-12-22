import functools
import pathlib
import time
from os import path
from typing import TYPE_CHECKING, Protocol, overload

from colorama import Fore, Style

if TYPE_CHECKING:
    from typing import Any


class SolutionModule[T](Protocol):
    type ParsedInput = T

    @overload
    def parse(self, puzzle_in: str) -> ParsedInput: ...
    @overload
    def parse(self, puzzle_in: str, *, is_testing: bool) -> ParsedInput: ...

    def solve_part_1(self, parsed_int: ParsedInput) -> int: ...

    def solve_part_2(self, parsed_int: ParsedInput) -> int | None: ...


_MESSAGE_DECORATIONS = ("├─", "└─")


def print_message(year: int, day: int, *msgs: str, is_err: bool = False) -> None:
    print(f"{Style.BRIGHT}{Fore.RED if is_err else Fore.YELLOW}{year} Day {day}{Style.RESET_ALL}")

    for i, msg in enumerate(msgs):
        print(f"{_MESSAGE_DECORATIONS[i == len(msgs) - 1]} {msg}")


class Solution:
    def __init__(self, year: int, day: int, module: SolutionModule[Any]) -> None:
        self.year = year
        self.day = day
        self.module = module

    def run(self) -> None:
        print_msg = functools.partial(print_message, self.year, self.day)

        puzzle_in: str

        try:
            puzzle_in = pathlib.Path(path.join("inputs", f"year_{self.year}", f"day_{self.day:02d}.txt")).read_text(
                encoding="utf-8"
            )
        except FileNotFoundError:
            print_msg("The puzzle's input file could not be found", is_err=True)

            return

        start_time = time.perf_counter()

        parsed_in = self.module.parse(puzzle_in)
        part_1_answer = self.module.solve_part_1(parsed_in)
        part_2_answer = self.module.solve_part_2(parsed_in)

        end_time = time.perf_counter()
        elapsed_milliseconds = (end_time - start_time) * 1000

        print_msg(
            f"Part 1: {Style.BRIGHT}{Fore.GREEN}{part_1_answer}{Style.RESET_ALL}",
            f"Part 2: {Style.BRIGHT}{Fore.BLACK if part_2_answer is None else Fore.GREEN}{part_2_answer or 'N/A'}{
                Style.RESET_ALL
            }",
            f"Elapsed Time: {Style.BRIGHT}{Fore.CYAN}{elapsed_milliseconds:,.2f} ms{Style.RESET_ALL}",
        )
