from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class News(Base):
    title: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    text: Mapped[str] = mapped_column(String(256))
