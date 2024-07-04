from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models import Base

SQLITE = 'sqlite+aiosqlite:///my_base.db'
DATABASE_URL = "sqlite+aiosqlite:///vacancies.db"

engine = create_async_engine(SQLITE, echo=True)
engine_hh = create_async_engine(DATABASE_URL, echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
session_maker_hh = async_sessionmaker(bind=engine_hh, class_=AsyncSession, expire_on_commit=False)
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
async def create_vacancy_db():
    async with engine_hh.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def drop_vacancy_db():
    async with engine_hh.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
