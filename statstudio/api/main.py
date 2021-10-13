import fastapi
from statstudio.api import endpoints
import uvicorn

api = fastapi.FastAPI()

def configure():
    api.include_router(endpoints.router)

configure()

if __name__ == '__main__':
    uvicorn.run(api, host = '0.0.0.0')

