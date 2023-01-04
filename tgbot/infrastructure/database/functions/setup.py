from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tgbot.config import DbConfig


def create_session_pool(db: DbConfig, echo=False) -> sessionmaker:
    async_engine = create_async_engine(
        db.construct_sqlalchemy_url(),
        query_cache_size=1200,
        pool_size=20,
        max_overflow=200,
        future=True,
        echo=echo
    )

    session_pool = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
    return session_pool
