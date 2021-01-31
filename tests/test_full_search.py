from algorithms_and_data_structures.full_search import *


def test_full_search_1():
    expected_twelve = full_search_1([8, 5, 4], [4, 1, 9], 10)
    assert expected_twelve == 12
    expected_none = full_search_1([1, 2, 3], [1, 2, 3], 7)
    assert expected_none is None
