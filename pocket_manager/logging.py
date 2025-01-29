"""Logging configuration for Pocket Manager."""

import logging
import argparse
import os
from .config import DEFAULT_LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT

def setup_logging(args: argparse.Namespace = None) -> None:
    """Set up logging with priority: args > env > config default."""
    
    # Priority: CLI args > env var > config default
    log_level = (
        args.log_level if args and hasattr(args, "log_level")
        else os.getenv("POCKET_LOG_LEVEL")
        or DEFAULT_LOG_LEVEL
    )

    logging.basicConfig(
        level=log_level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    ) 