from typing import Optional
from pathlib import Path
from datetime import timezone

from pydantic import Field, field_validator
from pydantic_settings import SettingsConfigDict, BaseSettings
import zoneinfo


class BaseEnv(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore"
    )


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
SECRETS_DIR = BASE_DIR / "secrets" / "app"


class Env(BaseEnv):
    DEBUG: Optional[bool] = Field(default=True)
    TIMEZONE: Optional[str] = Field(default="UTC")

    @field_validator("TIMEZONE")
    def parse_timezone(cls, v: str):
        if isinstance(v, timezone):
            return v
        if v == "UTC":
            return timezone.utc
        try:
            return zoneinfo.ZoneInfo(v)
        except Exception:
            raise ValueError(f"Invalid timezone: {v}")
    
    model_config = SettingsConfigDict(
        env_file=SECRETS_DIR / ".env",
    )

env = Env()

DEBUG: bool = env.DEBUG
TIMEZONE: timezone = env.TIMEZONE

