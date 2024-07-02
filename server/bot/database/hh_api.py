import aiohttp
import os

HH_API_URL = "https://api.hh.ru/vacancies"
HH_API_TOKEN = 'APPLHIOPSPUH2TUHNNE7T1P4129Q3QNTV4ERREEM4390JVI58LKCO042OJMASC9I'

async def fetch_vacancies(params):
    headers = {
        "User-Agent": "CareerPathBot/1.0",
        "Authorization": f"Bearer {HH_API_TOKEN}"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(HH_API_URL, headers=headers, params=params) as response:
            return await response.json()