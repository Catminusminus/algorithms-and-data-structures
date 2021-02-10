from algorithms_and_data_structures.recursive_call import *


def test_calculate_total_sum():
    expected_six = calculate_total_sum(3)
    assert expected_six == 6
    expected_not_six = calculate_total_sum(4)
    assert not expected_not_six == 6


def test_gcd():
    expected_five = GCD(40, 15)
    assert expected_five == 5


def test_calculate_fibonacci():
    expected_one = calculate_fibonacci(2)
    assert expected_one == 1
    expected_three = calculate_fibonacci(4)
    assert expected_three == 3


def test_calculate_fibonacci_memorized():
    expected_three = calculate_fibonacci_memorized(4)
    assert expected_three == 3
