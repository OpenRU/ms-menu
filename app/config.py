import os
from pathlib import Path
from typing import Any

from flask.cli import load_dotenv

BASE_DIR = Path(__file__).parent.parent.resolve()
ENV_PATH = BASE_DIR / ".env"

if not ENV_PATH.exists():
    raise RuntimeError(f"Arquivo .env não encontrado em {ENV_PATH}")

load_dotenv(ENV_PATH)

MS_AUTH_PREFIX = os.getenv("MS_AUTH_PREFIX")


class BaseSettings:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    API_TITLE = "MS-MENU"
    API_VERSION = "v1"
    OPENAPI_VERSION = os.getenv("OPENAPI_VERSION", "3.0.2")


class ProductionSettings(BaseSettings):
    DEBUG = False

    OPENAPI_URL_PREFIX = None
    OPENAPI_SWAGGER_UI_PATH = None
    OPENAPI_SWAGGER_UI_URL = None


class DevelopmentSettings(BaseSettings):
    DEBUG = True

    OPENAPI_URL_PREFIX = os.getenv("OPENAPI_URL_PREFIX", "/")
    OPENAPI_SWAGGER_UI_PATH = os.getenv("OPENAPI_SWAGGER_UI_PATH", "/swagger-ui")
    OPENAPI_SWAGGER_UI_URL = os.getenv("OPENAPI_SWAGGER_UI_URL", "https://cdn.jsdelivr.net/npm/swagger-ui-dist/")

    API_SPEC_OPTIONS: dict[str, Any] = {
        "security": [{"bearerAuth": []}],
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        }
    }
