import fastapi
from statstudio.api import endpoints
import uvicorn

api = fastapi.FastAPI()

def configure():
    api.include_router(endpoints.router)

configure()


