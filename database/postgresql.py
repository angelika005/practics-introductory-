import time
import random
import logging
import requests
import psycopg2

hh_token = 'APPLHIOPSPUH2TUHNNE7T1P4129Q3QNTV4ERREEM4390JVI58LKCO042OJMASC9I'

# Конфигурация базы данных
db_config = {
    'dbname': 'vacancies_db',
    'user': 'lika_user',
    'password': 'first_db',
    'host': '127.0.0.1',
    'port': '5432'
}

# Логгирование базы данных
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Создаю таблицу с вакансиями
def create_table(conn):
    cursor = conn.cursor()

    create_table = """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            company VARCHAR(200),
            professional_role VARCHAR(200),
            salary VARCHAR(50),
            schedule VARCHAR(50),
            experience VARCHAR(50),
            employment VARCHAR(50),
            url VARCHAR(200)
        )
    """
    cursor.execute(create_table)

    conn.commit()
    cursor.close()
    logging.info("Таблица 'vacancies' успешно создана.")

# Функция для получения вакансий
def get_vacancies(page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'specialization': 1,
        'per_page': 100,
        'page': page
    }
    headers = {
        'Authorization': f'Bearer {hh_token}'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Функция для удаления дубликотов на основе столбца «url»
def remove_duplicates():
    with psycopg2.connect(**db_config) as conn:
        cursor = conn.cursor()

        # Удалить дубликаты на основе столбца «url»
        delete_duplicates_query = """
            DELETE FROM vacancies
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM vacancies
                GROUP BY url
            )
        """
        cursor.execute(delete_duplicates_query)

        conn.commit()
        cursor.close()

    logging.info("Дубликаты в таблице 'vacancies' успешно удалены.")


# Функция для парсинга вакансий
def parse_vacancies():

    with psycopg2.connect(**db_config) as conn:
        create_table(conn)
        page = 0
        while True:
            data = get_vacancies(page)

            if not data.get('items'):
                break

            with conn.cursor() as cursor:
                for item in data['items']:
                    city = item['address']['city']
                    company = item['employer']['name']
                    professional_role = item['professional_roles']['name']
                    schedule = item['schedule']['name']
                    experience = item['experience'].get('name', '')
                    employment = item['employment']['name']
                    url = item['alternate_url']
                    salary = item['salary']
                    if salary is None:
                        salary = "з/п не указана"
                    else:
                        salary = salary.get('from', '')

                    insert_query = """
                        INSERT INTO vacancies 
                        (city, company, professional_role, salary, schedule, experience, employment, url) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query,
                                (city, company, professional_role, salary, schedule, experience, employment, url))

                if page >= data['pages'] - 1:
                    break

                page += 1

                # Задержка между запросами в пределах 1-3 секунд
                time.sleep(random.uniform(3, 6))

    conn.commit()

    logging.info("Парсинг завершен. Данные сохранены в базе данных PostgreSQL.")


def run_parsing_job():
    logging.info("Запуск парсинга...")

    try:
        parse_vacancies()
        remove_duplicates()
    except Exception as e:
        logging.error(f"Ошибка при выполнении задачи парсинга: {e}")


