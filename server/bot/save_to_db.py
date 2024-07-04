from database.models import Vacancy
from database.engine import session_maker_hh


async def save_vacancy(vacancy_data):
    async with session_maker_hh() as session:
        async with session.begin():
            professional_roles = [role['name'] for role in vacancy_data['professional_roles']]
            vacancy = Vacancy(
                hh_id=vacancy_data['id'],
                area=vacancy_data['area']['name'],
                company=vacancy_data['employer']['name'],
                prof_role=professional_roles,
                salary=vacancy_data['salary']['from'] if vacancy_data['salary'] else None,
                schedule=vacancy_data['schedule']['name'],
                experience=vacancy_data['experience']['name'],
                employment=vacancy_data['employment']['name'],
                url=vacancy_data['alternate_url']
            )
            session.add(vacancy)
