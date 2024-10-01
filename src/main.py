from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

import redis

from config import settings
from news.router import news_router
from tasks import celery
from celery.schedules import crontab


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis_0 = aioredis.from_url(settings.REDIS_URL)
    FastAPICache.init(RedisBackend(redis_0), prefix="fastapi-cache")
    yield


app = FastAPI(
    lifespan=lifespan,
    debug=settings.debug,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Запрос: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Ответ: {response.status_code}")
    return response


# Add the router to FastAPI
app.include_router(news_router, prefix="/news", tags=["news"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Запуск сервера Uvicorn
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
