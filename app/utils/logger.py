import os
import logging
from logging.handlers import RotatingFileHandler
from app.config import config


class Logger:
    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_logger()
        return cls._instance

    def _init_logger(self):
        log_level = getattr(logging, config.LOG_LEVEL.upper(), logging.INFO)
        
        os.makedirs(config.LOG_PATH, exist_ok=True)
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)

        file_handler = RotatingFileHandler(
            os.path.join(config.LOG_PATH, 'app.log'),
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        error_file_handler = RotatingFileHandler(
            os.path.join(config.LOG_PATH, 'error.log'),
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.setLevel(log_level)
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
        root_logger.addHandler(error_file_handler)

    @staticmethod
    def get(name=None):
        return logging.getLogger(name)


logger = Logger().get('app')


def get_logger(name='app'):
    return logging.getLogger(name)
