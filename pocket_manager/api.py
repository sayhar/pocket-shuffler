"""Pocket API interactions."""

import time
from typing import Any, Dict, List, Tuple
from pocket import Pocket
from .config import CONSUMER_KEY, ACCESS_TOKEN


def get_articles(state: str = "all") -> List[Dict[str, Any]]:
    """Get all articles of a given state from Pocket.

    Args:
        state: Article state ('unread', 'archive', or 'all')

    Returns:
        List of articles from Pocket

    Raises:
        RuntimeError: If article fetch fails
    """
    pocket = Pocket(CONSUMER_KEY, ACCESS_TOKEN)
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
    pocket = Pocket(CONSUMER_KEY, ACCESS_TOKEN)
    response = pocket.get(
        state="all",
        detailType="complete",
        since=timestamp,
    )

    if not response or "list" not in response[0]:
        raise RuntimeError("Failed to fetch updates from Pocket")

    current_time = int(response[0].get("since", time.time()))
    return response[0]["list"], current_time
