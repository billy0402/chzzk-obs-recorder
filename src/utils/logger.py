import logging
import logging.config
import sys

from .file import file_name

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y/%m/%d %H:%M',
        },
        'colored_console': {
            '()': 'utils.logger.ColoredConsole',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y/%m/%d %H:%M',
        },
    },
    'filters': {
        'info_filter': {
            '()': 'utils.logger.LevelFilter',
            'level': 'INFO',
        },
        'error_filter': {
            '()': 'utils.logger.LevelFilter',
            'level': 'ERROR',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'colored_console',
        },
        'file_info': {
            'class': 'logging.FileHandler',
            'filename': 'logs/info.log',
            'level': 'INFO',
            'formatter': 'simple',
            'filters': ['info_filter'],
        },
        'file_error': {
            'class': 'logging.FileHandler',
            'filename': 'logs/error.log',
            'level': 'ERROR',
            'formatter': 'simple',
            'filters': ['error_filter'],
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file_info', 'file_error'],
    },
}


class ColoredConsole(logging.Formatter):
    grey = '\x1b[38;20m'
    yellow = '\x1b[33;20m'
    red = '\x1b[31;20m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    fmt = '[%(levelname)s] %(name)s - %(asctime)s : %(message)s'

    FORMATS = {
        logging.DEBUG: grey + fmt + reset,
        logging.INFO: grey + fmt + reset,
        logging.WARNING: yellow + fmt + reset,
        logging.ERROR: red + fmt + reset,
        logging.CRITICAL: bold_red + fmt + reset,
    }

    def format(self, record) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, self.datefmt)
        return formatter.format(record)


class LevelFilter(logging.Filter):
    level: int

    def __init__(self, level):
        if type(level) is int:
            self.level = level
        else:
            self.level = logging._nameToLevel[level]

    def filter(self, logRecord) -> bool:
        return logRecord.levelno == self.level


def get_main_file_name() -> str:
    main_full_path = sys.modules['__main__'].__file__
    return file_name(main_full_path)


def get_logger(name: str = get_main_file_name()) -> logging.Logger:
    logging.config.dictConfig(LOGGING)
    return logging.getLogger(name)
