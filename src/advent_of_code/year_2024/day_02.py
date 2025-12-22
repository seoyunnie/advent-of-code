import itertools

type _Report = list[int]

type ParsedInput = list[_Report]


def parse(puzzle_in: str) -> ParsedInput:
    return [list(map(int, report.split())) for report in puzzle_in.splitlines()]


_MIN_LEVEL_DIFFERENCE = 1
_MAX_LEVEL_DIFFERENCE = 3


def _is_safe(report: _Report) -> bool:
    return all(
        _MIN_LEVEL_DIFFERENCE <= abs(a - b) <= _MAX_LEVEL_DIFFERENCE for a, b in itertools.pairwise(report)
    ) and (report == sorted(report) or report == sorted(report, reverse=True))


def solve_part_1(parsed_in: ParsedInput) -> int:
    return sum(1 for report in parsed_in if _is_safe(report))


def solve_part_2(parsed_in: ParsedInput) -> int:
    return sum(1 for report in parsed_in if any(_is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))))
