import textwrap

from advent_of_code.puzzles.year_2024 import day_06


class TestSolution:
    _PUZZLE_INPUT = day_06.parse(
        textwrap.dedent("""\
            ....#.....
            .........#
            ..........
            ..#.......
            .......#..
            ..........
            .#..^.....
            ........#.
            #.........
            ......#...
        """)
    )

    def test_part_1(self) -> None:
        assert day_06.solve_part_1(self._PUZZLE_INPUT) == 41

    def test_part_2(self) -> None:
        assert day_06.solve_part_2(self._PUZZLE_INPUT) == 6
