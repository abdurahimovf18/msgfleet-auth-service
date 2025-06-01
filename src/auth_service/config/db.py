from pydantic_settings import SettingsConfigDict
from .base import BaseEnv, SECRETS_DIR


class Env(BaseEnv):
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DATABASE: str

    model_config = SettingsConfigDict(
        env_file=SECRETS_DIR / "db" / ".env"
    )


env = Env()

ASYNC_DATABASE_URL = (f"postgresql+asyncpg://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}"
                      f"@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}")

SYNC_DATABASE_URL = (f"postgresql+psycopg2://{env.POSTGRESQL_USER}:{env.POSTGRESQL_PASSWORD}"
                     f"@{env.POSTGRESQL_HOST}:{env.POSTGRESQL_PORT}/{env.POSTGRESQL_DATABASE}")

