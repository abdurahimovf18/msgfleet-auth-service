from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.auth_service.utils.log_setup import setup_logging
from .api.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    app.include_router(router)

    yield

