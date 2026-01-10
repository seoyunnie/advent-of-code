import collections

type ParsedInput = tuple[list[int], list[int]]


def parse(puzzle_in: str) -> ParsedInput:
    left_ids: list[int] = []
    right_ids: list[int] = []

    for line in puzzle_in.splitlines():
        left_id, right_id = line.split(maxsplit=1)

        left_ids.append(int(left_id))
        right_ids.append(int(right_id))

    return left_ids, right_ids


def solve_part_1(parsed_in: ParsedInput) -> int:
    left_ids, right_ids = parsed_in

    return sum(abs(left_id - right_id) for left_id, right_id in zip(sorted(left_ids), sorted(right_ids), strict=True))


def solve_part_2(parsed_in: ParsedInput) -> int:
    left_ids, right_ids = parsed_in
    right_id_counter = collections.Counter(right_ids)

    return sum(left_id * right_id_counter[left_id] for left_id in left_ids)
