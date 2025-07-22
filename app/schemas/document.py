from pydantic import BaseModel, Field
from datetime import datetime


class Document(BaseModel):
    doc_id: str = Field(..., description="고유 문서 ID")
    file_name: str = Field(..., description="원본 파일 이름")
    status: str = Field(...,
                        description="처리 상태 (e.g., completed, processing, failed)")
    created_at: datetime = Field(..., description="생성 일시")

    class Config:
        from_attributes = True


class DocumentDetail(Document):
    metadata: dict | None = Field(
        None, description="추가 메타데이터 (e.g., file_size, page_count)")
