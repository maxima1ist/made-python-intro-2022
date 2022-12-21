from datetime import datetime, timedelta
from typing import Dict, Optional


class BaseMetric:
    def __init__(self, name: str):
        NotImplemented

    def get_name(self):
        NotImplemented

    def get_value(self):
        NotImplemented

    def add(self, value):
        NotImplemented

    def clear(self):
        NotImplemented


class MetricTimer(BaseMetric):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__time: Optional[float] = None

    def __enter__(self):
        self.__start = datetime.now()
        return self

    def __exit__(self, cls, error, tb):
        self.__end = datetime.now()
        self.add(self.__end - self.__start)

    def get_name(self) -> str:
        return f"{self.__name}.timer"

    def get_value(self) -> Optional[float]:
        return self.__time

    def add(self, value: int | float) -> None:
        if self.__time is None:
            self.__time = 0
        if isinstance(value, timedelta):
            value = value.total_seconds()
        self.__time += float(value)

    def clear(self) -> None:
        self.__time = None


class MetricAvg(BaseMetric):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__sum: Optional[float] = None
        self.__count: Optional[int] = None

    def get_name(self) -> str:
        return f"{self.__name}.avg"

    def get_value(self) -> Optional[float]:
        if self.__sum is None or not self.__count:
            return None
        return self.__sum / self.__count

    def add(self, value: float) -> None:
        if self.__sum is None:
            self.__sum = 0.
        if self.__count is None:
            self.__count = 0
        self.__sum += value
        self.__count += 1

    def clear(self) -> None:
        self.__sum = None
        self.__count = None


class MetricCount(BaseMetric):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__count: Optional[int] = None

    def get_name(self) -> str:
        return f"{self.__name}.count"

    def get_value(self) -> Optional[int]:
        return self.__count

    def add(self, value: int = 1) -> None:
        if self.__count is None:
            self.__count = 0
        self.__count += value

    def clear(self) -> None:
        self.__count = None


class Stats:
    metrics_timer: Dict[str, BaseMetric] = {}
    metrics_avg: Dict[str, BaseMetric] = {}
    metrics_count: Dict[str, BaseMetric] = {}

    @staticmethod
    def timer(name: str) -> BaseMetric:
        if name not in Stats.metrics_timer:
            Stats.metrics_timer[name] = MetricTimer(name)
        return Stats.metrics_timer[name]

    @staticmethod
    def avg(name: str) -> BaseMetric:
        if name not in Stats.metrics_avg:
            Stats.metrics_avg[name] = MetricAvg(name)
        return Stats.metrics_avg[name]

    @staticmethod
    def count(name: str) -> BaseMetric:
        if name not in Stats.metrics_count:
            Stats.metrics_count[name] = MetricCount(name)
        return Stats.metrics_count[name]

    @staticmethod
    def collect() -> Dict[str, BaseMetric]:
        res = {}
        for metrics in [Stats.metrics_timer.items(),
                        Stats.metrics_avg.items(),
                        Stats.metrics_count.items()]:
            for _, metric in metrics:
                if metric.get_value() is not None:
                    res[metric.get_name()] = metric.get_value()
                    metric.clear()
        return res
