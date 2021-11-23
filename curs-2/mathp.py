def sum_n(n):
    if n == 0:
        return n
    return n + sum_n(n - 1);

def sum_n_even(n):
    if n % 2 != 0:
        n -= 1

    if n == 0:
        return n

    return n + sum_n(n - 2);

def sum_n_odd(n):
    if n % 2 == 0:
        n -= 1

    if n == 0:
        return n

    return n + sum_n(n - 2);