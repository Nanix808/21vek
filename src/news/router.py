from typing import Annotated

from fastapi import APIRouter, Depends, status, Path
from fastapi_cache.decorator import cache

from .dependencies import news_service
from .service import NewsService
from .schemas import News, CreateNews

news_router = APIRouter()


@news_router.get("/", response_model=list[News])
@cache(expire=30)
async def get_news(
    news_service: Annotated[NewsService, Depends(news_service)],
) -> list[News]:
    news = await news_service.get_news()
    return news


@news_router.get("/{news_id}", response_model=News)
async def get_news_by_id(
    news_service: Annotated[NewsService, Depends(news_service)],
    news_id: int = Path(...),
):
    news = await news_service.news_by_id(news_id)
    return news


@news_router.post(
    "/",
    response_model=CreateNews,
    status_code=status.HTTP_201_CREATED,
)
async def create_news(
    news_service: Annotated[NewsService, Depends(news_service)],
    news_in: CreateNews,
) -> CreateNews:
    news = await news_service.add_one(news_in)
    return news


@news_router.patch("/{news_id}", response_model=News)
async def update_news(
    news_service: Annotated[NewsService, Depends(news_service)],
    news_update: CreateNews,
    news_id: int = Path(...),
):
    news = await news_service.update_news(news_id, news_update)
    return news


@news_router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(
    news_service: Annotated[NewsService, Depends(news_service)],
    news_id: int = Path(...),
) -> None:
    await news_service.delete_news(news_id)
