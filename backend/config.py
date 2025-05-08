from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings class to manage environment variables and application settings."""

    aws_bedrock_flow_id: str

    model_config = SettingsConfigDict(env_file=".env")
