import uvicorn

from app.main import create_app
from app.core.config import settings

app = create_app()

if __name__ == "__main__":
    uvicorn.run("run:app", host="localhost", port=settings.MICROSERVICE_PORT, reload=True)
