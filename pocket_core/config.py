"""Configuration management."""

import json
import os
from typing import Dict, Any


class Config:
    """Configuration manager for pocket-core."""

    REQUIRED_FIELDS = {
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

    _instance = None
    _config: Dict[str, Any] = None

    def __new__(cls):
        """Singleton pattern to ensure one config instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize config if not already loaded."""
        if self._config is None:
            self.load_config()

    def load_config(self) -> None:
        """Load and validate configuration from JSON file.

        Raises:
            KeyError: If required configuration values are missing
            TypeError: If configuration values are of wrong type
        """
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            self._config = json.load(f)

        # Validate required fields and types
        for field, expected_type in self.REQUIRED_FIELDS.items():
            if field not in self._config:
                raise KeyError(f"Missing required config field: {field}")
            if not isinstance(self._config[field], expected_type):
                raise TypeError(
                    f"Config field {field} must be {expected_type.__name__}, "
                    f"got {type(self._config[field]).__name__}"
                )

    def get(self, key: str) -> Any:
        """Get configuration value.

        Args:
            key: Configuration key to retrieve

        Returns:
            Configuration value

        Raises:
            KeyError: If key doesn't exist
        """
        return self._config[key]

    def update(self, key: str, value: Any) -> None:
        """Update configuration value and save to file.

        Args:
            key: Configuration key to update
            value: New value
        """
        self._config[key] = value
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "w") as f:
            json.dump(self._config, f, indent=4)
