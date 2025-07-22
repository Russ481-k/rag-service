from pydantic import BaseModel, Field
from typing import List, Optional


class QueryRequest(BaseModel):
    query: str = Field(..., description="사용자의 질문")
    doc_id: Optional[str] = Field(
        None, description="특정 문서로 검색 범위를 한정할 경우의 문서 ID")
    template_id: Optional[str] = Field(None, description="사용할 출력 템플릿 ID")


class Source(BaseModel):
    doc_id: str = Field(..., description="출처 문서의 ID")
    file_name: str = Field(..., description="출처 문서의 파일 이름")
    page_number: int = Field(..., description="출처 페이지 번호")
    content: str = Field(..., description="답변의 근거가 된 원본 텍스트 일부")


class QueryResponse(BaseModel):
    answer: str = Field(..., description="LLM이 생성한 최종 답변")
    sources: List[Source] = Field(..., description="답변의 근거가 된 출처 목록")
    formatted_answer: Optional[str] = Field(
        None, description="템플릿이 적용된 최종 답변 문자열")
