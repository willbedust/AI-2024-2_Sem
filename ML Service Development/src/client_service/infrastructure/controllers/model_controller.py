from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from src.client_service.core.entities.user import User
from src.client_service.core.services.model_service import ModelService
from src.client_service.infrastructure.controllers.auth_controller import get_current_user
from src.client_service.infrastructure.controllers.dependencies import model_service

router = APIRouter(
    prefix="/model",
    tags=["Model"],
)


@router.post("/predict")
async def predict(
    text: str,
    model_name: str,
    model_service: Annotated[ModelService, Depends(model_service)],
    current_user: User = Depends(get_current_user),
):
    try:
        label = await model_service.predict(text, model_name, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while prediction: {e}.")

    return JSONResponse({"label": label})
