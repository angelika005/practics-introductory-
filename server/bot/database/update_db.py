from hh_api import fetch_vacancies
from save_to_db import save_vacancy
from fetch_params import fetch_params

async def update_vacancies():
    params_list = await fetch_params()
    for params in params_list:
        api_params = {
            'area': params.area,
            'prof_role': params.prof_role,
            'salary': params.salary,
            'schedule': params.schedule,
            'experience': params.experience,
            'employment': params.employment
        }
        vacancies = await fetch_vacancies(api_params)
        for item in vacancies['items']:
            await save_vacancy(item)

if __name__ == '__main__':
    import asyncio
    asyncio.run(update_vacancies())
