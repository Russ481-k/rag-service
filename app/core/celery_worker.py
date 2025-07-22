from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "rag_service_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_track_started=True,
)
