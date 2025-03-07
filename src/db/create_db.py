
from src.db.async_db import engine
from src.models.base import Base


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
