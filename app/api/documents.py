import shutil
import uuid
from pathlib import Path
from typing import List

from fastapi import APIRouter, UploadFile, File, HTTPException, status, BackgroundTasks

from app.core.tasks import process_document
from app.schemas.document import Document, DocumentDetail
from app.schemas.task import UploadTask, DeleteTask, TaskStatus
from app.core.celery_worker import celery_app

router = APIRouter()

# 임시 업로드 디렉토리 설정
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload", response_model=UploadTask, status_code=status.HTTP_202_ACCEPTED)
async def upload_document(file: UploadFile = File(...)):
    """
    문서를 업로드하여 처리 파이프라인을 시작합니다.

    - **file**: 업로드할 문서 파일 (PDF, DOCX 등)
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename not found.")

    try:
        # 고유한 파일명 생성 (중복 방지)
        file_extension = Path(file.filename).suffix
        doc_id = str(uuid.uuid4())
        unique_filename = f"{doc_id}{file_extension}"
        file_path = UPLOAD_DIR / unique_filename

        # 파일 저장
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Celery 작업 호출
        task = process_document.delay(str(file_path), doc_id)

        return UploadTask(task_id=task.id, doc_id=doc_id)

    except Exception as e:
        # 파일 저장이나 태스크 호출 중 에러 발생 시 처리
        raise HTTPException(
            status_code=500, detail=f"File processing error: {e}")
    finally:
        file.file.close()


@router.get("/status/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str):
    """
    문서 처리 또는 삭제 작업의 상태를 확인합니다.
    """
    task_result = celery_app.AsyncResult(task_id)

    response = {"task_id": task_id, "status": task_result.status}
    if task_result.successful():
        response["result"] = task_result.get()
    elif task_result.failed():
        response["result"] = str(task_result.info)  # 에러 정보
    else:  # PENDING, PROGRESS
        response["result"] = task_result.info  # 진행 상태 정보

    return response


@router.get("/documents", response_model=List[Document])
async def get_all_documents():
    """
    업로드된 모든 문서의 목록을 조회합니다.
    """
    # TODO: 데이터베이스에서 문서 목록 조회 로직 구현
    return []


@router.get("/documents/{doc_id}", response_model=DocumentDetail)
async def get_document_details(doc_id: str):
    """
    특정 문서의 상세 정보를 조회합니다.
    """
    # TODO: 데이터베이스에서 특정 문서 정보 조회 로직 구현
    return None


@router.delete("/documents/{doc_id}", response_model=DeleteTask, status_code=status.HTTP_202_ACCEPTED)
async def delete_document(doc_id: str):
    """
    특정 문서를 시스템에서 삭제합니다.
    """
    # TODO: 문서 삭제 비동기 작업 호출 로직 구현
    return DeleteTask(task_id="dummy_delete_task_id")
