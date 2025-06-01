from typing import Optional
from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .base import BaseEnv, SECRETS_DIR


class Env(BaseEnv):

    DEBUG: Optional[bool] = Field(default=True)

    # JWT authentication
    JWT_ALGORITHM: str
    JWT_ISS: str
    JWT_EXP: int

    model_config = SettingsConfigDict(
        env_file=SECRETS_DIR / "app" / ".env"
    )


env = Env()


PRIVATE_KEY_FILE = SECRETS_DIR / "private_key.pem"

try:
    with PRIVATE_KEY_FILE.open("r") as f:
        JWT_PRIVATE_KEY = f.read()
except FileNotFoundError:
    raise RuntimeError(
        f"{PRIVATE_KEY_FILE} not found.\n"
        "This file contains the JWT private key used for token verification.\n"
        "Please ensure it exists and is accessible at runtime."
    )

JWT_ALGORITHM = env.JWT_ALGORITHM
JWT_ISS = env.JWT_ISS
JWT_EXP = env.JWT_EXP
