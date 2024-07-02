from models_hh import Vacancy
from vacancy_db import async_sessionmaker_hh

async def save_vacancy(vacancy_data):
    async with async_sessionmaker_hh() as session:
        async with session.begin():
            vacancy = Vacancy(
                hh_id=vacancy_data['id'],
                area=vacancy_data['adress']['city'],
                company=vacancy_data['employer']['name'],
                prof_role=vacancy_data['professional_roles']['name'],
                salary=vacancy_data['salary']['name'],
                schedule=vacancy_data['schedule']['name'],
                experience=vacancy_data['experience']['name'],
                employment=vacancy_data['employment']['name'],
                url=vacancy_data['alternate_url']
            )
            session.add(vacancy)
