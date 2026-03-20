import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.responses import JSONResponse

from src.client_service.core.entities.user import User
from src.client_service.core.repositories.user_repository.dto.create_user_dto import CreateUserDTO
from src.client_service.core.services.user_service import UserService
from src.client_service.infrastructure.controllers.dependencies import user_service
from src.client_service.infrastructure.utils import tokens

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register")
async def register(user: CreateUserDTO, user_service: Annotated[UserService, Depends(user_service)]):
    try:
        await user_service.get_user_by_username(user.username)
    except Exception:
        await user_service.create_user(user)
        return JSONResponse({"message": "User registered successfully!"})

    raise HTTPException(status_code=400, detail="User already exists")


@router.post("/login")
async def login(user: CreateUserDTO, user_service: Annotated[UserService, Depends(user_service)]):
    try:
        found_user = await user_service.get_user_by_username(user.username)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if found_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = str(uuid.uuid4())
    tokens[token] = found_user
    return JSONResponse({"token": token})


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> User:
    token = credentials.credentials
    if token not in tokens:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    current_user: User = tokens[token]
    return current_user
