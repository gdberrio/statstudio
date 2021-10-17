import os
import time

from celery import Celery
from dotenv import load_dotenv

from statstudio.StatModels.CountDataPoisson import CountModel

load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@celery.task(name="test_task")
def create_task(a, b, c):
    time.sleep(a)
    return b + c

@celery.task(name="count_data")
def create_task_count(data, data_column):
    tau_mean = CountModel(data=data, data_column=data_column)
    return tau_mean

