from typing import TYPE_CHECKING

import numpy as np
from scipy import optimize

if TYPE_CHECKING:
    from collections.abc import Collection, Sequence

type _Button = set[int]
type _MachineManual = tuple[list[bool], list[_Button], list[int]]

type ParsedInput = list[_MachineManual]


def parse(puzzle_in: str) -> ParsedInput:
    on_indicator_key = "#"

    sep = ","

    machine_manuals: list[_MachineManual] = []

    for line in puzzle_in.splitlines():
        indicators, *buttons, joltages = line.split()

        machine_manuals.append(
            (
                [key == on_indicator_key for key in indicators[1:-1]],
                [set(map(int, btn[1:-1].split(sep))) for btn in buttons],
                list(map(int, joltages[1:-1].split(sep))),
            )
        )

    return machine_manuals


def _get_min_button_press_count(
    goals: Sequence[int | bool], buttons: Collection[_Button], *, part_1: bool = False
) -> float:
    btn_cnt = len(buttons)
    goal_cnt = len(goals)

    btn_press_costs = [1] * btn_cnt
    constraint_matrix = [[i in btn for btn in buttons] for i in range(goal_cnt)]
    bounds: list[tuple[float | None, float | None]] = [(0, None)] * btn_cnt

    if part_1:
        btn_press_costs += [0] * goal_cnt
        constraint_matrix = np.hstack([constraint_matrix, -2 * np.eye(goal_cnt)])
        bounds += [(None, None)] * goal_cnt

    btn_press_cnt = optimize.linprog(
        btn_press_costs, A_eq=constraint_matrix, b_eq=goals, bounds=bounds, integrality=1
    ).fun

    if btn_press_cnt is None:
        assertion_msg = "Impossible under normal circumstances"

        raise AssertionError(assertion_msg)

    return btn_press_cnt


def solve_part_1(parsed_in: ParsedInput) -> int:
    return int(
        sum(_get_min_button_press_count(indicators, buttons, part_1=True) for indicators, buttons, _ in parsed_in)
    )


def solve_part_2(parsed_in: ParsedInput) -> int:
    return int(sum(_get_min_button_press_count(joltage, buttons) for _, buttons, joltage in parsed_in))
