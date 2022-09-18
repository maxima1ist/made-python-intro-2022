import utils


# unit tests for 'merge_with_set' function
assert utils.get_min_abs([]) == []
assert utils.get_min_abs([-1, 0, 1]) == [0]
assert utils.get_min_abs([-5, 9, 6, -8]) == [-5]
assert utils.get_min_abs([-1, 2, -5, 1, -1]) == [-1, 1, -1]

# unit tests for 'merge_with_set' function
assert utils.merge_with_set([], []) == []
assert utils.merge_with_set((1, 2), []) == []
assert utils.merge_with_set((), [3, 4]) == []
assert utils.merge_with_set((1,), {1}) == [1]
assert utils.merge_with_set({1, 3, 5}, [2, 4, 6]) == []
assert utils.merge_with_set([1, 2, 3], {1, 2, 3}) == [1, 2, 3]
assert utils.merge_with_set([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]

# unit tests for 'merge' function
assert utils.merge([], []) == []
assert utils.merge((1, 2), []) == []
assert utils.merge((), [3, 4]) == []
assert utils.merge((1,), {1}) == [1]
assert utils.merge({1, 3, 5}, [2, 4, 6]) == []
assert utils.merge([1, 2, 3], {1, 2, 3}) == [1, 2, 3]
assert utils.merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]

print("All tests passed!")
