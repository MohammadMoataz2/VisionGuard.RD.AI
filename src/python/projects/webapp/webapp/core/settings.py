import os
import secrets
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    web_app_name: str = "visionguard.tech.ai.webapp"
    app_version: str = "0.0.1"
    api_auth_username: str = "Foo"
    api_auth_password: str = "Bar"

    api_auth_admin_username: str = "Bar"
    api_auth_admin_password: str = "Baz"

    API_V_STR: str = "/api/v1"

    API_CONN_STRING: str = "http://localhost"

    APP_DEBUG: bool = True

    LOGGER_PREFIX: str = ""




    class Config:
        case_sensitive = True
        env_file = os.getenv("APP_DOTENV_PATH", ".env")  # Use a default `.env` file if not explicitly set
        env_file_encoding = "utf-8"
        extra = "allow"



settings = Settings()
if settings.APP_DEBUG:
    from pprint import pprint

    pprint(settings.dict())