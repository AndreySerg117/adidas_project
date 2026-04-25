from functools import lru_cache
from pydantic_settings import BaseSettings


class LoggerSettings(BaseSettings):
    SOURCE_TOKEN: str
    BETTERSTACK_HOST: str


class Settings(
    LoggerSettings
):
    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()