from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env", env_file_encoding="utf-8")
    debug: bool = False
    postgres_drivername: str = "postgresql+asyncpg"
    postgres_host: str = "fastrawgis-db"
    postgres_port: int = 5432
    postgres_database: str = "postgres"
    postgres_username: str = "postgres"
    postgres_password: str = "postgres"


@lru_cache
def get_settings() -> Settings:
    return Settings()
