from typing import Dict


def calculate_total_sum(n: int) -> int:
    if n == 0:
        return 0
    return n + calculate_total_sum(n - 1)


def GCD(m: int, n: int) -> int:
    if n == 0:
        return m
    return GCD(n, m % n)


def calculate_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


def calculate_fibonacci_memorized(n: int) -> int:
    table = {}

    def calculate_fibonacci_memorized_impl(n: int, table: Dict[int, int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in table:
            return table[n]
        result = calculate_fibonacci_memorized_impl(
            n - 1, table
        ) + calculate_fibonacci_memorized_impl(n - 2, table)
        table[n] = result
        return result

    return calculate_fibonacci_memorized_impl(n, table)
