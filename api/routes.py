from .Formulario.controller import router as formulario_routes
from .Auth.controller import routes as auth_routes
from .User.controller import routes as user_routes
from fastapi import APIRouter

routes = APIRouter(prefix="/api/v1")

routes.include_router(formulario_routes)
routes.include_router(auth_routes)
routes.include_router(user_routes)
