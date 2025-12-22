import re

type ParsedInput = str


def parse(puzzle_in: str) -> ParsedInput:
    return puzzle_in


_DIGIT_PATTERN = re.compile(r"\d")


def _calibrate(calibration_doc: str) -> int:
    return sum(int((digits := _DIGIT_PATTERN.findall(line))[0] + digits[-1]) for line in calibration_doc.splitlines())


def solve_part_1(parsed_in: ParsedInput) -> int:
    return _calibrate(parsed_in)


def solve_part_2(parsed_in: ParsedInput) -> int:
    return _calibrate(
        parsed_in.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
