# 출력 템플릿 관리 API 명세

생성된 답변을 특정 서식으로 포맷팅하기 위한 템플릿을 관리하는 API입니다.

---

### 1. 템플릿 생성

- `POST /templates`
- **Description**: 새로운 출력 템플릿을 생성합니다. 템플릿 본문에는 `{{ answer }}`와 `sources` 객체 배열을 활용한 반복문 등을 사용할 수 있습니다 (Jinja2와 유사).
- **Request Body**:
  ```json
  {
    "name": "기본 요약형",
    "description": "답변과 출처를 간결하게 요약하여 보여주는 템플릿입니다.",
    "template_body": "**요약 답변:**\n{{ answer }}\n\n**주요 근거:**\n{% for source in sources %}\n- 문서: {{ source.file_name }} (Page: {{ source.page_number }})\n{% endfor %}"
  }
  ```
- **Responses**:
  - **`201 Created`**: 템플릿 생성 성공
    ```json
    {
      "template_id": "tmpl_a1b2c3d4",
      "name": "기본 요약형",
      "description": "답변과 출처를 간결하게 요약하여 보여주는 템플릿입니다.",
      "created_at": "2023-10-28T11:00:00Z"
    }
    ```

### 2. 템플릿 목록 조회

- `GET /templates`
- **Description**: 사용 가능한 모든 출력 템플릿의 목록을 조회합니다.
- **Responses**:
  - **`200 OK`**: 조회 성공
    ```json
    [
      {
        "template_id": "tmpl_a1b2c3d4",
        "name": "기본 요약형",
        "description": "답변과 출처를 간결하게 요약하여 보여주는 템플릿입니다."
      }
    ]
    ```

### 3. 특정 템플릿 상세 조회

- `GET /templates/{template_id}`
- **Description**: `template_id`에 해당하는 특정 템플릿의 상세 정보를 조회합니다.
- **Responses**:
  - **`200 OK`**: 조회 성공
    ```json
    {
      "template_id": "tmpl_a1b2c3d4",
      "name": "기본 요약형",
      "description": "답변과 출처를 간결하게 요약하여 보여주는 템플릿입니다.",
      "template_body": "**요약 답변:**\n{{ answer }}\n\n**주요 근거:**\n{% for source in sources %}\n- 문서: {{ source.file_name }} (Page: {{ source.page_number }})\n{% endfor %}",
      "created_at": "2023-10-28T11:00:00Z",
      "updated_at": "2023-10-28T11:00:00Z"
    }
    ```
  - **`404 Not Found`**: 템플릿을 찾을 수 없을 때

### 4. 템플릿 삭제

- `DELETE /templates/{template_id}`
- **Description**: `template_id`에 해당하는 템플릿을 삭제합니다.
- **Responses**:
  - **`204 No Content`**: 삭제 성공
  - **`404 Not Found`**: 템플릿을 찾을 수 없을 때
