from src.client_service.core.entities import ModelRequest, ModelResponse
from src.client_service.core.repositories.model_repository import IModelRepository
from src.client_service.core.repositories.model_repository.dto import CreateRequestDTO, CreateResponseDTO
from src.client_service.infrastructure.db.entities import ModelRequestEntity, ModelResponseEntity
from src.client_service.infrastructure.db.mappers import ModelRequestMapper, ModelResponseMapper
from src.client_service.infrastructure.utils import async_session_maker


class ModelRepository(IModelRepository):
    @staticmethod
    async def create_request(request: CreateRequestDTO) -> ModelRequest:
        new_request = ModelRequestEntity(
            model_name=request.model_name,
            text=request.text,
        )

        async with async_session_maker() as session:
            session.add(new_request)

            await session.commit()
            await session.refresh(new_request)

        return ModelRequestMapper.to_domain(new_request)

    @staticmethod
    async def create_response(response: CreateResponseDTO) -> ModelResponse:
        new_response = ModelResponseEntity(
            request_id=response.request_id,
            label=response.label,
        )

        async with async_session_maker() as session:
            session.add(new_response)

            await session.commit()
            await session.refresh(new_response)

        return ModelResponseMapper.to_domain(new_response)
