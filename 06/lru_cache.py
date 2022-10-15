class LRUCache:

    def __init__(self, limit=42):
        self.__limit = limit
        self.__keys = []
        self.__keys_to_values = {}

    def get(self, key):
        if key not in self.__keys_to_values:
            return None

        self.__keys.pop(self.__keys.index(key))
        self.__keys.append(key)

        return self.__keys_to_values[key]

    def set(self, key, value):
        if key in self.__keys_to_values:
            self.__keys.pop(self.__keys.index(key))

        self.__keys.append(key)
        if len(self.__keys) > self.__limit:
            key_to_remove = self.__keys.pop(0)
            self.__keys_to_values.pop(key_to_remove)
        self.__keys_to_values[key] = value
