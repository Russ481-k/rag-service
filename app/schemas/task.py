from pydantic import BaseModel
from typing import Optional, Any


class UploadTask(BaseModel):
    task_id: str
    doc_id: str


class DeleteTask(BaseModel):
    task_id: str


class TaskStatus(BaseModel):
    task_id: str
    status: str
    result: Optional[Any] = None
