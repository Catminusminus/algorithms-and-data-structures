from algorithms_and_data_structures.linear_search import *


def test_linear_search_1():
    assert linear_search_1([1, 2, 3], 1)
    assert not linear_search_1([1, 2, 3], 4)
    assert not linear_search_1([], 1)


def test_linear_search_2():
    expected_true, expected_two = linear_search_2([1, 2, 3], 3)
    assert expected_true
    assert expected_two == 2
    expected_false, expected_none = linear_search_2([1, 2, 3], 4)
    assert not expected_false
    assert expected_none is None
    expected_false, expected_none = linear_search_2([], 1)
    assert not expected_false
    assert expected_none is None


def test_linear_search_min_value():
    expected_none = linear_search_min_value([])
    assert expected_none is None
    expected_one = linear_search_min_value([1, 2, 3, 4])
    assert expected_one == 1
