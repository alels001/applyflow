from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or a .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APPLYFLOW_",
        extra="ignore",
    )

    demo_mode: bool = True
    timezone: str = "Europe/Berlin"
    database_url: str = "sqlite:///data/applyflow.db"
