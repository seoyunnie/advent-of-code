from typing import TYPE_CHECKING, Protocol, overload

from colorama import Fore, Style

from .utils import Timer, print_section

if TYPE_CHECKING:
    import pathlib
    from typing import Any


class Puzzle[T](Protocol):
    type ParsedInput = T

    @overload
    def parse(self, puzzle_in: str) -> ParsedInput: ...
    @overload
    def parse(self, puzzle_in: str, *, is_testing: bool) -> ParsedInput: ...

    def solve_part_1(self, parsed_in: ParsedInput) -> int: ...

    def solve_part_2(self, parsed_in: ParsedInput) -> int | None: ...


class PuzzleRunner:
    year: int
    day: int

    module: Puzzle[Any]
    inputs_base_path: pathlib.Path

    def __init__(self, year: int, day: int, module: Puzzle[Any], inputs_base_path: pathlib.Path) -> None:
        self.year = year
        self.day = day

        self.module = module
        self.inputs_base_path = inputs_base_path

    def run(self) -> None:
        puzzle_in: str

        try:
            puzzle_in = self.inputs_base_path.joinpath(f"year_{self.year}", f"day_{self.day:02d}.txt").read_text(
                encoding="utf-8"
            )
        except FileNotFoundError:
            print_section(self.year, self.day, "The puzzle's input file could not be found", is_err=True)

            return

        with Timer() as t:
            parsed_in = self.module.parse(puzzle_in)
            part_1_answer = self.module.solve_part_1(parsed_in)
            part_2_answer = self.module.solve_part_2(parsed_in)

        print_section(
            self.year,
            self.day,
            f"Part 1: {Style.BRIGHT}{Fore.GREEN}{part_1_answer}{Style.RESET_ALL}",
            f"Part 2: {Style.BRIGHT}{Fore.GREEN}{part_2_answer}{Style.RESET_ALL}"
            if part_2_answer is not None
            else None,
            f"Elapsed Time: {Style.BRIGHT}{Fore.CYAN}{t.elapsed:,.6f} s{Style.RESET_ALL}",
        )
