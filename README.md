# Advent of Code

[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fseoyunnie%2Fadvent-of-code%2Fmain%2Fpyproject.toml&logo=python&label=Python&color=3776ab)](https://www.python.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff/)

My solutions for [Advent of Code](https://adventofcode.com/) problems throughout the years. The solutions are written in
Python and are not made with speed or memory efficiency in mind. I try to first solve the problems on my own, either
through algorithms or brute force, then view and/or copy other people's solutions to further improve my own.

I try to solve as many days as possible during the event, but stop when the solutions are beyond me. I try to solve the
remaining days after the event when I have the time.

## Setup

### Install Dependencies

```shell
uv sync
```

### Add Puzzle Inputs

Download the puzzle input files from [adventofcode.com](https://adventofcode.com/) and place them in the
[`inputs`](./inputs/) folder.

File names should follow this format:

```text
day_(0[1-9]|1[0-9]|2[0-5])\.txt
```

Examples:

```text
day_01.txt
day_12.txt
day_23.txt
```

## Usage

Shows the answers to the puzzles for the given day(s) of the given year(s):

```shell
uv run solve -y  YEAR [YEAR ...] -d DAY [DAY ...]
```

Examples:

```shell
uv run solve -y 2025 -d 1
uv run solve -y 2024 2025 -d 1 2
```
