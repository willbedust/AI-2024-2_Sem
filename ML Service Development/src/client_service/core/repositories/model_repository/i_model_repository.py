from abc import ABC, abstractmethod

from src.client_service.core.entities import ModelRequest, ModelResponse
from src.client_service.core.repositories.model_repository.dto import CreateRequestDTO, CreateResponseDTO


class IModelRepository(ABC):
    @staticmethod
    @abstractmethod
    async def create_request(request: CreateRequestDTO) -> ModelRequest:
        """Create a request entity"""

    @staticmethod
    @abstractmethod
    async def create_response(request: CreateResponseDTO) -> ModelResponse:
        """Create a response entity"""
