from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///vacancies.db"

engine_hh = create_async_engine(DATABASE_URL, echo=True)
Base_hh = declarative_base()
async_sessionmaker_hh = sessionmaker(bind=engine_hh, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with engine_hh.begin() as conn:
        await conn.run_sync(Base_hh.metadata.create_all)

async def drop_db():
    async with engine_hh.begin() as conn:
        await conn.run_sync(Base_hh.metadata.drop_all)