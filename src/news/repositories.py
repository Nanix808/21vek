from repository import SQLAlchemyRepository

from .models import News


class NewsRepository(SQLAlchemyRepository):
    model = News
