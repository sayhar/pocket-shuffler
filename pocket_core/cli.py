"""Command line interface for pocket-core."""

import argparse
from .auth import get_access_token
from .sync import sync_articles


def parse_and_run() -> None:
    """Parse arguments and run appropriate command."""
    parser = argparse.ArgumentParser(
        description="Sync and manage Pocket articles locally"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Auth command
    subparsers.add_parser("auth", help="Get Pocket API access token")

    # Sync command
    sync_parser = subparsers.add_parser("sync", help="Sync articles with Pocket")
    sync_parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set logging level (default: INFO)",
    )

    args = parser.parse_args()

    if args.command == "auth":
        get_access_token()
    elif args.command == "sync":
        sync_articles(args.log_level)
    else:
        parser.print_help()
