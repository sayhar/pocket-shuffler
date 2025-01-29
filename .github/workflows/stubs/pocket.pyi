from typing import Any, Dict, TypedDict

class PocketCredentials(TypedDict):
    access_token: str
    username: str

class PocketArticleList(TypedDict):
    list: Dict[str, Dict[str, Any]]
    since: int

class Pocket:
    def __init__(self, consumer_key: str, access_token: str) -> None: ...
    @staticmethod
    def get_request_token(consumer_key: str, redirect_uri: str) -> str: ...
    @staticmethod
    def get_auth_url(code: str, redirect_uri: str) -> str: ...
    @staticmethod
    def get_credentials(consumer_key: str, code: str) -> Dict[str, str]: ...
    def get(self, **kwargs: Any) -> list[Dict[str, Any]]: ...
