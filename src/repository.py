from abc import ABC, abstractmethod

from sqlalchemy import select

from database import db_helper


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    def get_by_id(id: id):
        """Retrieves entity by its identity"""
        raise NotImplementedError()

    @abstractmethod
    def update(id: id):
        """Retrieves entity by its identity"""
        raise NotImplementedError()


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, empty: dict) -> int:
        async with db_helper.session_dependency() as session:
            session.add(empty)
            await session.commit()
            await session.refresh(empty)
            return empty

    async def find_all(self):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model).order_by(self.model.id)
            res = await session.execute(stmt)
            return res.scalars().all()

    async def get_by_id(self, id: int, *args, **kwargs):
        async with db_helper.session_dependency() as session:
            stmt = select(self.model).where(self.model.id == id)
            empty = await session.execute(stmt)
            empty = empty.scalars().first()
            if empty:
                return empty

    async def update(self, id, data, exclude=True):
        async with db_helper.session_dependency() as session:
            print(id, data)
            empty = await session.get(self.model, id)
            for name, value in data.model_dump(exclude_unset=exclude).items():
                setattr(empty, name, value)
            await session.commit()
            return empty

    async def delete(self, id):
        async with db_helper.session_dependency() as session:
            empty = await session.get(self.model, id)
            if empty:
                await session.delete(empty)
                await session.commit()
            return empty
