from advent_of_code.puzzles.year_2024 import day_09


class TestSolution:
    _PUZZLE_INPUT = day_09.parse("2333133121414131402")

    def test_part_1(self) -> None:
        assert day_09.solve_part_1(self._PUZZLE_INPUT) == 1928

    def test_part_2(self) -> None:
        assert day_09.solve_part_2(self._PUZZLE_INPUT) == 2858
