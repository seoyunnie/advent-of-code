import textwrap

from advent_of_code.puzzles.year_2025 import day_03


class TestSolution:
    _PUZZLE_INPUT = day_03.parse(
        textwrap.dedent("""\
            987654321111111
            811111111111119
            234234234234278
            818181911112111
        """)
    )

    def test_part_1(self) -> None:
        assert day_03.solve_part_1(self._PUZZLE_INPUT) == 357

    def test_part_2(self) -> None:
        assert day_03.solve_part_2(self._PUZZLE_INPUT) == 3121910778619
