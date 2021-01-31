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
