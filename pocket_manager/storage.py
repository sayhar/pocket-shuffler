"""Local storage operations."""

import os
import json
from typing import Any, Dict, List, Optional
from datetime import datetime
from .config import DATA_DIR


def process_article(article: Dict[str, Any]) -> Dict[str, Any]:
    """Process a raw article from Pocket API."""
    return {
        "item_id": article.get("item_id"),
        "resolved_title": article.get("resolved_title"),
        "resolved_url": article.get("resolved_url"),
        "given_url": article.get("given_url"),
        "excerpt": article.get("excerpt"),
        "word_count": article.get("word_count"),
        "time_added": article.get("time_added"),
        "time_read": article.get("time_read"),
        "status": article.get("status"),  # 0: unread, 1: archived
        "is_article": article.get("is_article"),
        "favorite": article.get("favorite") == "1",  # "1" for favorited, "0" for not
        "tags": list(
            article.get("tags", {}).keys()
        ),  # Tags come as a dict with tag names as keys
        "downloaded_at": datetime.now().isoformat(),
    }


def load_articles(filename: str, data_dir: str = DATA_DIR) -> Dict[str, Dict[str, Any]]:
    """Load articles from a JSON file."""
    try:
        with open(os.path.join(data_dir, filename), "r") as f:
            return {article["item_id"]: article for article in json.load(f)}
    except FileNotFoundError:
        return {}


def save_articles(
    articles: List[Dict[str, Any]], filename: str, data_dir: str = DATA_DIR
) -> None:
    """Save articles to a JSON file."""
    os.makedirs(data_dir, exist_ok=True)
    with open(os.path.join(data_dir, filename), "w", newline="\n") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)


def get_last_sync(data_dir: str = DATA_DIR) -> Optional[int]:
    """Get timestamp of last successful sync."""
    try:
        with open(os.path.join(data_dir, "last_sync.json"), "r") as f:
            return json.load(f)["last_sync"]
    except FileNotFoundError:
        return None


def save_last_sync(timestamp: int, data_dir: str = DATA_DIR) -> None:
    """Save timestamp of successful sync."""
    os.makedirs(data_dir, exist_ok=True)
    with open(os.path.join(data_dir, "last_sync.json"), "w", newline="\n") as f:
        json.dump({"last_sync": timestamp}, f)
