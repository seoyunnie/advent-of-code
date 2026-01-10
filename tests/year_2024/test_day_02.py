import textwrap

from advent_of_code.puzzles.year_2024 import day_02


class TestSolution:
    _PUZZLE_INPUT = day_02.parse(
        textwrap.dedent("""\
            7 6 4 2 1
            1 2 7 8 9
            9 7 6 2 1
            1 3 2 4 5
            8 6 4 4 1
            1 3 6 7 9
        """)
    )

    def test_part_1(self) -> None:
        assert day_02.solve_part_1(self._PUZZLE_INPUT) == 2

    def test_part_2(self) -> None:
        assert day_02.solve_part_2(self._PUZZLE_INPUT) == 4
