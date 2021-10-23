import fastapi
from statstudio.api import endpoints
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

api = fastapi.FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def configure():
    api.include_router(endpoints.router)

configure()


