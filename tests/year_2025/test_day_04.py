import textwrap

from advent_of_code.puzzles.year_2025 import day_04


class TestSolution:
    _PUZZLE_INPUT = day_04.parse(
        textwrap.dedent("""\
            ..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.
        """)
    )

    def test_part_1(self) -> None:
        assert day_04.solve_part_1(self._PUZZLE_INPUT) == 13

    def test_part_2(self) -> None:
        assert day_04.solve_part_2(self._PUZZLE_INPUT) == 43
