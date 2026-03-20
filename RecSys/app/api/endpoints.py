from fastapi import APIRouter, Depends
from starlette.responses import Response

from app.core.auth import verify_token
from app.schemas.api import HealthResponse
from app.schemas.api.reco_response import RecoResponse
from app.services.model_registry import model_registry

router = APIRouter()


@router.get(
    "/health",
    description="Проверка работоспособности сервиса",
    response_description="Стандартный ответ `ok`",
    response_model=HealthResponse,
    tags=["service"],
    status_code=200,
    responses={
        200: {
            "description": "Успешный ответ: сервис работает и возвращает статус 'ok'",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def health():
    return HealthResponse(status="ok")


@router.get(
    "/reco/{model_name}/{user_id}",
    description="Получение рекомендаций, требует bearer аутентификации",
    response_description="Список из 10 ответов типа Item, включающих информацию о фильме",
    response_model=RecoResponse,
    tags=["api"],
    status_code=200,
    responses={
        200: {
            "description": "Успешное получение рекомендаций для пользователя",
            "content": {"application/json": {"example": {"user_id": 973171, "items": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}}},
        },
        401: {"description": "Неавторизованный запрос: отсутствует или неверный токен"},
        404: {"description": "Модель не найдена"},
        500: {"description": "Внутренняя ошибка сервера"},
    },
)
async def get_recommendations(model_name: str, user_id: int, credentials=Depends(verify_token)):
    model = await model_registry.get(model_name)
    if model is None:
        return Response("Model not found", status_code=404)

    recommendations = await model.predict(user_id)
    return RecoResponse(user_id=user_id, items=recommendations)
