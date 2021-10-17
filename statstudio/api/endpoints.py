import pandas as pd
from fastapi import Body
from fastapi.responses import JSONResponse
from worker.celery_worker import create_task, create_task_count
from celery.result import AsyncResult
import fastapi
from statstudio.StatModels import CountDataPoisson

router = fastapi.APIRouter()

@router.post('/test_task')
async def run_task(data=Body(...)):
    delay = int(data["delay"])
    x = data["x"]
    y = data["y"]
    task = create_task.delay(delay, x, y)
    return {"task_id": str(task), "status": "Processing"}

@router.get('/test_task/result/{task_id}')
async def task_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'result': str(result)}

@router.post('/count_data/predict')
async def run_count(data=Body(...)):
    data_sales = data["Sales"]
    data_column = 'Sales'
    print(type(data_sales))
    task = create_task_count.delay(data_sales, data_column)
    return {"task_id": str(task), "status": "Processing"}


@router.get('/count_data/result/{task_id}')
async def count_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'result': str(result)}

@router.get('/')
async def root():
    return {"message": "Working with change!"}

@router.get('/api/csv', status_code=fastapi.status.HTTP_200_OK)
def get_csv():
    pass