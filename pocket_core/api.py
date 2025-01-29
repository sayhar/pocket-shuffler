"""Pocket API interactions."""

# Specifically, this is the API that talks to the Pocket server.
# A future api file will be the API that others can use to talk to this program.
# We will resolve those naming issues later.

import time
from typing import Any, Dict, List, Tuple
from pocket import Pocket
from .config import Config


def get_articles(state: str = "all") -> List[Dict[str, Any]]:
    """Get all articles of a given state from Pocket.

    Args:
        state: Article state ('unread', 'archive', or 'all')

    Returns:
        List of articles from Pocket

    Raises:
        RuntimeError: If article fetch fails
    """
    pocket = get_pocket_instance()
    articles = []
    offset = 0
    count = 100
    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            response = pocket.get(
                state=state,
                detailType="complete",
                count=count,
                offset=offset,
            )

            if "list" not in response[0]:
                break

            items = response[0]["list"]
            if not items:
                break

            articles.extend(items.values())
            offset += count
            retries = 0

        except Exception as e:
            retries += 1
            if retries >= max_retries:
                raise RuntimeError(f"Failed to fetch articles: {e}")
            time.sleep(2**retries)

    return articles


def get_modified_since(timestamp: int) -> Tuple[Dict[str, Any], int]:
    """Get articles modified since given timestamp.

    Args:
        timestamp: Unix timestamp

    Returns:
        Tuple of (modified articles dict, new timestamp)

    Raises:
        RuntimeError: If fetch fails
    """
    pocket = get_pocket_instance()
    response = pocket.get(
        state="all",
        detailType="complete",
        since=timestamp,
    )

    if not response or "list" not in response[0]:
        raise RuntimeError("Failed to fetch updates from Pocket")

    current_time = int(response[0].get("since", time.time()))
    return response[0]["list"], current_time


def get_pocket_instance() -> Pocket:
    """Get authenticated Pocket instance.

    Raises:
        RuntimeError: If the access token is invalid or missing.
    """
    config = Config()
    access_token = config.get("ACCESS_TOKEN")

    if not access_token:
        raise RuntimeError("Access token is missing. Please authenticate first.")

    try:
        pocket_instance = Pocket(
            consumer_key=config.get("CONSUMER_KEY"), access_token=access_token
        )
        # Optionally, you could make a test call to validate the token here
        # e.g., pocket_instance.get() to check if the token is valid
        return pocket_instance
    except Exception as e:
        raise RuntimeError(f"Failed to create Pocket instance: {e}")
