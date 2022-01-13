from __future__ import absolute_import, unicode_literals

import sys
import socket

from anti_useragent.utils import misc


try:
    from loguru import logger
except:
    misc.install("loguru")
    from loguru import logger


def set_log_config(formatter, logfile=None):
    return {
        "default": {
            "handlers": [
                {
                    "sink": sys.stdout,
                    "format": formatter,
                    "level": "TRACE"
                },
                {
                    "sink": "info.log" if not logfile else logfile,
                    "format": formatter,
                    "level": "INFO",
                    "rotation": '1 week',
                    "retention": '30 days',
                    'encoding': 'utf-8'
                },
            ],
            "extra": {
                "host": socket.gethostbyname(socket.gethostname()),
                'log_name': 'default',
                'type': 'None'
            },
            "levels": [
                dict(name="TRACE", icon="✏️", color="<cyan><bold>"),
                dict(name="DEBUG", icon="❄️", color="<blue><bold>"),
                dict(name="INFO", icon="♻️", color="<bold>"),
                dict(name="SUCCESS", icon="✔️", color="<green><bold>"),
                dict(name="WARNING", icon="⚠️", color="<yellow><bold>"),
                dict(name="ERROR", icon="❌️", color="<red><bold>"),
                dict(name="CRITICAL", icon="☠️", color="<RED><bold>"),
            ]
        },
        'kafka': True
    }


class LogFormatter(object):
    default_formatter = '<green>{time:YYYY-MM-DD HH:mm:ss,SSS}</green> | ' \
                        '[<cyan>{extra[log_name]}</cyan>] <cyan>{module}</cyan>:<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | ' \
                        '<red>{extra[host]}</red> | ' \
                        '<level>{level.icon}{level: <5}</level> | ' \
                        '<level>{level.no}</level> | ' \
                        '<level>{extra[type]}</level> | ' \
                        '<level>{message}</level> '

    kafka_formatter = '{time:YYYY-MM-DD HH:mm:ss,SSS}| ' \
                      '[{extra[log_name]}] {module}:{name}:{function}:{line} | ' \
                      '{extra[host]} | ' \
                      '{process} | ' \
                      '{thread} | ' \
                      '{level: <5} | ' \
                      '{level.no} | ' \
                      '{extra[type]}| ' \
                      '{message} '

    def __init__(self):
        self.logger = logger

    def setter_log_handler(self, callback=None):
        assert callable(callback), 'callback must be a callable object'
        self.logger.add(callback, format=self.kafka_formatter)

    def get_logger(self, name=None):
        log_config = set_log_config(self.default_formatter)
        config = log_config.pop('default', {})
        if name:
            config['extra']['log_name'] = name
        self.logger.configure(**config)
        return self.logger

    @staticmethod
    def format(spider, meta):
        if hasattr(spider, 'logging_keys'):
            logging_txt = []
            for key in spider.logging_keys:
                if meta.get(key, None) is not None:
                    logging_txt.append(u'{0}:{1} '.format(key, meta[key]))
            logging_txt.append('successfully')
            return ' '.join(logging_txt)

