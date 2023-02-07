from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION_ROOT: str = "/api/v1"
    MICROSERVICE_PORT: int = 8000


settings = Settings()
