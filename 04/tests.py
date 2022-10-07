from custom_list import CustomList


def compare_element_by_element(lhs: CustomList, rhs: CustomList) -> bool:
    if len(lhs) != len(rhs):
        return False

    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            return False

    return True


if __name__ == '__main__':
    # operator +
    assert compare_element_by_element(CustomList() + CustomList(),
                                      CustomList())
    assert compare_element_by_element([] + CustomList(),
                                      CustomList())
    assert compare_element_by_element(CustomList([1, 2]) + CustomList(),
                                      CustomList([1, 2]))
    assert compare_element_by_element([1, 2] + CustomList(),
                                      CustomList([1, 2]))
    assert compare_element_by_element(CustomList([5, 1, 3, 7]) + [1, 2, 7],
                                      CustomList([6, 3, 10, 7]))
    assert compare_element_by_element(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]),
                                      CustomList([6, 3, 10, 7]))

    # operator -
    assert compare_element_by_element(CustomList() - CustomList(),
                                      CustomList())
    assert compare_element_by_element(CustomList() - [], CustomList())
    assert compare_element_by_element(CustomList() - [1, 2],
                                      CustomList([-1, -2]))
    assert compare_element_by_element([1, 2] - CustomList(),
                                      CustomList([1, 2]))
    assert compare_element_by_element(CustomList([5, 1, 3, 7]) - [1, 2, 7],
                                      CustomList([4, -1, -4, 7]))
    assert compare_element_by_element(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]),
                                      CustomList([4, -1, -4, 7]))

    # operator <
    assert CustomList() < CustomList([1, 2, 3])
    assert CustomList([-1, -2]) < CustomList()

    # operator <=
    assert CustomList() <= CustomList([1, 2, 3])
    assert CustomList([1, 2]) <= CustomList([1, 2])

    # operator ==
    assert CustomList() == CustomList([1, -1])
    assert CustomList([1, 2, 3]) == CustomList([6])

    # operator !=
    assert CustomList([1, 2]) != CustomList()
    assert CustomList([1, 2]) != CustomList([1, 2, 3])

    # operator >
    assert CustomList([1, 2, 3]) > CustomList()
    assert CustomList([1, -2]) > CustomList([-5])

    # operator >=
    assert CustomList([1]) >= CustomList()
    assert CustomList([-2, 2]) >= CustomList([-5, 5])

    # to string
    ltest = []
    assert str(CustomList(ltest)) == f'{ltest}, sum is {sum(ltest)}'
    ltest = [1, -1]
    assert str(CustomList(ltest)) == f'{ltest}, sum is {sum(ltest)}'
    ltest = [1, 2, 3]
    assert str(CustomList(ltest)) == f'{ltest}, sum is {sum(ltest)}'

    print('All tests passed!')
