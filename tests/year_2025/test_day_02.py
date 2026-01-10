from advent_of_code.puzzles.year_2025 import day_02


class TestSolution:
    _PUZZLE_INPUT = day_02.parse(
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    )

    def test_part_1(self) -> None:
        assert day_02.solve_part_1(self._PUZZLE_INPUT) == 1227775554

    def test_part_2(self) -> None:
        assert day_02.solve_part_2(self._PUZZLE_INPUT) == 4174379265
