from typing import List, Dict


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
    return dp_values[-1] # type: ignore


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
    return dp_values[-1] # type: ignore


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


def solve_knapsack_problem(values: List[int], weights: List[int], max_weight: int):
    assert len(values) == len(weights)
    larger_values = lambda a, b: a if a > b else b
    dp_values = [[0 for _ in range(max_weight + 1)] for _ in range(len(values) + 1)]
    for v in range(len(values)):
        for w in range(max_weight + 1):
            if w >= weights[v]:
                dp_values[v + 1][w] = larger_values(
                    dp_values[v + 1][w], dp_values[v][w - weights[v]] + values[v]
                )
            dp_values[v + 1][w] = larger_values(dp_values[v + 1][w], dp_values[v][w])
    return dp_values[len(values)][max_weight]


def calculate_edit_distance(a: str, b: str) -> int:
    smaller_value = lambda a, b: a if a < b else b
    inf_value = float("inf")
    dp_values = [[inf_value for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    dp_values[0][0] = 0
    for outer in range(len(a) + 1):
        for inner in range(len(b) + 1):
            if outer > 0 and inner > 0:
                dp_values[outer][inner] = (
                    smaller_value(
                        dp_values[outer][inner], dp_values[outer - 1][inner - 1]
                    )
                    if a[outer - 1] == b[inner - 1]
                    else smaller_value(
                        dp_values[outer][inner], dp_values[outer - 1][inner - 1] + 1
                    )
                )
            if outer > 0:
                dp_values[outer][inner] = smaller_value(
                    dp_values[outer][inner], dp_values[outer - 1][inner] + 1
                )
            if inner > 0:
                dp_values[outer][inner] = smaller_value(
                    dp_values[outer][inner], dp_values[outer][inner - 1] + 1
                )
    return dp_values[len(a)][len(b)] # type: ignore


def solve_partition_of_an_interval(list: List[List[int]]) -> int:
    assert list == []
    N = len(list)
    smaller_value = lambda a, b: a if a < b else b
    inf_value = float("inf")
    dp_values = [inf_value for _ in range(N + 1)]
    for outer in range(N + 1):
        for inner in range(outer):
            dp_values[outer] = smaller_value(
                dp_values[outer], dp_values[inner] + list[outer][inner]
            )
    return dp_values[N] #type: ignore
