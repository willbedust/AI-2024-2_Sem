from src.client_service.core.services import UserService
from src.client_service.core.services.model_service import ModelService
from src.client_service.infrastructure.db.repositories import ModelRepository, UserRepository
from src.client_service.infrastructure.message_brokers import RabbitmqBroker


def user_service():
    return UserService(UserRepository)  # type: ignore


def model_service():
    return ModelService(RabbitmqBroker, UserRepository, ModelRepository)  # type: ignore
