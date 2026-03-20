import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import router
from app.core.middleware import ExceptionMiddleware

app = FastAPI(
    title="Recommendation Service",
    description="Сервис рекомендаций с поддержкой Bearer-аутентификации и регистрацией моделей",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(router)
app.add_middleware(CORSMiddleware, allow_origins=["*"])
app.add_middleware(ExceptionMiddleware)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
