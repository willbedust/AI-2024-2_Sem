from abc import ABC, abstractmethod
from typing import List, Optional

from src.client_service.core.entities import User
from src.client_service.core.repositories.user_repository.dto import CreateUserDTO, PatchUserDTO, UpdateUserDTO


class IUserRepository(ABC):
    @staticmethod
    @abstractmethod
    async def create_user(user: CreateUserDTO) -> User:
        """Create a new user"""

    @staticmethod
    @abstractmethod
    async def get_user_by_id(user_id: int) -> Optional[User]:
        """Retrieve an user by its ID"""

    @staticmethod
    @abstractmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        """Retrieve an user by its name"""

    @staticmethod
    @abstractmethod
    async def get_users(offset: int, limit: int) -> List[User]:
        """Retrieve a list of users, with optional filters and pagination"""

    @staticmethod
    @abstractmethod
    async def update_user(user_id: int, user: UpdateUserDTO) -> Optional[User]:
        """Replace an user with new data"""

    @staticmethod
    @abstractmethod
    async def patch_user(user_id: int, user: PatchUserDTO) -> Optional[User]:
        """Partially update an user"""

    @staticmethod
    @abstractmethod
    async def delete_user(user_id: int) -> Optional[User]:
        """Delete user from storage"""
