import logging

from pythonjsonlogger import json

json_formatter = json.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(name)s %(message)s %(filename)s"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(json_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler],
)


def get_logger(name):
    return logging.getLogger(name)

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": json.JsonFormatter,
            "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s %(filename)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}