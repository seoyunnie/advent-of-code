import textwrap

from advent_of_code.puzzles.year_2025 import day_01


class TestSolution:
    _PUZZLE_INPUT = day_01.parse(
        textwrap.dedent("""\
            L68
            L30
            R48
            L5
            R60
            L55
            L1
            L99
            R14
            L82
        """)
    )

    def test_part_1(self) -> None:
        assert day_01.solve_part_1(self._PUZZLE_INPUT) == 3

    def test_part_2(self) -> None:
        assert day_01.solve_part_2(self._PUZZLE_INPUT) == 6
