from pydantic import BaseModel


class CoreModel(BaseModel):
    pass


class CreateNews(CoreModel):
    title: str
    text: str = None


class News(CreateNews):
    id: int
