import time
from app.core.celery_worker import celery_app


@celery_app.task(bind=True)
def process_document(self, file_path: str, doc_id: str):
    """
    문서를 파싱, 청킹, 임베딩하고 Vector Store에 저장하는 비동기 태스크입니다.
    """
    self.update_state(state='PROGRESS', meta={'status': '파싱 시작...'})
    print(f"'{doc_id}' 문서 파싱 시작. 경로: {file_path}")
    time.sleep(5)  # 실제 파싱 로직을 대체하는 더미 작업

    self.update_state(state='PROGRESS', meta={'status': '청킹 중...'})
    print(f"'{doc_id}' 문서 청킹 중...")
    time.sleep(5)  # 실제 청킹 로직을 대체하는 더미 작업

    self.update_state(state='PROGRESS', meta={'status': '임베딩 및 저장 중...'})
    print(f"'{doc_id}' 문서 임베딩 및 저장 중...")
    time.sleep(5)  # 실제 임베딩/저장 로직을 대체하는 더미 작업

    return {'status': '완료', 'doc_id': doc_id}
