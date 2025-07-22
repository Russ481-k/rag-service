# 문서 관리 API 명세

업로드된 문서를 조회, 상세 확인, 삭제하는 등 관리 기능과 관련된 API입니다.

---

### 1. 전체 문서 목록 조회

- `GET /documents`
- **Description**: 시스템에 업로드된 모든 문서의 메타데이터 목록을 조회합니다.
- **Responses**:
  - **`200 OK`**: 조회 성공
    ```json
    [
      {
        "doc_id": "doc_a4d3e2b1-3e4c-4b5d-9a8f-2c1b3d4e5f6a",
        "file_name": "RIS_strategy_A.pdf",
        "status": "completed",
        "created_at": "2023-10-27T10:00:00Z"
      }
    ]
    ```

---

### 2. 특정 문서 상세 정보 조회

- `GET /documents/{doc_id}`
- **Description**: `doc_id`에 해당하는 특정 문서의 상세 정보를 조회합니다.
- **Responses**:
  - **`200 OK`**: 조회 성공
    ```json
    {
      "doc_id": "doc_a4d3e2b1-3e4c-4b5d-9a8f-2c1b3d4e5f6a",
      "file_name": "RIS_strategy_A.pdf",
      "status": "completed",
      "created_at": "2023-10-27T10:00:00Z"
    }
    ```
  - **`404 Not Found`**: 문서를 찾을 수 없을 때

---

### 3. 특정 문서 삭제

- `DELETE /documents/{doc_id}`
- **Description**: `doc_id`에 해당하는 문서를 시스템에서 삭제합니다.
- **Responses**:
  - **`202 Accepted`**: 삭제 요청이 성공적으로 접수되었을 때
    ```json
    {
      "task_id": "d4b8e7f6-a54c-3d2b-1a9f-8e7d6c5b4a3e",
      "message": "Document deletion has been initiated."
    }
    ```
  - **`404 Not Found`**: 문서를 찾을 수 없을 때
