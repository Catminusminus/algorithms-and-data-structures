from typing import List, Optional


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
