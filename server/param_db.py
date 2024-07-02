from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Параметры подключения к базе данных
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "params"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание объекта Engine
engine = create_engine(DATABASE_URL)

# Создание базового класса модели
Base = declarative_base()

# Определение модели
class Params(Base):
    tablename = 'params'
    area = Column(String(100), nullable=False)
    professional_role = Column(String(200), nullable=False)
    salary = Column(String(50), nullable=False)
    schedule = Column(String(50), nullable=False)
    experience = Column(String(50), nullable=False)
    employment = Column(String(50), nullable=False)


# Создание объекта Session
Session = sessionmaker(bind=engine)
session = Session()
