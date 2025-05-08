from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class to manage environment variables and application settings."""

    aws_bedrock_flow_id: str
    aws_access_key_id: str = Field(default="")
    aws_secret_access_key: str = Field(default="")

    model_config = SettingsConfigDict(env_file=".env")
