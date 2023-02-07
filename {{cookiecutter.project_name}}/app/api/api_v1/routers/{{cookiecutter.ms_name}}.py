from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_microservice_name():
    return {"microservice": "{{cookiecutter.ms_name}}"}
