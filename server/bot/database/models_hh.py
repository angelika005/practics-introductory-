from sqlalchemy import Column, Integer, String, Text
from vacancy_db import Base_hh

class Vacancy(Base_hh):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hh_id = Column(String, unique=True, nullable=False)
    area = Column(String)
    company = Column(String)
    prof_role = Column(String)
    salary = Column(String)
    schedule = Column(String)
    experience = Column(String)
    employment = Column(String)
    url = Column(String, nullable=False)
