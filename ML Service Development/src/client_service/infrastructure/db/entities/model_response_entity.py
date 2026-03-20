from sqlalchemy import Boolean, Column, Integer

from src.client_service.infrastructure.utils import Base


class ModelResponseEntity(Base):
    __tablename__ = "model_response"

    id = Column(Integer, primary_key=True, autoincrement=True)
    request_id = Column(Integer, nullable=False)
    label = Column(Boolean, nullable=False)
