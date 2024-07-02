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


from sqlalchemy import create_engine, Integer, String, Column, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime
import uuid

# Параметры подключения к PostgreSQL
DB_HOST = "127.0.0.1"  # Или IP-адрес Docker контейнера
DB_PORT = "5432"
DB_NAME = "vacancies"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


class Search(Base):
    tablename = 'search'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_title = Column(String(255), nullable=False)
    experience = Column(String(255), nullable=False)
    employment = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    vacancies = relationship('Vacancy', back_populates='search')


class Vacancy(Base):
    tablename = 'vacancy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    salary = Column(String(255), nullable=False)
    offer_link = Column(Text, nullable=False)
    search_id = Column(Integer, ForeignKey('search.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    search = relationship('Search', back_populates='vacancies')


# Пример использования существующей базы данных

# Добавление новой записи
new_search = Search(
    job_title="Software Engineer",
    experience="3-5 years",
    employment="Full-time",
    city="San Francisco"
)

session.add(new_search)
session.commit()

new_vacancy = Vacancy(
    title="Backend Developer",
    company_name="Tech Corp",
    salary="120000",
    offer_link="http://example.com/job/backend-developer",
    search_id=new_search.id,
    created_at=datetime.utcnow()
)

session.add(new_vacancy)
session.commit()

# Получение записей
searches = session.query(Search).all()
for search in searches:
    print(f"Search ID: {search.id}, Job Title: {search.job_title}")

vacancies = session.query(Vacancy).all()
for vacancy in vacancies:
    print(f"Vacancy Title: {vacancy.title}, Company: {vacancy.company_name}")

