import json
from pathlib import Path
from typing import Dict

from src.client_service.core.message_brokers.i_message_broker import IMessageBroker
from src.client_service.core.repositories import IUserRepository
from src.client_service.core.repositories.model_repository import IModelRepository
from src.client_service.core.repositories.model_repository.dto import CreateRequestDTO
from src.client_service.core.repositories.model_repository.dto.create_response_dto import CreateResponseDTO
from src.client_service.core.repositories.user_repository.dto import PatchUserDTO
from src.client_service.core.services.interfaces import IModelService


class ModelService(IModelService):
    MODELS_CONFIG_PATH = Path(__file__).parents[4] / "configs/models.json"

    def __init__(
        self,
        message_broker: IMessageBroker,
        user_repository: IUserRepository,
        model_repository: IModelRepository,
    ):
        self._user_repository = user_repository
        self._model_repository = model_repository
        self._message_broker = message_broker

        with open(self.MODELS_CONFIG_PATH, encoding="utf-8") as f:
            self._models_registry: Dict[str, float] = json.load(f)

    async def predict(self, text: str, model_name: str, current_user_id: int) -> bool:
        if self._models_registry.get(model_name) is None:
            raise ValueError(f"Model {model_name} not found.")

        model_request_cost: float = self._models_registry[model_name]
        user = await self._user_repository.get_user_by_id(current_user_id)
        if user is None:
            raise ValueError("User not found.")

        if user.funds < model_request_cost:
            raise ValueError("Not enough funds.")

        user_balance_start = user.funds
        user_balance_target = user_balance_start - model_request_cost
        await self._user_repository.patch_user(current_user_id, PatchUserDTO(password=None, funds=user_balance_target))

        request = await self._model_repository.create_request(CreateRequestDTO(model_name=model_name, text=text))
        try:
            response = await self._message_broker.predict(text, model_name)
        except Exception:
            response = None

        if response is not None:
            await self._model_repository.create_response(CreateResponseDTO(request_id=request.id, label=response))
            return response

        await self._user_repository.patch_user(current_user_id, PatchUserDTO(password=None, funds=user_balance_start))
        raise ValueError("Error while predict.")
