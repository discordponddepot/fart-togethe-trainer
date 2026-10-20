from __future__ import annotations

import sys

from loguru import logger


def setup(verbose: bool = False) -> None:
    logger.remove()
    level = "DEBUG" if verbose else "INFO"
    logger.add(sys.stderr, level=level, format="<green>{time:HH:mm:ss}</green> | {level: <7} | {message}")
    logger.add("logs/trainer_{time}.log", rotation="5 MB", retention=3, level="DEBUG")