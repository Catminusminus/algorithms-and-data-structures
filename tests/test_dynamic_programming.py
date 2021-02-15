from algorithms_and_data_structures.dynamic_programming import *


def test_solve_frog():
    expected_one = solve_frog([7, 5, 6])
    assert expected_one == 1
    expected_two = solve_frog([7, 5, 6, 5])
    assert expected_two == 2


def test_solve_frog_relaxation_1():
    expected_one = solve_frog_relaxation_1([7, 5, 6])
    assert expected_one == 1
    expected_two = solve_frog_relaxation_1([7, 5, 6, 5])
    assert expected_two == 2


def test_solve_frog_relaxation_2():
    expected_one = solve_frog_relaxation_2([7, 5, 6])
    assert expected_one == 1
    expected_two = solve_frog_relaxation_2([7, 5, 6, 5])
    assert expected_two == 2


def test_solve_frog_memorized():
    dp_values = [float("inf") for _ in range(3)]
    expected_one = solve_frog_memorized([7, 5, 6], dp_values)
    assert expected_one == 1
    dp_values = [float("inf") for _ in range(4)]
    expected_two = solve_frog_memorized([7, 5, 6, 5], dp_values)
    assert expected_two == 2


def test_solve_knapsack_problem():
    expected_94 = solve_knapsack_problem([3, 2, 6, 1, 3, 85], [2, 1, 3, 2, 1, 5], 9)
    assert expected_94 == 94


def test_calculate_edit_distance():
    expected_one = calculate_edit_distance("ab", "a")
    assert expected_one == 1
    expected_zero = calculate_edit_distance("ab", "ab")
    assert expected_zero == 0
    expected_two = calculate_edit_distance("ab", "ba")
    assert expected_two == 2


def test_solve_partition_of_an_interval():
    pass
