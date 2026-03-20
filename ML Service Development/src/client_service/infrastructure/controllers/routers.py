from .auth_controller import router as auth_router
from .model_controller import router as model_router
from .user_controller import router as user_router

all_routers = [user_router, auth_router, model_router]
