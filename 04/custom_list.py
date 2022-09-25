"""
This is module description.
"""


class CustomList(list):
    """
    This is class description.
    """

    def __init__(self, values: list = None):
        self.__sum = 0
        if values:
            super().__init__(values)
            for value in values:
                self.__sum += value
        else:
            super().__init__()

    def __add__(self, other):
        result = CustomList()

        self_len = len(self)
        other_len = len(other)
        for i in range(min(self_len, other_len)):
            result.append(self[i] + other[i])

        if self_len < other_len:
            for i in range(self_len, other_len):
                result.append(other[i])
        elif self_len > other_len:
            for i in range(other_len, self_len):
                result.append(self[i])

        return result

    def __sub__(self, other):
        result = CustomList()

        self_len = len(self)
        other_len = len(other)
        for i in range(min(self_len, other_len)):
            result.append(self[i] - other[i])

        if self_len < other_len:
            for i in range(self_len, other_len):
                result.append(-other[i])
        elif self_len > other_len:
            for i in range(other_len, self_len):
                result.append(self[i])

        return result

    @property
    def sum(self):
        """
        This is function description.
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
