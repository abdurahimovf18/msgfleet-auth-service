from pathlib import Path
from datetime import timezone, timedelta
from typing import Optional
import sys

from pydantic import Field, HttpUrl
from pydantic_settings import SettingsConfigDict, BaseSettings


# ---------------------------------------------
# Base directory for locating env files and logs
# ---------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SECRETS_DIR = BASE_DIR / "secrets"
APP_SECRETS_DIR = SECRETS_DIR / "app"

# ---------------------------------------------
# Static settings / constants
# ---------------------------------------------

DEBUG: bool = True
TIMEZONE = timezone.utc

# ---------------------------------------------
# Environment: Core Application & Database
# ---------------------------------------------

class Env(BaseSettings):
    # PostgreSQL configuration
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DATABASE: str

    # JWT authentication
    JWT_ALGORITHM: str
    JWT_ISS: str
    JWT_EXP: int

    model_config = SettingsConfigDict(
        env_file=APP_SECRETS_DIR / ".env",
    )


# ---------------------------------------------
# Environment: Microservice URLs
# ---------------------------------------------

class ServiceUrlsEnv(BaseSettings):
    # Optional service base URLs
    USERS_SERVICE_URL: Optional[HttpUrl] = Field(default=None)
    AUTH_SERVICE_URL: Optional[HttpUrl] = Field(default=None)

    model_config = SettingsConfigDict(
        env_file=APP_SECRETS_DIR / ".service-urls.env",
    )


# ---------------------------------------------
# Environment Instances
# ---------------------------------------------

env = Env()
service_urls = ServiceUrlsEnv()


# ---------------------------------------------
# Database URLs (build elsewhere if needed)
# ---------------------------------------------

ASYNC_DATABASE_URL = f"postgresql+asyncpg://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}"
SYNC_DATABASE_URL = f"postgresql+psycopg2://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}"


# ---------------------------------------------
# JWT Settings
# ---------------------------------------------

PRIVATE_KEY_FILE = APP_SECRETS_DIR / "private_key.pem"

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

# ---------------------------------------------
# Microservice URLs (optional values)
# ---------------------------------------------

USERS_SERVICE_URL = service_urls.USERS_SERVICE_URL
AUTH_SERVICE_URL = service_urls.AUTH_SERVICE_URL


# ---------------------------------------------
# Logging Configuration
# ---------------------------------------------

LOG_DEBUG_SETTINGS = [
    {
        "sink": sys.stdout,
        "format": "<green>{time: YYYY:MM:DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>",
        "colorize": True,
        "level": "DEBUG",
    },
    {
        "sink": BASE_DIR / "logs/debug.log",
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        "rotation": "7 days",
        "retention": "1 month",
        "compression": "zip",
    }
]

LOG_PRODUCTION_SETTINGS = [
    {
        "sink": BASE_DIR / "logs/app.log",
        "level": "INFO",
        "format": "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
        "rotation": "7 days",
        "retention": "1 month",
        "compression": "zip",
        "enqueue": True
    }
]
