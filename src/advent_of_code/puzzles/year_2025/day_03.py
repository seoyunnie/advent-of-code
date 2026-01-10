type _Bank = tuple[int, ...]

type ParsedInput = list[_Bank]


def parse(puzzle_in: str) -> ParsedInput:
    return [tuple(map(int, bank)) for bank in puzzle_in.splitlines()]


def _get_max_joltage(bank: _Bank, battery_cnt: int) -> int:
    max_battery_cnt = len(bank)

    front_idx = 0

    joltage = 0

    for rear_idx in range(max_battery_cnt - battery_cnt, max_battery_cnt):
        largest_joltage = bank[front_idx]

        for i in range(front_idx + 1, rear_idx + 1):
            if bank[i] > largest_joltage:
                front_idx = i
                largest_joltage = bank[i]

        joltage = (joltage * 10) + bank[front_idx]

        front_idx += 1

    return joltage


_PART_1_BATTERY_COUNT = 2


def solve_part_1(parsed_in: ParsedInput) -> int:
    return sum(_get_max_joltage(bank, _PART_1_BATTERY_COUNT) for bank in parsed_in)


_PART_2_BATTERY_COUNT = 12


def solve_part_2(parsed_in: ParsedInput) -> int:
    return sum(_get_max_joltage(bank, _PART_2_BATTERY_COUNT) for bank in parsed_in)
