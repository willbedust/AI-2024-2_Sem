from sqlalchemy import Column, Integer, String

from src.client_service.infrastructure.utils import Base


class ModelRequestEntity(Base):
    __tablename__ = "model_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String, nullable=False)
    text = Column(String, nullable=False)
