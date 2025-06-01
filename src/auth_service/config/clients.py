from typing import Optional
from pydantic_settings import SettingsConfigDict
from pydantic import HttpUrl, Field

from .base import SECRETS_DIR, BaseEnv


class Env(BaseEnv):
    # Optional service base URLs
    USERS_SERVICE_URL: Optional[HttpUrl] = Field(default=None)
    AUTH_SERVICE_URL: Optional[HttpUrl] = Field(default=None)

    model_config = SettingsConfigDict(
        env_file=SECRETS_DIR / ".clients.env",
    )


env = Env()


USERS_SERVICE_URL = env.USERS_SERVICE_URL
AUTH_SERVICE_URL = env.AUTH_SERVICE_URL
