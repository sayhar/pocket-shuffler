from typing import Any, Dict, List, Tuple

class Pocket:
    def __init__(self, consumer_key: str, access_token: str) -> None: ...
    @staticmethod
    def get_request_token(consumer_key: str, redirect_uri: str) -> str: ...
    @staticmethod
    def get_auth_url(code: str, redirect_uri: str) -> str: ...
    @staticmethod
    def get_credentials(consumer_key: str, code: str) -> Dict[str, str]: ...
    def get(
        self,
        state: str = ...,
        detailType: str = ...,
        count: int = ...,
        offset: int = ...,
        since: int = ...,
    ) -> Tuple[Dict[str, Any], ...]: ...
