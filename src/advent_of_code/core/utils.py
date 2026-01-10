import time
from typing import TYPE_CHECKING

from colorama import Fore, Style

if TYPE_CHECKING:
    from types import TracebackType
    from typing import Self

_MESSAGE_DECORATIONS = ("├─", "└─")


def print_section(year: int, day: int, *msgs: str | None, is_err: bool = False) -> None:
    print(f"{Style.BRIGHT}{Fore.RED if is_err else Fore.YELLOW}{year} Day {day}{Style.RESET_ALL}")

    filtered_msgs = [msg for msg in msgs if msg is not None]

    if not filtered_msgs:
        return

    last_idx = len(filtered_msgs) - 1

    for i, msg in enumerate(filtered_msgs):
        print(f"{_MESSAGE_DECORATIONS[i == last_idx]} {msg}")


class Timer:
    start: float
    end: float
    elapsed: float

    def __enter__(self) -> Self:
        self.start = time.perf_counter()

        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
