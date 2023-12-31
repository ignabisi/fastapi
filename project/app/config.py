import logging
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    # bool(0) = False
    # bool(1) = True
    testing: bool = bool(0)
    databse_url: AnyUrl = None


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
