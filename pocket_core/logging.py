"""Logging configuration for Pocket Manager."""

import logging
from .config import Config


def setup_logging(log_level: str = None) -> None:
    """Configure logging.

    Args:
        log_level: Override default log level
    """
    config = Config()
    default_format = config.get("LOG_FORMAT")
    default_level = config.get("DEFAULT_LOG_LEVEL")
    date_format = config.get("LOG_DATE_FORMAT")

    logging.basicConfig(
        format=default_format,
        level=log_level or default_level,
        datefmt=date_format,
    )
