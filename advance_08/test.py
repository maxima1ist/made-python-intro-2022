import time
from math import isclose

from stats import Stats


def test_time():
    cals_timer = Stats.timer("calc")
    assert cals_timer.get_name() == "calc.timer"
    assert cals_timer.get_value() is None
    cals_timer.add(1)
    assert isclose(cals_timer.get_value(), 1)
    cals_timer.add(2)
    Stats.timer("calc").add(5)
    assert isclose(cals_timer.get_value(), 8)
    assert isclose(Stats.timer("calc").get_value(), 8)
    with Stats.timer("calc"):
        time.sleep(3)
    assert isclose(round(cals_timer.get_value()), 11)
    cals_timer.clear()
    assert cals_timer.get_value() is None


def test_avg():
    cals_avg = Stats.avg("calc")
    assert cals_avg.get_name() == "calc.avg"
    assert cals_avg.get_value() is None
    cals_avg.add(1)
    assert isclose(cals_avg.get_value(), 1)
    cals_avg.add(2)
    Stats.avg("calc").add(5)
    assert isclose(cals_avg.get_value(), (1 + 2 + 5) / 3)
    assert isclose(Stats.avg("calc").get_value(), (1 + 2 + 5) / 3)
    cals_avg.clear()
    assert cals_avg.get_value() is None


def test_count():
    cals_count = Stats.count("calc")
    assert cals_count.get_name() == "calc.count"
    assert cals_count.get_value() is None
    cals_count.add()
    assert cals_count.get_value() == 1
    cals_count.add()
    Stats.count("calc").add()
    assert cals_count.get_value() == 3
    assert Stats.count("calc").get_value() == 3
    cals_count.clear()
    assert cals_count.get_value() is None


def test_collect():
    metrics = Stats.collect()
    assert metrics == {}

    Stats.count("no_used")
    metrics = Stats.collect()
    assert metrics == {}

    Stats.timer("calc").add(1)
    Stats.avg("calc").add(1)
    Stats.count("calc").add(1)
    metrics = Stats.collect()
    assert metrics == {
        "calc.timer": 1,
        "calc.avg": 1,
        "calc.count": 1
    }

    Stats.timer("calc").add(5)
    Stats.timer("calc").add(5)
    Stats.avg("calc").add(10)
    Stats.avg("calc").add(2)
    for _ in range(5):
        Stats.count("calc").add()
    Stats.count("anothe_no_used")
    metrics = Stats.collect()
    assert metrics == {
        "calc.timer": 10.,
        "calc.avg": 6.,
        "calc.count": 5
    }

    metrics = Stats.collect()
    assert metrics == {}
