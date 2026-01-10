type ParsedInput = list[str]

_FREE_SPACE_BLOCK_KEY = "."


def parse(puzzle_in: str) -> ParsedInput:
    file_id = 0
    is_free_space = False

    disk_map: list[str] = []

    for digit in puzzle_in.strip():
        key = str(file_id) if not is_free_space else _FREE_SPACE_BLOCK_KEY

        disk_map.extend(key for _ in range(int(digit)))

        if is_free_space := not is_free_space:
            file_id += 1

    return disk_map


def solve_part_1(parsed_in: ParsedInput) -> int:
    disk_map = list(parsed_in)

    for i, block in enumerate(disk_map):
        if block == _FREE_SPACE_BLOCK_KEY and i < len(disk_map):
            while i < len(disk_map):
                if (rear_file_block := disk_map.pop()) != _FREE_SPACE_BLOCK_KEY:
                    disk_map[i] = rear_file_block

                    break

    return sum(int(block) * i for i, block in enumerate(disk_map) if block != _FREE_SPACE_BLOCK_KEY)


def solve_part_2(parsed_in: ParsedInput) -> int:
    disk_map = parsed_in
    disk_map_len = len(disk_map)

    front_idx = 0

    free_spaces: list[list[int]] = []

    while front_idx < disk_map_len:
        if disk_map[front_idx] == _FREE_SPACE_BLOCK_KEY:
            start = front_idx

            while front_idx < disk_map_len and disk_map[front_idx] == _FREE_SPACE_BLOCK_KEY:
                front_idx += 1

            free_spaces.append([start, front_idx - start])
        else:
            front_idx += 1

    rear_idx = -1

    while rear_idx >= -disk_map_len:
        if disk_map[rear_idx] == _FREE_SPACE_BLOCK_KEY:
            rear_idx -= 1

            continue

        file = [rear_idx]

        while (rear_idx := rear_idx - 1) >= -disk_map_len and disk_map[rear_idx] == disk_map[rear_idx + 1]:
            file.append(rear_idx)

        file_block_cnt = len(file)

        free_space = next((free_space for free_space in free_spaces if free_space[1] >= file_block_cnt), None)

        if free_space is not None and disk_map_len + file[0] > free_space[0]:
            for i in file:
                disk_map[free_space[0]] = disk_map[i]
                disk_map[i] = _FREE_SPACE_BLOCK_KEY

                free_space[0] += 1
                free_space[1] -= 1

    return sum(int(block) * i for i, block in enumerate(disk_map) if block != _FREE_SPACE_BLOCK_KEY)
