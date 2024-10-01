from repository import AbstractRepository
from .models import News as NewsModel
from .schemas import CreateNews


class NewsService:
    def __init__(self, news_repo: AbstractRepository):
        self.news_repo: AbstractRepository = news_repo()

    async def get_news(self):
        news = await self.news_repo.find_all()
        return news

    async def news_by_id(self, id: int):
        news = await self.news_repo.get_by_id(id)
        return news

    async def delete_news(self, id: int):
        news = await self.news_repo.delete(id)
        return news

    async def add_one(self, news_in: CreateNews):
        news = NewsModel(**news_in.model_dump())
        news = await self.news_repo.add_one(news)
        return news

    async def update_news(
        self,
        news_id: int,
        news_update: CreateNews,
    ):
        news = await self.news_repo.update(news_id, news_update)
        return news
