import re
import pytest


def test_int_operation():
    assert int(1) + int(2) == int(3)
    assert int(1) - int(2) == int(-1)
    assert int(1) * int(2) == int(2)
    assert int(1) / int(2) == float(1 / 2)
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        assert int(1) / int(0)


def test_int_from_str():
    assert int(1) == int("1")
    assert int(-1) == int("-1")
    assert int(100) == int("100")
    with pytest.raises(ValueError,
                       match=re.escape(r"invalid literal for int() with base 10: 'some'")):
        int("some")


def test_int_from_float():
    assert int(0.) == int(0)
    assert int(1.1) == int(1)
    assert int(1.5) == int(1)
    assert int(1.7) == int(1)


def test_int_to_two():
    assert int("0", 2) == int(0)
    assert int("1", 2) == int(1)
    assert int("-1", 2) == int(-1)
    assert int("1010", 2) == int(10)


def test_int_to_sixteen():
    assert int("0", 16) == int(0)
    assert int("1", 16) == int(1)
    assert int("-1", 16) == int(-1)
    assert int("1c", 16) == int(28)
