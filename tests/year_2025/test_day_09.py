import textwrap

from advent_of_code.puzzles.year_2025 import day_09


class TestSolution:
    _PUZZLE_INPUT = day_09.parse(
        textwrap.dedent("""\
            7,1
            11,1
            11,7
            9,7
            9,5
            2,5
            2,3
            7,3
        """)
    )

    def test_part_1(self) -> None:
        assert day_09.solve_part_1(self._PUZZLE_INPUT) == 50

    def test_part_2(self) -> None:
        assert day_09.solve_part_2(self._PUZZLE_INPUT) == 24
