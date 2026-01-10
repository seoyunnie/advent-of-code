import textwrap

from advent_of_code.puzzles.year_2025 import day_11


class TestSolution:
    def test_part_1(self) -> None:
        parsed_in = day_11.parse(
            textwrap.dedent("""\
            aaa: you hhh
            you: bbb ccc
            bbb: ddd eee
            ccc: ddd eee fff
            ddd: ggg
            eee: out
            fff: out
            ggg: out
            hhh: ccc fff iii
            iii: out
        """)
        )

        assert day_11.solve_part_1(parsed_in) == 5

    def test_part_2(self) -> None:
        parsed_in = day_11.parse(
            textwrap.dedent("""\
            svr: aaa bbb
            aaa: fft
            fft: ccc
            bbb: tty
            tty: ccc
            ccc: ddd eee
            ddd: hub
            hub: fff
            eee: dac
            dac: fff
            fff: ggg hhh
            ggg: out
            hhh: out
        """)
        )

        assert day_11.solve_part_2(parsed_in) == 2
