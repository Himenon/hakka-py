from logging import StreamHandler, getLogger as _getLogger
from logging import DEBUG, INFO, WARN, CRITICAL, WARNING, ERROR
from os import environ

_LOG_LEVELS = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARN": WARN,
    "CRITICAL": CRITICAL,
    "WARNING": WARNING,
    "ERROR": ERROR
}

LOG_LEVEL = _LOG_LEVELS.get(environ.get('LOG_LEVEL'), INFO)

logger = _getLogger(__name__)
handler = StreamHandler()

handler.setLevel(LOG_LEVEL)
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)
