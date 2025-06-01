from src.auth_service.utils.clients.http_client import HTTPClient
from auth_service.config.clients import USERS_SERVICE_URL


class UsersHTTPClient(HTTPClient):
    def __init__(self, **kw):
        self.kw = {}
        super().__init__(base_url=USERS_SERVICE_URL, **(self.kw | kw))
