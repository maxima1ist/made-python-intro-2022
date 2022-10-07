import utils as my_math

# unit tests for 'solve_quadratic' function
try:
    my_math.solve_quadratic(0, 0, 0) == None
    assert False
except:
    pass

assert my_math.solve_quadratic(1, 2, 3) == None

answer = my_math.solve_quadratic(1, 1, 0.25)
assert len(answer) == 2
assert my_math.is_close(answer[0], -0.5)
assert my_math.is_close(answer[1], -0.5)

answer = my_math.solve_quadratic(3, 10, 5)
assert len(answer) == 2
assert my_math.is_close(answer[0], -2.72076, 1e-5)
assert my_math.is_close(answer[1], -0.61257, 1e-5)

# unit tests for 'split_by_even' function
assert my_math.split_by_even([]) == ([], [])
assert my_math.split_by_even([1]) == ([], [1])
assert my_math.split_by_even([2]) == ([2], [])
assert my_math.split_by_even([1, 2, 3, 4, 5, 6]) == ([2, 4, 6], [1, 3, 5])

arr = [value for value in range(-10000, 10000)]
assert my_math.split_by_even(arr) == ([value for value in arr if value % 2 == 0],
                                      [value for value in arr if value % 2 == 1])

print('All tests passed!')
