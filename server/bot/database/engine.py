from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models import Base

SQLITE = 'sqlite+aiosqlite:///my_base.db'

engine = create_async_engine(SQLITE, echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
