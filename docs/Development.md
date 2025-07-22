# 개발 환경 설정

## 1. 사전 요구사항

- Python 3.13.3
- Poetry (의존성 관리 도구)
- Git

## 2. 설치 및 실행

1.  **저장소 클론**

    ```bash
    git clone <repository_url>
    cd rag-service
    ```

2.  **의존성 설치**

    ```bash
    poetry install
    ```

3.  **환경 변수 설정**

    - `.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.

    ```bash
    cp .env.example .env
    ```

    - `.env` 파일 내에 필요한 API 키 및 설정 값을 입력합니다.

    ```env
    # .env
    # Google AI Studio 또는 Google Cloud AI Platform에서 발급
    JEMINI_API_KEY="your-gemini-api-key"

    # Supabase 프로젝트 URL 및 anon key
    SUPABASE_URL="your-supabase-url"
    SUPABASE_ANON_KEY="your-supabase-anon-key"

    # Celery와 Redis 설정
    CELERY_BROKER_URL="redis://localhost:6379/0"
    CELERY_RESULT_BACKEND="redis://localhost:6379/0"
    ```

4.  **개발 서버 실행**
    ```bash
    poetry run uvicorn app.main:app --reload
    ```
    이제 브라우저에서 `http://localhost:8000/docs` 로 접속하여 자동 생성된 Swagger UI를 확인할 수 있습니다.

## 3. 로컬 의존성 실행 (Docker)

개발에 필요한 Redis와 같은 외부 서비스를 로컬 환경에서 간편하게 실행하기 위해 Docker Compose를 사용합니다.

1.  **Docker 설치**: 시스템에 Docker와 Docker Compose를 설치합니다.

2.  **의존성 실행**: 프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다.
    ```bash
    docker-compose up -d
    ```
    이 명령어는 `docker-compose.yml` 파일에 정의된 `redis` 서비스를 백그라운드에서 실행합니다.

## 4. 테스트 실행

```bash
poetry run pytest
```
