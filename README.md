# Pocket Manager

[![Python CI](https://github.com/sayhar/pocket-shuffler/actions/workflows/python.yml/badge.svg)](https://github.com/sayhar/pocket-shuffler/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Uses: pocket](https://img.shields.io/badge/uses-pocket-blue.svg)](https://github.com/tapanpandita/pocket/)

## Overview

This project started as a Pocket sync tool but is evolving into a platform for sharing my reading life.
The goal is to create a window into my intellectual journey - what I read, when I read it, and what I think about it.

## Project Structure

The project is split into components:

- `pocket-core/` - Core sync and storage engine
  - Syncs with Pocket API
  - Maintains local state
  - Will provide API for other components

Future components:

- `web/` - Web interface for public viewing
- `api/` - REST API for integrations
- `writers/` - Optional integrations to write annotations to other systems (e.g., Obsidian)

## Dependencies

- [pocket](https://github.com/tapanpandita/pocket/) - Python wrapper for the Pocket API

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Get your Pocket access token (first time only):

```bash
python -m pocket_core.auth  # Get Pocket authorization
# Copy the access token to pocket_core/config.py

python -m pocket_core      # Start syncing
```

## Usage

### Sync Articles

Download or update articles from Pocket:

```bash
python -m pocket_core

# Set logging level (recommended):
python -m pocket_core --log-level DEBUG
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
pocket_core/
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

### Short Term

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

### Long Term Vision

1. **Public Reading Stream**

   - Show what I'm currently reading
   - Timeline of when I read articles
   - My thoughts and annotations
   - Context of why articles matter to me

2. **Social Features**

   - Allow comments on my reading choices
   - Suggest related articles
   - Ask questions about articles
   - Share reading patterns and interests

3. **Integration Points**

   - Write annotations to Obsidian
   - Connect with other reading services
   - Export data in various formats

4. **Analytics & Insights**
   - Reading patterns over time
   - Topic clustering
   - Connection mapping between articles
   - Personal knowledge graph visualization

Log levels:

- DEBUG: Show all details including article modifications
- INFO: Show basic sync progress (default)
- WARNING: Show only warnings and errors
- ERROR: Show only errors
