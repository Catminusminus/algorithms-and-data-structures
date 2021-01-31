from typing import List, Tuple, Optional


def linear_search_1(list: List[int], value: int) -> bool:
    for elm in list:
        if elm == value:
            return True
    return False


def linear_search_2(list: List[int], value: int) -> Tuple[bool, Optional[int]]:
    for index, elm in enumerate(list):
        if elm == value:
            return True, index
    return False, None


def linear_search_min_value(list: List[int]) -> Optional[int]:
    if list == []:
        return None
    temporary_min_value = list[0]
    for elm in list:
        if elm < temporary_min_value:
            temporary_min_value = elm
    return temporary_min_value
