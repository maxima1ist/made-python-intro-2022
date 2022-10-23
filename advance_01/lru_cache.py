from logger import logger, logger_s


class LRUCache:

    def __init__(self, limit=10, is_log_stdout=False):
        self.__logger = logger if is_log_stdout else logger_s
        self.__logger.info("LRUCache '__init__' called, "
                           "logger initialized %s stdout",
                           "without" if is_log_stdout else "with")

        self.__limit = limit
        self.__logger.debug(
            "Variable __limit set with '%s' value in LRUCache.__init__", limit)

        self.__keys = []
        self.__logger.debug(
            "Variable __keys set with empty value in LRUCache.__init__")

        self.__keys_to_values = {}
        self.__logger.debug(
            "Variable __keys set with empty value in LRUCache.__init__")

    def get(self, key):
        if key not in self.__keys_to_values:
            self.__logger.warning(
                "LRUCache.get: there is no such key as %s", key)
            return None

        self.__keys.pop(self.__keys.index(key))
        self.__keys.append(key)

        return self.__keys_to_values[key]

    def set(self, key, value):
        if key in self.__keys_to_values:
            self.__logger.warning(
                "LRUCache.set: key %s already exist, it will be overrided", key)
            self.__keys.pop(self.__keys.index(key))

        self.__keys.append(key)
        if len(self.__keys) > self.__limit:
            key_to_remove = self.__keys.pop(0)
            self.__keys_to_values.pop(key_to_remove)
        self.__keys_to_values[key] = value
