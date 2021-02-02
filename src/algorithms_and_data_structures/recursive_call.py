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
