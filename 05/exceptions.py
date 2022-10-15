class InvalidInputError(Exception):
    pass


class NotNumberError(InvalidInputError):
    pass


class OutOfRangeError(InvalidInputError):
    pass


class TakenCellError(InvalidInputError):
    pass
