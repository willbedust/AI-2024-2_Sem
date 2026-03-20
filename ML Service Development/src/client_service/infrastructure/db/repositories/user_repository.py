from typing import Optional

from sqlalchemy.exc import NoResultFound
from sqlalchemy.future import select

from src.client_service.core.entities import User
from src.client_service.core.repositories import IUserRepository
from src.client_service.core.repositories.user_repository.dto import CreateUserDTO, PatchUserDTO, UpdateUserDTO
from src.client_service.infrastructure.db.entities.user_entity import UserEntity
from src.client_service.infrastructure.db.mappers.user_mapper import UserMapper
from src.client_service.infrastructure.utils import async_session_maker


class UserRepository(IUserRepository):
    @staticmethod
    async def create_user(user: CreateUserDTO) -> User:
        new_user = UserEntity(
            username=user.username,
            password=user.password,
            funds=0.0,
        )

        async with async_session_maker() as session:
            session.add(new_user)

            await session.commit()
            await session.refresh(new_user)

        return UserMapper.to_domain(new_user)

    @staticmethod
    async def get_user_by_id(user_id: int) -> Optional[User]:
        query = select(UserEntity).where(UserEntity.id == user_id)
        async with async_session_maker() as session:
            result = await session.execute(query)

        try:
            user = result.scalar_one()
            return UserMapper.to_domain(user)
        except NoResultFound:
            return None

    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        query = select(UserEntity).where(UserEntity.username == username)
        async with async_session_maker() as session:
            result = await session.execute(query)

        try:
            user = result.scalar_one()
            return UserMapper.to_domain(user)
        except NoResultFound:
            return None

    @staticmethod
    async def get_users(offset: int, limit: int) -> list[User]:
        query = select(UserEntity).offset(offset).limit(limit)

        async with async_session_maker() as session:
            result = await session.execute(query)

        users = result.scalars().all()

        return [UserMapper.to_domain(user) for user in users]

    @staticmethod
    async def update_user(user_id: int, update_dto: UpdateUserDTO) -> Optional[User]:
        query = select(UserEntity).where(UserEntity.id == user_id)
        async with async_session_maker() as session:
            result = await session.execute(query)

            try:
                user = result.scalar_one()
                user.password = update_dto.password  # type: ignore
                user.funds = update_dto.funds  # type: ignore

                await session.commit()
                await session.refresh(user)

                return UserMapper.to_domain(user)
            except NoResultFound:
                return None

    @staticmethod
    async def patch_user(user_id: int, patch_dto: PatchUserDTO) -> Optional[User]:
        query = select(UserEntity).where(UserEntity.id == user_id)
        async with async_session_maker() as session:
            result = await session.execute(query)

            try:
                user = result.scalar_one()

                if patch_dto.password is not None:
                    user.password = patch_dto.password  # type: ignore

                if patch_dto.funds is not None:
                    user.funds = patch_dto.funds  # type: ignore

                await session.commit()
                await session.refresh(user)

                return UserMapper.to_domain(user)
            except NoResultFound:
                return None

    @staticmethod
    async def delete_user(user_id: int) -> Optional[User]:
        query = select(UserEntity).where(UserEntity.id == user_id)
        async with async_session_maker() as session:
            result = await session.execute(query)

            try:
                user = result.scalar_one()

                await session.commit()
                await session.refresh(user)

                return UserMapper.to_domain(user)
            except NoResultFound:
                return None
