from typing import List, Optional, Union
from bisect import bisect_left


def binary_search(sorted_list: List[int], key: int) -> Optional[int]:
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        print(f"{left}:{right}")
        mid = int((left + right) / 2)
        mid_value = sorted_list[mid]
        if mid_value == key:
            return mid
        if mid_value < key:
            left = mid + 1
            continue
        right = mid - 1
    return None


def binary_search_2(
    list_a: List[int], list_b: List[int], lower_bound: int
) -> Optional[int]:
    assert list_a != []
    assert list_b != []

    min_value = float("inf")
    list_b.sort()
    for a in list_a:
        index = bisect_left(list_b, lower_bound - a)
        if a + list_b[index] < min_value:
            min_value = a + list_b[index]

    return min_value  # type: ignore


def solve_shooting_king(h: List[int], s: List[int]) -> int:
    assert len(h) == len(s)
    left = 0
    right = int(1e8)
    while left + 1 < right:
        mid = (left + right) // 2
        time_limit = [0 for _ in range(len(h))]
        ok = True
        for i in range(len(h)):
            if mid < h[i]:
                ok = False
            else:
                time_limit[i] = (mid - h[i]) / s[i]
        time_limit.sort()
        for i in range(len(h)):
            if time_limit[i] < i:
                ok = False
        if ok:
            right = mid
        else:
            left = mid
    return right
