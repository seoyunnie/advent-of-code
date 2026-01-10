import textwrap

from advent_of_code.puzzles.year_2025 import day_10


class TestSolution:
    _PUZZLE_INPUT = day_10.parse(
        textwrap.dedent("""\
            [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
            [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
            [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
        """)
    )

    def test_part_1(self) -> None:
        assert day_10.solve_part_1(self._PUZZLE_INPUT) == 7

    def test_part_2(self) -> None:
        assert day_10.solve_part_2(self._PUZZLE_INPUT) == 33
