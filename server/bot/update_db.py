from database.hh_api import fetch_vacancies
from save_to_db import save_vacancy
from database.fetch_params import fetch_params
import aiohttp

VALID_SCHEDULE_VALUES = {
    'Полный день': 'fullDay',
    'Сменный график': 'shift',
    'Гибкий график': 'flexible',
    'Удаленная работа': 'remote',
    'Вахтовый метод': 'flyInFlyOut'
}

VALID_EXPERIENCE_VALUES = {
    'Нет опыта': 'noExperience',
    'От 1 года до 3 лет': 'between1And3',
    'От 3 до 6 лет': 'between3And6',
    'Более 6 лет': 'moreThan6'
}

VALID_EMPLOYMENT_VALUES = {
    'Полная занятость': 'full',
    'Частичная занятость': 'part',
    'Проектная работа': 'project',
    'Волонтерство': 'volunteer',
    'Стажировка': 'probation'
}

def map_schedule(schedule):
    return VALID_SCHEDULE_VALUES.get(schedule, '')

def map_experience(experience):
    return VALID_EXPERIENCE_VALUES.get(experience, '')

def map_employment(employment):
    return VALID_EMPLOYMENT_VALUES.get(employment, '')


async def get_areas():
    url = "https://api.hh.ru/areas"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch areas: {response.status}")
            data = await response.json()
            return data


async def get_professional_roles():
    url = "https://api.hh.ru/professional_roles"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch professional roles: {response.status}")
            data = await response.json()
            return data


def find_area_id_by_name(areas, name):
    for area in areas:
        if area['name'] == name:
            return area['id']
        for sub_area in area.get('areas', []):
            if sub_area['name'] == name:
                return sub_area['id']
    return ''


def find_prof_role_id_by_name(prof_roles, name):
    for role in prof_roles['categories']:
        for spec in role['roles']:
            if spec['name'] == name:
                return spec['id']
    return ''


async def fetch_params_by_name(area_name, prof_role_name):
    areas = await get_areas()
    prof_roles = await get_professional_roles()

    area_id = find_area_id_by_name(areas, area_name)
    prof_role_id = find_prof_role_id_by_name(prof_roles, prof_role_name)

    return area_id, prof_role_id


async def update_vacancies():
    params_list = await fetch_params()
    for params in params_list:
        area_id, prof_role_id = await fetch_params_by_name(params.area, params.prof_role)
        api_params = {
            'area': area_id,
            'professional_role': prof_role_id,
            'salary': params.salary,
            'schedule': map_schedule(params.schedule),
            'experience': map_experience(params.experience),
            'employment': map_employment(params.employment)
        }
        vacancies = await fetch_vacancies(api_params)
        print(vacancies)
        for item in vacancies['items']:
            await save_vacancy(item)
