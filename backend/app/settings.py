from functools import lru_cache
from pydantic_settings import BaseSettings


class LoggerSettings(BaseSettings):
    SOURCE_TOKEN: str
    BETTERSTACK_HOST: str


class I18nSettings(BaseSettings):
    SUPPORTED_LANGUAGES: list[str] = ["en", "uk", "ru", "it"]
    DEFAULT_LANGUAGE: str = "en"
    LANGUAGE_HEADER: str = "Accept-Language"


class Settings(
    LoggerSettings, I18nSettings
):
    pass


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
