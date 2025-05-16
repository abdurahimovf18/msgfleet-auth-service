from src.auth_service.utils.http.http_client import HTTPClient
from src.auth_service.config.settings import USERS_SERVICE_URL


class UsersHTTPClient(HTTPClient):
    def __init__(self, **kw):
        self.kw = {}
        super().__init__(base_url=USERS_SERVICE_URL, **(self.kw | kw))
