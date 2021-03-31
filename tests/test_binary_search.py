from algorithms_and_data_structures.binary_search import *


def test_binary_search():
    sorted_list = [0, 2, 4, 6]
    assert binary_search(sorted_list, 0) == 0
    assert binary_search(sorted_list, 2) == 1
    assert binary_search(sorted_list, 4) == 2
    assert binary_search(sorted_list, 6) == 3
    sorted_list = [0, 2, 4]
    assert binary_search(sorted_list, 0) == 0
    assert binary_search(sorted_list, 2) == 1
    assert binary_search(sorted_list, 4) == 2
    assert binary_search(sorted_list, 100) is None


def test_binary_search2():
    expected_twelve = binary_search_2([8, 5, 4], [4, 1, 9], 10)
    assert expected_twelve == 12


def test_solve_shooting_king():
    h = [10, 12]
    s = [2, 1]
    expected_twelve = solve_shooting_king(h, s)
    assert expected_twelve == 12
    h = [5, 12, 14, 21]
    s = [6, 4, 7, 2]
    expected_23 = solve_shooting_king(h, s)
    assert expected_23 == 23 