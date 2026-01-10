import textwrap

from advent_of_code.puzzles.year_2023 import day_01


class TestSolution:
    def test_part_1(self) -> None:
        parsed_in = day_01.parse(
            textwrap.dedent("""\
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
            """)
        )

        assert day_01.solve_part_1(parsed_in) == 142

    def test_part_2(self) -> None:
        parsed_in = textwrap.dedent("""\
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
        """)

        assert day_01.solve_part_2(parsed_in) == 281
