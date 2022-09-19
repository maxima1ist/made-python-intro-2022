def get_min_abs(arr: list) -> list:
    if not arr:
        return []

    curr_res = []
    min_abs = abs(arr[0])
    for el in arr:
        curr_abs = abs(el)

        if curr_abs > min_abs:
            continue

        if curr_abs < min_abs:
            curr_res.clear()
            min_abs = curr_abs

        curr_res.append(el)

    return curr_res


def merge_with_set(lhs, rhs) -> list:
    return sorted(set(lhs).intersection(set(rhs)))


def merge(lhs, rhs) -> list:
    if not lhs or not rhs:
        return []

    res = []
    liter = iter(lhs)
    riter = iter(rhs)
    lvalue = next(liter)
    rvalue = next(riter)
    while True:
        try:
            if lvalue == rvalue:
                if not res or res[-1] != lvalue:
                    res.append(lvalue)
                rvalue = next(riter)
                lvalue = next(liter)
            elif lvalue > rvalue:
                rvalue = next(riter)
            else:  # lvalue < rvalue
                lvalue = next(liter)
        except StopIteration:
            break
    return res
