import itertools
from typing import cast

import networkx as nx

type _OrderingRule = tuple[int, int]
type _Update = tuple[int, ...]

type ParsedInput = tuple[list[_OrderingRule], list[_Update], list[_Update]]


def parse(puzzle_in: str) -> ParsedInput:
    ordering_rule_lines, update_lines = puzzle_in.split("\n\n")

    rule_sep = "|"
    ordering_rules = cast(
        "list[_OrderingRule]",
        [tuple(map(int, line.split(rule_sep, maxsplit=1))) for line in ordering_rule_lines.splitlines()],
    )

    update_sep = ","
    updates: list[_Update] = [tuple(map(int, line.split(update_sep))) for line in update_lines.splitlines()]

    unsorted_updates: list[_Update] = []

    for update in updates:
        page_to_idx = {page: i for i, page in enumerate(update)}

        if any(a in page_to_idx and b in page_to_idx and page_to_idx[a] > page_to_idx[b] for a, b in ordering_rules):
            unsorted_updates.append(update)

    return ordering_rules, updates, unsorted_updates


def solve_part_1(parsed_in: ParsedInput) -> int:
    _, updates, unsorted_updates = parsed_in

    return sum(update[len(update) // 2] for update in updates if update not in unsorted_updates)


def solve_part_2(parsed_in: ParsedInput) -> int:
    ordering_rules, _, unsorted_updates = parsed_in

    G = nx.DiGraph(ordering_rules)  # noqa: N806

    return sum(
        next(itertools.islice(nx.topological_sort(cast("nx.DiGraph[int]", G.subgraph(update))), len(update) // 2, None))
        for update in unsorted_updates
    )
