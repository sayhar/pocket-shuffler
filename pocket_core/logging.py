"""Logging configuration for Pocket Manager."""

import logging
from . import config


def setup_logging(log_level: str) -> None:
    """Configure logging.

    Args:
        log_level: Override default log level
    """
    default_format = config.get("LOG_FORMAT")
    default_level = config.get("DEFAULT_LOG_LEVEL")
    date_format = config.get("LOG_DATE_FORMAT")

    logging.basicConfig(
        format=default_format,
        level=log_level or default_level,
        datefmt=date_format,
    )
