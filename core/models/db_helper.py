from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from core.config import settings


class DatabaseSettings:
    def __init__(self, db_url, db_echo: bool = False):
        self.engine = create_async_engine(
            db_url,
            echo=db_echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseSettings(
    db_url=settings.db_url,
    db_echo=settings.db_echo,
)
