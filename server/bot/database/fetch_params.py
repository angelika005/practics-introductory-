from sqlalchemy.future import select
from engine import session_maker
from models import Product

#Для извлечения параметров запросов из бд телеграмма
async def fetch_params():
    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(Product))
            params = result.scalars().all()
            return params
