# Pocket Manager

[![Python CI](https://github.com/sayhar/pocket-shuffler/actions/workflows/python.yml/badge.svg)](https://github.com/sayhar/pocket-shuffler/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/code%20linting-ruff-red)](https://github.com/astral-sh/ruff)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-blue)](https://github.com/python/mypy)
[![Uses: pocket](https://img.shields.io/badge/uses-pocket-blue.svg)](https://github.com/tapanpandita/pocket/)

## Overview

This project started as a Pocket sync tool but is evolving into a platform for sharing my reading life. The goal is to create a window into my intellectual journey - what I read, when I read it, and what I think about it.

## Project Structure

The project is split into components:

- `pocket-core/` - Core sync and storage engine
  - Syncs with Pocket API
  - Maintains local state
  - Will provide API for other components

Future components:

- `web/` - Web interface for public viewing
- `mobile/` - iPhone and Android interface?
- `api/` - REST API for integrations
- `writers/` - Optional integrations to write annotations to other systems (e.g., Obsidian)

## Dependencies

- [pocket](https://github.com/tapanpandita/pocket/) - Python wrapper for the Pocket API

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, create a `config.json` file based on `config.json.template`. Fill in the required fields:

- `CONSUMER_KEY`: Your Pocket API consumer key.
- `REDIRECT_URI`: The URI to redirect after authorization.
- `ACCESS_TOKEN`: This will be populated after running the authentication command.
- Logging and data storage configurations can also be set here.

## Usage

### Command Line Usage

```bash
python -m pocket_core            # Show help
python -m pocket_core auth       # Get authorization token
python -m pocket_core sync       # Sync with default settings
python -m pocket_core sync --log-level DEBUG  # Sync with debug output
```

### Library Usage

```python
from pocket_core import config
from pocket_core.sync import sync_articles

# Get authorization
token = get_access_token()  # This will automatically save the token to config.json

# Read config values
value = config.get("SOME_KEY")

# Update config
config.set("SOME_KEY", "new_value")

# Sync articles
sync_articles(log_level="DEBUG")  # Optional: set log level
```

## Authentication

First time setup to get your Pocket access token:

```bash
python -m pocket_core auth  # Get authorization token
# Follow the prompts to authorize and get your token
# The token will be saved in pocket_core/config.json
```

## Logging

Logging configuration can be adjusted in `config.json`. The following fields are available:

- `LOG_FORMAT`: Format of the log messages.
- `DEFAULT_LOG_LEVEL`: Default logging level (e.g., DEBUG, INFO).
- `LOG_DATE_FORMAT`: Format for the date in log messages.

## Future Plans

### Short Term

1. Hosting
   Deploy as a web service (likely on Fly.io or Railway) to make the tool accessible online.
   Use an SQLite database for article storage to allow for more complex queries and data management.
   Implement a simple authentication system to secure user data.
2. Web Interface
   Develop a user-friendly web interface to show random article suggestions.
   Allow users to archive articles directly from the web interface.
   Implement features for adding favorites and annotations.
   Provide basic article management capabilities.
3. Mobile Access
   Create a simple mobile interface for quick article actions.
   Implement push notifications for new articles or updates.
   Long Term Vision
4. Public Reading Stream
   Show what I'm currently reading in real-time.
   Create a timeline of when articles were read.
   Share thoughts and annotations on articles.
   Provide context on why certain articles matter to me.
5. Social Features
   Allow users to comment on reading choices.
   Suggest related articles based on reading patterns.
   Enable users to ask questions about articles.
   Share reading patterns and interests with others.
6. Integration Points
   Write annotations to Obsidian or other note-taking apps.
   Connect with other reading services for a more comprehensive experience.
   Export data in various formats for offline use or backup.
