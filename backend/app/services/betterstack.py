import sys

from logtail import LogtailHandler
import logging

from settings import settings


def get_betterstack_logging():
    logger = logging.getLogger("fastapi app")
    logger.handlers = []
    logger.setLevel(logging.INFO)

    handler = LogtailHandler(
        source_token=settings.SOURCE_TOKEN,
        host=settings.BETTERSTACK_HOST,
    )
    logger.addHandler(handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


betterstack_log = get_betterstack_logging()
