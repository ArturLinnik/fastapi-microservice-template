from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api.api_v1.api import api_router


def include_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_routes(app):
    app.include_router(api_router, prefix=settings.API_VERSION_ROOT)


def create_app():
    app = FastAPI()

    include_middleware(app)
    register_routes(app)

    return app
