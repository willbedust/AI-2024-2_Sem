from sqlalchemy import Column, Float, Integer, String

from src.client_service.infrastructure.utils import Base


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    funds = Column(Float, nullable=False)
