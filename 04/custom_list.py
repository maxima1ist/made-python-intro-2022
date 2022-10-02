"""
Package with custome list implementation.
"""


from itertools import zip_longest


class CustomList(list):
    """
    This is custome list implementation.
    Addition and subtraction operations are supported, \
    as well as comparisons by the sum of elements.
    """

    def __init__(self, values: list = None):
        self.__sum = 0
        if values:
            super().__init__(values)
            for value in values:
                self.__sum += value
        else:
            super().__init__()

    @staticmethod
    def __make_operator(lhs, rhs, operator):
        return [operator(value[0], value[1]) for value in zip_longest(lhs, rhs, fillvalue=0)]

    def __add__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: x + y)

    def __radd__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: y + x)

    def __sub__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: x - y)

    def __rsub__(self, other):
        return CustomList.__make_operator(self, other, lambda x, y: y - x)

    @property
    def sum(self):
        """
        It is the sum of CustomList elements.
        """
        return self.__sum

    def __lt__(self, other):
        return self.sum < other.sum

    def __le__(self, other):
        return self.sum <= other.sum

    def __eq__(self, other):
        return self.sum == other.sum

    def __ne__(self, other):
        return self.sum != other

    def __gt__(self, other):
        return self.sum > other.sum

    def __ge__(self, other):
        return self.sum >= other.sum

    def __str__(self):
        return f"{super().__str__()}, sum is {self.sum}"

    def append(self, value):
        self.__sum += value
        return super().append(value)
