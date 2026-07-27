from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    db_url: str
    db_echo: bool
    postgres_db: str
    postgres_user: str
    postgres_password: str


settings = Settings()
