import time

from memory_profiler import profile

from users import ID, Name
from users import UsualUser, SlotsUser, WeakrefUser

from profile_deco import profile_deco


BIG_COUNT = 100_000
INITIALIZER_VALUES = [(ID(i), Name(f"name_{i}")) for i in range(BIG_COUNT)]


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Time for {func.__name__} is {(end - start) * 1000} msec")
        return res
    return wrapper


@profile
@stopwatch
def create_usual_users() -> list[UsualUser]:
    return [UsualUser(user_id, user_name) for user_id, user_name in INITIALIZER_VALUES]


@profile
@stopwatch
def create_slots_users() -> list[SlotsUser]:
    return [SlotsUser(user_id, user_name) for user_id, user_name in INITIALIZER_VALUES]


@profile
@stopwatch
def create_weakref_users() -> list[WeakrefUser]:
    return [WeakrefUser(user_id, user_name) for user_id, user_name in INITIALIZER_VALUES]


@profile
@stopwatch
def delete_usual_users(users: list[UsualUser]) -> None:
    del users


@profile
@stopwatch
def delete_slots_users(users: list[SlotsUser]) -> None:
    del users


@profile
@stopwatch
def delete_weakref_users(users: list[WeakrefUser]) -> None:
    del users


@profile_deco
def add(a, b):
    time.sleep(1)
    return a + b


@profile_deco
def sub(a, b):
    time.sleep(2)
    return a - b


if __name__ == "__main__":
    usual_users = create_usual_users()
    slots_users = create_slots_users()
    weakref_users = create_weakref_users()

    delete_usual_users(usual_users)
    delete_slots_users(slots_users)
    delete_weakref_users(weakref_users)

    add(1, 2)
    add(4, 5)
    add.print_stat()

    sub(1, 2)
    sub(4, 5)
    sub.print_stat()
