'''
Module with custome list implementation.
'''


from itertools import zip_longest


class CustomList(list):
    '''
    This is custome list implementation.
    Addition and subtraction operations are supported, \
    as well as comparisons by the sum of elements.
    '''

    @staticmethod
    def __make_operator(lhs, rhs, operator):
        return CustomList([operator(value[0], value[1]) for value in zip_longest(lhs, rhs, fillvalue=0)])

    def __add__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: x + y)

    def __radd__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: y + x)

    def __sub__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: x - y)

    def __rsub__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: y - x)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f'{super().__str__()}, sum is {sum(self)}'
