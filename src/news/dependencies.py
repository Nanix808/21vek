from .repositories import NewsRepository
from .service import NewsService


def news_service():
    return NewsService(NewsRepository)
