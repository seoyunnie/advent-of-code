import functools

type ParsedInput = dict[str, list[str]]


def parse(puzzle_in: str) -> ParsedInput:
    lines = [line.split() for line in puzzle_in.splitlines()]

    return {device[:-1]: neighbors for device, *neighbors in lines}


_START_DEVICES = ("you", "svr")
_END_DEVICE = "out"


def solve_part_1(parsed_in: ParsedInput) -> int:
    @functools.cache
    def get_path_count(device: str) -> int:
        if device == _END_DEVICE:
            return True

        return sum(get_path_count(neighbor) for neighbor in parsed_in[device])

    return get_path_count(_START_DEVICES[0])


_REQUIRED_DEVICES = ("dac", "fft")


def solve_part_2(parsed_in: ParsedInput) -> int:
    @functools.cache
    def get_path_count(device: str, dac_seen: bool = False, fft_seen: bool = False) -> int:  # noqa: FBT001, FBT002
        dac_seen = dac_seen or device == _REQUIRED_DEVICES[0]
        fft_seen = fft_seen or device == _REQUIRED_DEVICES[1]

        if device == _END_DEVICE:
            return dac_seen and fft_seen

        return sum(get_path_count(neighbor, dac_seen, fft_seen) for neighbor in parsed_in[device])

    return get_path_count(_START_DEVICES[1])
