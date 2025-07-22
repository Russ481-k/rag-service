# RAG 핵심 API 명세

문서 처리 및 질의응답과 관련된 핵심 API입니다.

---

### 1. 문서 업로드

- `POST /upload`
- **Description**: 파일을 업로드하여 비동기 처리 파이프라인을 시작합니다.
- **Request**:
  - `Content-Type: multipart/form-data`
  - `Body`: `file` (file, required)
- **Response `202 Accepted`**:
  ```json
  {
    "task_id": "c1a9a83a-4342-45c1-8f43-059a9a3b6522",
    "doc_id": "doc_a4d3e2b1-3e4c-4b5d-9a8f-2c1b3d4e5f6a",
    "message": "Document processing started."
  }
  ```

---

### 2. 문서 처리 상태 확인

- `GET /status/{task_id}`
- **Description**: `task_id`를 사용하여 작업의 현재 상태를 조회합니다.
- **Response `200 OK`**:
  ```json
  {
    "task_id": "c1a9a83a-4342-45c1-8f43-059a9a3b6522",
    "status": "completed"
  }
  ```

---

### 3. 질의응답

- `POST /query`
- **Description**: 시스템에 저장된 문서를 기반으로 질문에 대한 답변을 생성합니다. 지정된 템플릿에 따라 응답 형식이 달라집니다.
- **Request Body**:
  ```json
  {
    "query": "RIS 사업의 핵심 성공 요인은 무엇인가요?",
    "doc_id": "doc_a4d3e2b1-3e4c-4b5d-9a8f-2c1b3d4e5f6a",
    "template_id": "tmpl_a1b2c3d4"
  }
  ```
  - `query`: (string, **required**)
  - `doc_id`: (string, _optional_)
  - `template_id`: (string, _optional_) 응답 형식을 지정할 템플릿 ID. 미지정 시 기본 템플릿 사용.
- **Response `200 OK`**:
  ```json
  {
    "answer": "RIS 사업의 핵심 성공 요인은 지역 대학과 산업체의 긴밀한 협력, 그리고 지속적인 정부 지원입니다.",
    "sources": [
      {
        "doc_id": "doc_a4d3e2b1-3e4c-4b5d-9a8f-2c1b3d4e5f6a",
        "file_name": "RIS_strategy_A.pdf",
        "page_number": 5,
        "content": "핵심 성공 요인으로는 지역 대학과 산업체의 긴밀한 협력, 그리고 지속적인 정부 지원을 들 수 있다..."
      }
    ],
    "formatted_answer": "**요약 답변:**\nRIS 사업의 핵심 성공 요인은 지역 대학과 산업체의 긴밀한 협력, 그리고 지속적인 정부 지원입니다.\n\n**주요 근거:**\n- 문서: RIS_strategy_A.pdf (Page: 5)"
  }
  ```
