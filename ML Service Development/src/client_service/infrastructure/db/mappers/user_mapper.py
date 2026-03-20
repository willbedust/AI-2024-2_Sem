from src.client_service.core.entities import User
from src.client_service.infrastructure.db.entities import UserEntity
from src.client_service.infrastructure.db.mappers.interfaces import IMapper


class UserMapper(IMapper[User, UserEntity]):
    @staticmethod
    def to_domain(entity: UserEntity) -> User:
        return User(
            id=int(entity.id),
            username=str(entity.username),
            password=str(entity.password),
            funds=float(entity.funds),
        )

    @staticmethod
    def to_entity(domain: User) -> UserEntity:
        return UserEntity(
            id=domain.id,
            username=domain.username,
            password=domain.password,
            funds=domain.funds,
        )
