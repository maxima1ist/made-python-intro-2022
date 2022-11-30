import weakref


class ID:
    def __init__(self, identificator):
        self.__identificator = identificator


class Name:
    def __init__(self, name):
        self.__name = name


class UsualUser:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name


class SlotsUser:
    __slots__ = ("__user_id", "__name")

    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name


class WeakrefUser:
    def __init__(self, user_id, name):
        self.__user_id = weakref.ref(user_id)
        self.__name = weakref.ref(name)
