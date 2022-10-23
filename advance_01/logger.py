import logging
import logging.config


logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "file_formatter": {
                "format": "%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s"
            },
            "stdout_formatter": {
                "format": "%(asctime)s\t%(levelname)s\t%(message)s"
            }
        },
        "handlers": {
            "file_handler": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "filename": "cache.log",
                "formatter": "file_formatter"
            },
            "stdout_handler": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "stdout_formatter"
            }
        },
        "loggers": {
            "logger": {
                "level":  "DEBUG",
                "handlers": ["file_handler"]
            },
            "logger_s": {
                "level":  "DEBUG",
                "handlers": ["file_handler", "stdout_handler"]
            }
        }
    }
)

logger = logging.getLogger("logger")
logger_s = logging.getLogger("logger_s")
