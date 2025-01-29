"""Authentication utilities for Pocket API."""

from pocket import Pocket
from .config import CONSUMER_KEY, REDIRECT_URI


def get_access_token() -> str:
    """Get access token for Pocket API.

    Interactive function that:
    1. Gets a request token
    2. Shows authorization URL
    3. Waits for user to authorize
    4. Returns access token

    Returns:
        str: The access token to use with Pocket API

    Raises:
        RuntimeError: If token retrieval fails
    """
    try:
        request_token = Pocket.get_request_token(
            consumer_key=CONSUMER_KEY, redirect_uri=REDIRECT_URI
        )

        auth_url = Pocket.get_auth_url(code=request_token, redirect_uri=REDIRECT_URI)

        print(f"Go to this URL to authorize the app:\n{auth_url}")
        input("Press Enter after you've authorized the app...")

        user_credentials = Pocket.get_credentials(
            consumer_key=CONSUMER_KEY, code=request_token
        )
        access_token = user_credentials["access_token"]
        print(f"\nYour access token is: {access_token}")
        return access_token
    except Exception as e:
        raise RuntimeError(f"Error retrieving access token: {e}") from e


if __name__ == "__main__":
    get_access_token()
