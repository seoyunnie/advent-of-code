import textwrap

from advent_of_code.puzzles.year_2025 import day_05


class TestSolution:
    _PUZZLE_INPUT = day_05.parse(
        textwrap.dedent("""\
            3-5
            10-14
            16-20
            12-18

            1
            5
            8
            11
            17
            32
        """)
    )

    def test_part_1(self) -> None:
        assert day_05.solve_part_1(self._PUZZLE_INPUT) == 3

    def test_part_2(self) -> None:
        assert day_05.solve_part_2(self._PUZZLE_INPUT) == 14
