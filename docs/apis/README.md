# RAG 서비스 API 명세서

본 문서는 RAG 서비스의 REST API를 사용하는 방법에 대해 기술합니다.

## 기본 정보

- **Base URL**: `http://localhost:8000`
- **응답 형식**: 모든 응답은 JSON 형식을 따릅니다.

## 인증

현재 API는 인증을 요구하지 않으나, 향후 `API-KEY` 헤더를 통한 인증 방식이 도입될 예정입니다.

```http
Authorization: Bearer <YOUR_API_KEY>
```

## API 문서 목록

- **[RAG 핵심 API](./rag.md)**: 문서 처리 및 질의응답과 관련된 핵심 API 명세입니다.
- **[문서 관리 API](./documents.md)**: 업로드된 문서를 관리(조회, 삭제)하기 위한 API 명세입니다.
- **[출력 템플릿 관리 API](./templates.md)**: 답변 서식을 지정하는 템플릿을 관리하기 위한 API 명세입니다.
