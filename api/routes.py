from .Formulario.controller import router as formulario_routes
from fastapi import APIRouter

routes = APIRouter(prefix="/api/v1")

routes.include_router(formulario_routes)
