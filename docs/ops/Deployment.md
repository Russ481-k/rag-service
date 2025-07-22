# 배포 안내서 (Deployment Guide)

본 문서는 개발이 완료된 RAG 서비스를 실제 운영 환경에 배포하는 절차를 안내합니다.

## 1. 인프라 요구사항

- **Compute**: 2 vCPU, 4GB RAM 이상의 사양을 가진 가상 머신 (e.g., AWS EC2, GCP Compute Engine)
- **OS**: Ubuntu 22.04 LTS
- **Database**: [Supabase](https://supabase.com/) 프로젝트
- **Message Broker & Result Backend**: [Redis](https://redis.io/) 인스턴스 (e.g., AWS ElastiCache, 직접 설치)
- **Domain**: 서비스에 연결할 도메인 주소 (선택 사항)

## 2. 배포 시나리오: Docker Compose

초기 배포는 Docker Compose를 사용하여 FastAPI 애플리케이션, Celery Worker, Redis를 단일 서버 내에서 컨테이너로 실행하는 방식을 권장합니다. 이는 설정이 비교적 간단하고 관리가 용이합니다.

### `docker-compose.yml` 예시

```yaml
version: "3.8"

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  api:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    volumes:
      - ./app:/app
    ports:
      - "8000:8000"
    depends_on:
      - redis
    env_file:
      - .env.prod

  worker:
    build: .
    command: celery -A app.core.celery_worker.celery_app worker --loglevel=info
    volumes:
      - ./app:/app
    depends_on:
      - redis
    env_file:
      - .env.prod
# volumes:
#   redis_data:
```

## 3. 단계별 배포 가이드

1.  **서버 준비**: 클라우드 제공업체를 통해 요구사항에 맞는 가상 머신을 생성하고 Docker와 Docker Compose를 설치합니다.

2.  **소스 코드 클론**:

    ```bash
    git clone <your-repository-url>
    cd rag-service
    ```

3.  **프로덕션 환경 변수 설정**:

    - `.env.prod` 파일을 생성하고 Supabase, Gemini API 키 등 프로덕션 환경에 맞는 설정 값을 입력합니다.

4.  **Docker 이미지 빌드 및 실행**:

    ```bash
    docker-compose up --build -d
    ```

5.  **(선택) Nginx 리버스 프록시 설정**:
    - 도메인 연결 및 HTTPS 설정을 위해 Nginx를 설치하고, 80/443 포트로 들어오는 요청을 `localhost:8000`으로 전달하도록 설정합니다.

## 4. CI/CD 파이프라인 (미래)

향후 GitHub Actions를 사용하여 `main` 브랜치에 코드가 푸시될 때마다 자동으로 테스트, Docker 이미지 빌드, 및 서버 배포가 이루어지도록 파이프라인을 구성할 수 있습니다.
