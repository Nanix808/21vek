import os
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent
DOTENV = os.path.join(os.path.join(BASE_DIR, ".env"))


print(BASE_DIR, DOTENV)


class Settings(BaseSettings):
    """Class Settings"""

    # model_config = SettingsConfigDict(env_file=DOTENV)

    debug: bool = True
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_echo: bool = False
    redis_port: int = 6379
    redis_host: str = "redis"

    @property
    def DATABASE_URL_psycopg(self):
        """URL connect DB"""
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def REDIS_URL(self):
        """URL connect DB"""
        return f"redis://{self.redis_host}:{self.redis_port}/0"


settings = Settings()
