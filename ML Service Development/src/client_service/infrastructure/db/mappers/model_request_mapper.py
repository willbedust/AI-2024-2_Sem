from src.client_service.core.entities import ModelRequest
from src.client_service.infrastructure.db.entities import ModelRequestEntity
from src.client_service.infrastructure.db.mappers.interfaces import IMapper


class ModelRequestMapper(IMapper[ModelRequest, ModelRequestEntity]):
    @staticmethod
    def to_domain(entity: ModelRequestEntity) -> ModelRequest:
        return ModelRequest(
            id=int(entity.id),
            model_name=str(entity.model_name),
            text=str(entity.text),
        )

    @staticmethod
    def to_entity(domain: ModelRequest) -> ModelRequestEntity:
        return ModelRequestEntity(
            id=domain.id,
            model_name=domain.model_name,
            text=domain.text,
        )
