import fastapi
from statstudio.StatModels import CountDataPoisson

router = fastapi.APIRouter()

@router.get('/')
async def root():
    return {"message": "Working!"}

@router.get('/api/csv', status_code=fastapi.status.HTTP_200_OK)
def get_csv():
    pass