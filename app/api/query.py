from fastapi import APIRouter

from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    """
    문서 내용에 대해 질의하고 답변을 생성합니다.
    """
    # TODO: RAG 서비스 로직 호출 구현
    return QueryResponse(
        answer="This is a dummy answer.",
        sources=[]
    )
