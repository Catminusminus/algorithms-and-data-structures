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
