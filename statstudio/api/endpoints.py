import pandas as pd
from fastapi import Body
from fastapi.responses import JSONResponse
from worker.celery_worker import create_task_count
from celery.result import AsyncResult
import fastapi
from statstudio.StatModels import CountDataPoisson

router = fastapi.APIRouter()

@router.post('/count_data/predict')
async def run_count(data=Body(...)):
    data_sales = data["Sales"]
    data_column = 'Sales'
    task = create_task_count.delay(data_sales, data_column)
    return {"task_id": str(task), "status": "Processing"}


@router.get('/count_data/result/{task_id}')
async def count_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'result': str(result)}

@router.post('/')
async def root(data=Body(...)):
    return {"message": "Working!"}