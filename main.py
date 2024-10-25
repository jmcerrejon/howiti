import os
from enum import Enum

from fastapi import FastAPI
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from services.api.v1.qr_router import qr_router

QR_ROUTER_PREFIX = "/api/v1"
QR_DEFAULT_PATH = "qr"


class EnvironmentType(str, Enum):
    LOCAL = "local"
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class Settings(BaseSettings):
    debug: bool = False
    environment: str = EnvironmentType.LOCAL
    app_version: str = "0.0.0"
    base_url: str = "https://howiti.com"
    app_name: str
    description: str
    qr_code_example: str
    qr_code_example_url: str
    pythonpath: str = "."

    model_config = ConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".", ".env"),
        extra="forbid",
    )


settings = Settings()
app = FastAPI(
    title=settings.app_name,
    description=settings.description,
    version=settings.app_version,
)
app.include_router(qr_router, prefix="/api")


@app.get(f"{QR_ROUTER_PREFIX}")
async def read_root():
    return {
        "Provide": f"{settings.app_name} API REST",
        "App_Version": settings.app_version,
        "URL": settings.base_url,
    }
