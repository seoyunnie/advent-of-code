import textwrap

from advent_of_code.puzzles.year_2025 import day_06


class TestSolution:
    _PUZZLE_INPUT = day_06.parse(
        textwrap.dedent("""\
            123 328  51 64
             45 64  387 23
              6 98  215 314
            *   +   *   +
        """)
    )

    def test_part_1(self) -> None:
        assert day_06.solve_part_1(self._PUZZLE_INPUT) == 4277556

    def test_part_2(self) -> None:
        assert day_06.solve_part_2(self._PUZZLE_INPUT) == 3263827
