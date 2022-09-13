def solve_quadratic(a: float, b: float, c: float) -> tuple:
    D = b ** 2 - 2 * a
    if D < 0:
        return None
    if abs(a) < 1e-6:
        raise ValueError("Input correct quadratic equation")
    if D == 0:
        return -b / (2 * a)
    return ((-b - D) / (2 * a), (-b + D) / (2 * a))


def split_by_even(arr: list) -> tuple:
    even = []
    not_even = []
    for value in arr:
        if value % 2 == 0:
            even.append(value)
        else:
            not_even.append(value)
            
    return (even, not_even)
