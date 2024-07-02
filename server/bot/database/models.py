from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
class Base(DeclarativeBase):
    ...

class Product(Base):
    __tablename__ = 'param'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(String(50))
    prof_role: Mapped[str] = mapped_column(String(50))
    salary: Mapped[str] = mapped_column(String(50))
    schedule: Mapped[str] = mapped_column(String(50))
    experience: Mapped[str] = mapped_column(String(50))
    employment: Mapped[str] = mapped_column(String(50))
