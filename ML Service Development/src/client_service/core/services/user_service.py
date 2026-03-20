from src.client_service.core.entities import User
from src.client_service.core.repositories import IUserRepository
from src.client_service.core.repositories.user_repository.dto import CreateUserDTO, PatchUserDTO, UpdateUserDTO
from src.client_service.core.services.interfaces import IUserService


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    async def create_user(self, user_dto: CreateUserDTO) -> User:
        return await self._user_repository.create_user(user_dto)

    async def get_user_by_id(self, user_id: int) -> User:
        found_user = await self._user_repository.get_user_by_id(user_id)
        if found_user is None:
            raise ValueError(f"User with ID {user_id} not found.")

        return found_user

    async def get_user_by_username(self, username: str) -> User:
        found_user = await self._user_repository.get_user_by_username(username)
        if found_user is None:
            raise ValueError(f"User with name {username} not found.")

        return found_user

    async def get_users(self, offset: int = 0, limit: int = 10) -> list[User]:
        if offset < 0:
            raise ValueError("Offset must be a non-negative integer.")

        if limit <= 0:
            raise ValueError("Limit must be a positive integer.")

        return await self._user_repository.get_users(offset, limit)

    async def update_user(self, user_id: int, update_dto: UpdateUserDTO) -> User:
        updated_user = await self._user_repository.update_user(user_id, update_dto)
        if updated_user is None:
            raise ValueError(f"User with ID {user_id} not found.")

        return updated_user

    async def patch_user(self, user_id: int, patch_dto: PatchUserDTO) -> User:
        existing_user = await self._user_repository.get_user_by_id(user_id)
        if existing_user is None:
            raise ValueError(f"User with ID {user_id} not found.")

        patched_user = await self._user_repository.patch_user(user_id, patch_dto)
        if patched_user is None:
            raise ValueError(f"User with ID {user_id} not found.")

        return patched_user

    async def delete_user(self, user_id: int) -> User:
        deleted_user = await self._user_repository.delete_user(user_id)
        if deleted_user is None:
            raise ValueError(f"User with ID {user_id} not found.")

        return deleted_user
