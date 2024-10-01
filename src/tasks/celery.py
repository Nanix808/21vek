import requests
from celery import Celery
from requests.exceptions import RequestException

from config import settings


celery = Celery(
    "celery",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)
celery.conf.broker_connection_retry_on_startup = True


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls my_function every 10 seconds.
    sender.add_periodic_task(10.0, send_requests.s(), name="add every 10")


@celery.task(autoretry_for=(RequestException,), retry_kwargs={"max_retries": 5})
def send_requests():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("arg", res.text)
