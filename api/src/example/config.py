"""Application configuration."""

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration."""

    model_config = SettingsConfigDict(env_prefix="EXAMPLE_")

    db_dsn: PostgresDsn
