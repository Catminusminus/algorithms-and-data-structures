from typing import List

from algorithms_and_data_structures import full_search
from typing import Dict


def solve_frog(list: List[int]) -> int:
    if list == []:
        return 0
    if len(list) == 1:
        return 0
    if len(list) == 2:
        return abs(list[0] - list[1])
    return min(
        solve_frog(list[:-1]) + abs(list[-1] - list[-2]),
        solve_frog(list[:-2]) + abs(list[-1] - list[-3]),
    )


def solve_frog_relaxation_1(list: List[int]) -> int:
    if list == []:
        return 0
    if len(list) == 1:
        return 0
    if len(list) == 2:
        return abs(list[0] - list[1])
    inf_value = float("inf")
    dp_values = [inf_value for _ in list]
    dp_values[0] = 0
    dp_values[1] = abs(list[0] - list[1])
    smaller_value = lambda a, b: a if a < b else b
    for i in range(2, len(list)):
        dp_values[i] = smaller_value(
            dp_values[i], dp_values[i - 1] + abs(list[i - 1] - list[i])
        )
        dp_values[i] = smaller_value(
            dp_values[i], dp_values[i - 2] + abs(list[i - 2] - list[i])
        )
    return dp_values[-1]


def solve_frog_relaxation_2(list: list[int]) -> int:
    if list == []:
        return 0
    if len(list) == 1:
        return 0
    if len(list) == 2:
        return abs(list[0] - list[1])
    inf_value = float("inf")
    dp_values = [inf_value for _ in list]
    dp_values[0] = 0
    dp_values[1] = abs(list[0] - list[1])
    smaller_value = lambda a, b: a if a < b else b
    for i in range(len(list) - 1):
        dp_values[i + 1] = smaller_value(
            dp_values[i + 1], dp_values[i] + abs(list[i + 1] - list[i])
        )
        if i < len(list) - 2:
            dp_values[i + 2] = smaller_value(
                dp_values[i + 2], dp_values[i] + abs(list[i + 2] - list[i])
            )
    return dp_values[-1]


def solve_frog_memorized(list: List[int], dp_values: Dict[int, int]) -> int:
    if list == []:
        return 0
    if len(list) == 1:
        return 0
    if len(list) == 2:
        return abs(list[0] - list[1])
    inf_value = float("inf")
    l = len(list) - 1
    if dp_values[l] < inf_value:
        return dp_values[l]
    dp_values[l] = min(
        solve_frog_memorized(list[:-1], dp_values) + abs(list[-1] - list[-2]),
        solve_frog_memorized(list[:-2], dp_values) + abs(list[-1] - list[-3]),
    )
    return dp_values[l]
