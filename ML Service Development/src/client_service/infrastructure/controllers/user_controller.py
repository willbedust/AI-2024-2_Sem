from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException  # , Query
from starlette.responses import JSONResponse

from src.client_service.core.entities.user import User
from src.client_service.core.repositories.user_repository.dto import CreateUserDTO, PatchUserDTO, UpdateUserDTO
from src.client_service.core.services.user_service import UserService
from src.client_service.infrastructure.controllers.auth_controller import get_current_user
from src.client_service.infrastructure.controllers.dependencies import user_service

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post("")
async def add_user(
    user: CreateUserDTO,
    user_service: Annotated[UserService, Depends(user_service)],
):
    created_user = await user_service.create_user(user)
    return JSONResponse(content=created_user.model_dump(), status_code=201)


@router.get("")
async def get_user_by_id(
    user_service: Annotated[UserService, Depends(user_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        found_user = await user_service.get_user_by_id(current_user.id)
        return found_user.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.get("")
async def get_user_by_username(
    user_service: Annotated[UserService, Depends(user_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        found_user = await user_service.get_user_by_id(current_user.id)
        return found_user.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


# TODO: need it?
# @router.get("")
# async def get_users(
#     user_service: Annotated[UserService, Depends(user_service)],
#     current_user: str = Depends(get_current_user),
#     offset: int = Query(0, ge=0, description="Non-negative integer, offset for pagination."),
#     limit: int = Query(10, gt=0, description="Positive integer, maximum number of users to return."),
# ):
#     try:
#         users = await user_service.get_users(offset=offset, limit=limit)
#         return [user.model_dump() for user in users]
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e)) from e


@router.put("")
async def update_user(
    update_dto: UpdateUserDTO,
    user_service: Annotated[UserService, Depends(user_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        updated_user = await user_service.update_user(current_user.id, update_dto)
        return updated_user.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.patch("")
async def patch_user(
    patch_dto: PatchUserDTO,
    user_service: Annotated[UserService, Depends(user_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        patched_user = await user_service.patch_user(current_user.id, patch_dto)
        return patched_user.model_dump()
    except TypeError as e:
        raise HTTPException(status_code=304, detail=str(e)) from e
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.delete("")
async def delete_user(
    user_service: Annotated[UserService, Depends(user_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        deleted_user = await user_service.delete_user(current_user.id)
        return deleted_user.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
