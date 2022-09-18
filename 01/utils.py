ROUNDING_ACCURACY = 1e-10


def is_close(lhs: float, rhs: float, accuracy: float = ROUNDING_ACCURACY) -> bool:
    return abs(lhs - rhs) < accuracy


def solve_quadratic(a: float, b: float, c: float) -> tuple:
    if is_close(a, 0):
        raise ValueError("Incorrect quadratic equation")

    d = b ** 2 - 4 * a * c
    if d < 0:
        return None

    d = d ** (1 / 2)
    return ((-b - d) / (2 * a), (-b + d) / (2 * a))


def split_by_even(arr: list) -> tuple:
    even = []
    not_even = []
    for value in arr:
        if value % 2 == 0:
            even.append(value)
        else:
            not_even.append(value)

    return (even, not_even)
