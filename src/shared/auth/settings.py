from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from auth_service.config.base import BASE_DIR


AUTH_SECRETS_DIR = BASE_DIR / "secrets" / "auth"
PUBLIC_KEY_FILE = AUTH_SECRETS_DIR / "public_key.pem"


class AuthConfig(BaseSettings):
    JWT_ALGORITHM: str
    JWT_ISS: str

    model_config = SettingsConfigDict(
        env_file=AUTH_SECRETS_DIR / ".env",
        extra="ignore",
    )


auth_config = AuthConfig()

JWT_ALGORITHM = auth_config.JWT_ALGORITHM
JWT_ISS = auth_config.JWT_ISS

try:
    with PUBLIC_KEY_FILE.open("r") as f:
        JWT_PUBLIC_KEY = f.read()
except FileNotFoundError:
    raise RuntimeError(
        f"{PUBLIC_KEY_FILE} not found.\n"
        "This file contains the JWT public key used for token verification.\n"
        "Please ensure it exists and is accessible at runtime."
    )
