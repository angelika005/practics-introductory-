from sqlalchemy.future import select
from vacancy_db import async_sessionmaker_hh
from models import Product

#Для извлечения параметров запросов из бд телеграмма
async def fetch_params():
    async with async_sessionmaker_hh() as session:
        async with session.begin():
            result = await session.execute(select(Product))
            params = result.scalars().all()
            return params
