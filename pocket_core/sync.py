"""Main sync logic for Pocket articles."""

import logging
import time
from datetime import datetime

from .cli import parse_args
from .logging import setup_logging
from .api import get_articles, get_modified_since
from .storage import (
    process_article,
    load_articles,
    save_articles,
    get_last_sync,
    save_last_sync,
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for sync command."""
    args = parse_args()
    setup_logging(args)
    sync_articles()


def sync_articles() -> None:
    """Sync local articles with Pocket.

    Raises:
        RuntimeError: If sync fails
    """
    logger.info("Starting sync")

    # Get last sync time
    since = get_last_sync()
    if since is None:
        logger.info("No previous sync found. Performing full download...")
        # Download all articles
        unread = [process_article(a) for a in get_articles("unread")]
        archived = [process_article(a) for a in get_articles("archive")]

        # Save articles
        save_articles(unread, "unread_articles.json")
        save_articles(archived, "archived_articles.json")

        # Save sync time
        save_last_sync(int(time.time()))
        logger.info("Initial download complete")
        return

    # Get modified articles since last sync
    logger.info(f"Fetching changes since {datetime.fromtimestamp(since)}")
    try:
        modified, current_time = get_modified_since(since)

        # Load current state
        local_unread = load_articles("unread_articles.json")
        local_archived = load_articles("archived_articles.json")

        # Update collections
        updated_unread = local_unread.copy()
        updated_archived = local_archived.copy()

        # Process modified articles
        for article_id, article in modified.items():
            processed = process_article(article)

            # Log the modification
            title = processed.get("resolved_title", "No title")
            status = article.get("status")
            location = (
                "unread"
                if article_id in local_unread
                else "archived"
                if article_id in local_archived
                else "not in collections"
            )
            logger.debug(f"Article modified: {title}")
            logger.debug(f"  Status: {status} (was in {location})")
            logger.debug(f"  Favorite: {processed.get('favorite')}")
            logger.debug(f"  Tags: {', '.join(processed.get('tags', []))}")

            # Remove from both collections first
            updated_unread.pop(article_id, None)
            updated_archived.pop(article_id, None)

            # Add to appropriate collection based on status
            if article.get("status") == "0":  # unread
                updated_unread[article_id] = processed
                logger.debug("  → Added to unread")
            elif article.get("status") == "1":  # archived
                updated_archived[article_id] = processed
                logger.debug("  → Added to archived")
            else:
                logger.debug("  → Removed (deleted)")

        # Save updated state
        save_articles(list(updated_unread.values()), "unread_articles.json")
        save_articles(list(updated_archived.values()), "archived_articles.json")
        save_last_sync(current_time)

        # Print summary
        logger.info("Sync Summary:")
        logger.info(f"Modified articles: {len(modified)}")
        logger.info(f"Unread articles: {len(local_unread)} → {len(updated_unread)}")
        logger.info(
            f"Archived articles: {len(local_archived)} → {len(updated_archived)}"
        )

    except Exception as e:
        logger.error(f"Sync failed: {e}")
        raise RuntimeError(f"Sync failed: {e}") from e

    logger.info("Sync completed")
