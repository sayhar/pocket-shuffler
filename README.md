# Pocket Manager

[![Python CI](https://github.com/sayhar/pocket-shuffler/actions/workflows/python.yml/badge.svg)](https://github.com/sayhar/pocket-shuffler/actions)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Uses: pocket](https://img.shields.io/badge/uses-pocket-blue.svg)](https://github.com/tapanpandita/pocket/)

Tool to sync and manage Pocket articles locally.

## Dependencies

- [pocket](https://github.com/tapanpandita/pocket/) - Python wrapper for the Pocket API

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Get your Pocket access token (first time only):

```bash
python -m pocket_manager.auth
```

3. When prompted:
   - Click the authorization URL
   - Log into Pocket and authorize the app
   - Copy the access token
   - Update `ACCESS_TOKEN` in `pocket_manager/config.py`

## Usage

### Sync Articles

Download or update articles from Pocket:

```bash
python -m pocket_manager

# Set logging level (recommended):
python -m pocket_manager --log-level DEBUG
```

This will:

- Download all articles if running for the first time
- Only fetch changes since last sync on subsequent runs
- Store articles in `pocket_data/` directory:
  - `unread_articles.json`: Current unread articles
  - `archived_articles.json`: Archived articles
  - `last_sync.json`: Timestamp of last successful sync

## File Structure

```
pocket_manager/
├── __init__.py # Package initialization
├── __main__.py # Command-line entry point
├── api.py # Pocket API functions
├── auth.py # Authentication utilities
├── cli.py # Command-line interface
├── config.py # Configuration and credentials
├── logging.py # Logging configuration
├── storage.py # Local storage operations
└── sync.py # Main sync logic

pocket_data/ # Created automatically
├── unread_articles.json # Current unread articles
├── archived_articles.json # Archived articles
└── last_sync.json # Timestamp of last successful sync
```

## Troubleshooting

- First time setup:

  1. Run `auth.py` to get your access token
  2. Copy the token to `config.py`
  3. Run `sync.py` to download your articles

- If sync fails:
  1. Check your API credentials in `config.py`
  2. Delete `last_sync.json` to force a full refresh
  3. Run sync again

## Future Plans

1. **Hosting**

   - Deploy as a web service (likely on Fly.io or Railway)
   - SQLite database for article storage
   - Simple authentication system

2. **Web Interface**

   - Show random article suggestions
   - Allow archiving articles directly
   - Add favorites/annotations
   - Basic article management

3. **Mobile Access**

   - Simple mobile interface
   - Quick article actions

4. **Multi-user Support**
   - User accounts
   - Individual article collections
   - Shared annotations

Log levels:

- DEBUG: Show all details including article modifications
- INFO: Show basic sync progress (default)
- WARNING: Show only warnings and errors
- ERROR: Show only errors
