type ParsedInput = tuple[dict[complex, str], complex, set[complex], set[complex]]

_INITIAL_DELTA = -1
_DELTA_TURN_MODIFIER = -1j


def parse(puzzle_in: str) -> ParsedInput:
    map_positions = {y + (1j * x): key for y, row in enumerate(puzzle_in.splitlines()) for x, key in enumerate(row)}

    start_pos_key = "^"
    start_pos = next(pos for pos, key in map_positions.items() if key == start_pos_key)

    obstruction_key = "#"
    obstruction_positions = {pos for pos, key in map_positions.items() if key == obstruction_key}

    curr_pos = start_pos
    delta = _INITIAL_DELTA

    seen_positions: set[complex] = set()

    while curr_pos in map_positions:
        seen_positions.add(curr_pos)

        if curr_pos + delta in obstruction_positions:
            delta *= _DELTA_TURN_MODIFIER
        else:
            curr_pos += delta

    return map_positions, start_pos, obstruction_positions, seen_positions


def solve_part_1(parsed_in: ParsedInput) -> int:
    _, _, _, seen_positions = parsed_in

    return len(seen_positions)


def solve_part_2(parsed_in: ParsedInput) -> int:
    map_positions, start_pos, obstruction_positions, seen_positions = parsed_in

    def is_looping(new_obstruction_pos: complex) -> bool:
        new_obstruction_positions = obstruction_positions | {new_obstruction_pos}

        curr_pos = start_pos
        delta = _INITIAL_DELTA

        seen_states: set[tuple[complex, complex]] = set()

        while curr_pos in map_positions:
            state = (curr_pos, delta)

            if state in seen_states:
                return True

            seen_states.add(state)

            next_pos = curr_pos + delta

            if next_pos in new_obstruction_positions:
                delta *= _DELTA_TURN_MODIFIER
            else:
                curr_pos = next_pos

        return False

    return sum(1 for pos in seen_positions if is_looping(pos))
