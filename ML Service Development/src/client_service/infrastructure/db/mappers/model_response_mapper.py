from src.client_service.core.entities import ModelResponse
from src.client_service.infrastructure.db.entities import ModelResponseEntity
from src.client_service.infrastructure.db.mappers.interfaces import IMapper


class ModelResponseMapper(IMapper[ModelResponse, ModelResponseEntity]):
    @staticmethod
    def to_domain(entity: ModelResponseEntity) -> ModelResponse:
        return ModelResponse(
            id=int(entity.id),
            request_id=int(entity.request_id),
            label=bool(entity.label),
        )

    @staticmethod
    def to_entity(domain: ModelResponse) -> ModelResponseEntity:
        return ModelResponseEntity(
            id=domain.id,
            request_id=domain.request_id,
            label=domain.label,
        )
