from typing import Literal
import sys

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .base import BaseEnv, SECRETS_DIR


class Env(BaseEnv):
    LOG_LEVEL: Literal["INFO", "DEBUG", "WARNING", "CRITICAL", "ERROR"] = Field(default="INFO")

    model_config = SettingsConfigDict(
        env_file=SECRETS_DIR / ".logging.env"
    )


env = Env()


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "stream": sys.stdout,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": env.LOG_LEVEL,
    },
    "loggers": {
        "uvicorn": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "sqlalchemy.engine": {"level": "WARNING"},
    },
}
