"""Configuration management."""

import json
import os
from typing import Any

# Required fields and their types
REQUIRED_FIELDS: dict[str, type] = {
    "CONSUMER_KEY": str,
    "REDIRECT_URI": str,
    "ACCESS_TOKEN": str,
    "LOG_FORMAT": str,
    "DEFAULT_LOG_LEVEL": str,
    "LOG_DATE_FORMAT": str,
    "DATA_DIR": str,
    "UNREAD_FILE": str,
    "ARCHIVED_FILE": str,
    "LAST_SYNC_FILE": str,
}

_config: dict[str, str] = {}


def _validate_config(config: dict[str, Any]) -> None:
    """Validate configuration fields and types."""
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in config:
            raise KeyError(f"Missing required config field: {field}")
        if not isinstance(config[field], expected_type):
            raise TypeError(
                f"Config field {field} must be {expected_type.__name__}, "
                f"got {type(config[field]).__name__}"
            )


def _ensure_loaded() -> None:
    """Ensure configuration is loaded."""
    if not _config:
        path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(path) as f:
            _config.update(json.load(f))
        _validate_config(_config)


def get(key: str) -> str:
    """Read configuration value, loading from file if needed."""
    _ensure_loaded()
    return _config[key]


def set(key: str, value: str) -> None:
    """Write configuration value to both memory and file."""
    _ensure_loaded()
    _config[key] = value

    path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(path, "w") as f:
        json.dump(_config, f, indent=4)
