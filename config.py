import os

import pydantic_settings

BASE_DIR = os.path.dirname(__file__)


class Settings(pydantic_settings.BaseSettings):
    BASE_URL: str
    TOKEN: str


settings = Settings(_env_file=os.path.join(BASE_DIR, '.env'))
