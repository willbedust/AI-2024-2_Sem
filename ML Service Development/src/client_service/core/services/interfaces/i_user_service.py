from abc import ABC, abstractmethod

from src.client_service.core.entities import User
from src.client_service.core.repositories.user_repository.dto import CreateUserDTO, PatchUserDTO, UpdateUserDTO


class IUserService(ABC):
    @abstractmethod
    async def create_user(self, user_dto: CreateUserDTO) -> User:
        """
        Creates a new user in the system
        :param user_dto: information about the user to be created
        :return: created user
        """

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User:
        """
        Returns an user by its id
        :param user_id: id of the user to be returned, positive integer
        :return: found user
        """

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User:
        """
        Returns an user by its name
        :param username: name of the user to be returned, string
        :return: found user
        """

    @abstractmethod
    async def get_users(self, offset: int = 0, limit: int = 10) -> list[User]:
        """
        Returns a list of users with filtering and pagination
        :param offset: _description_, defaults to 0
        :param limit: _description_, defaults to 10
        :return: list of users with filtering and pagination
        """

    @abstractmethod
    async def update_user(self, user_id: int, update_dto: UpdateUserDTO) -> User:
        """
        Updates an existing user in the system
        :param user_id: id of the user to be updated, positive integer
        :param update_dto: information about the user to be updated
        :return: updated user
        """

    @abstractmethod
    async def patch_user(self, user_id: int, patch_dto: PatchUserDTO) -> User:
        """
        Updates an existing user in the system partially
        :param user_id: id of the user to be updated, positive integer
        :param patch_dto: information about the user to be updated
        :return: updated user
        """

    @abstractmethod
    async def delete_user(self, user_id: int) -> User:
        """
        Deletes an existing user in the system
        :param user_id: id of the user to be deleted, positive integer
        :return: deleted user
        """
