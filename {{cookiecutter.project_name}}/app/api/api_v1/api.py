from fastapi import APIRouter

from ..api_v1.routers import (
    {{cookiecutter.ms_name}}
)

api_router = APIRouter()

api_router.include_router({{cookiecutter.ms_name}}.router, prefix="/{{cookiecutter.ms_name}}", tags=["{{cookiecutter.ms_name}}"])
