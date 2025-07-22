from fastapi import FastAPI

from app.api import documents, query

app = FastAPI(
    title="고도화 RAG 서비스",
    description="문서(PDF) 기반의 질의응답을 제공하는 고도화된 RAG 서비스 API",
    version="0.1.0",
)

app.include_router(documents.router, tags=["Documents"])
app.include_router(query.router, tags=["Query"])


@app.get("/")
def read_root():
    """서비스의 상태를 확인하는 기본 엔드포인트입니다."""
    return {"status": "ok"}
