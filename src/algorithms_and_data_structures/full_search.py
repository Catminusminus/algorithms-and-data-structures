from typing import List, Optional


def full_search_1(
    list_a: List[int], list_b: List[int], lower_bound: int
) -> Optional[int]:
    assert list_a != []
    assert list_b != []

    sum_value = None

    for elm_a in list_a:
        for elm_b in list_b:
            temporary_sum_value = elm_a + elm_b
            if temporary_sum_value < lower_bound:
                continue
            if sum_value is None or temporary_sum_value < sum_value:
                sum_value = temporary_sum_value

    return sum_value


def full_search_2(list: List[int], sub_sum: int) -> bool:
    n = len(list)
    for i in range(2 ** n):
        temporary_sum_value = 0
        for j in range(n):
            if (i >> j) & 1:
                temporary_sum_value += list[j]
        if temporary_sum_value == sub_sum:
            return True
    return False


def full_search_3(list: List[int], sub_sum: int) -> bool:
    if sub_sum < 0:
        return False
    if sub_sum == 0:
        return True
    if list == []:
        return False
    return full_search_3(list[1:], sub_sum - list[0]) or full_search_3(
        list[1:], sub_sum
    )
