from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class to manage environment variables and application settings."""

    nvidia_key: str = Field(default="")

    model_config = SettingsConfigDict(env_file=".env")
