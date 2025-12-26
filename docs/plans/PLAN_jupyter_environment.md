# Plan: Jupyter Notebook Environment Setup for MongoDB

## Goal Description
사용자의 요청에 따라 안전하고 독립적인 **Jupyter Notebook 실습 환경**을 구축합니다.
가상환경(`venv`)과 `.env`를 사용하여 보안을 강화하고, **DB 접속 로직을 별도 Python 모듈로 분리**하여 코드 재사용성을 높입니다.

## User Review Required
> [!IMPORTANT]
> **보안 및 설정**
> *   **Credentials**: MongoDB 접속 정보(Host, Port, User, Password)는 `.env` 파일에만 작성합니다. (Plan 문서에 포함 X)
> *   **Reusability**: 접속 로직은 `utils/database.py`에 구현되어 모든 노트북과 스크립트에서 공통으로 사용됩니다.

## Proposed Changes

### 1. Project Structure
`study/` 디렉토리를 다음과 같이 구조화합니다.
```
study/
├── .venv/                  # 가상환경
├── .env                    # 환경변수 (Git 제외)
├── .gitignore              # .env, .venv, .ipynb_checkpoints 추가
├── requirements.txt        # 의존성 패키지
├── utils/                  # [NEW] 공통 유틸리티 모듈
│   ├── __init__.py
│   └── database.py         # [NEW] DB 연결 함수 (Singleton 패턴 권장)
└── notebooks/              # 주피터 노트북
    ├── 00_setup_check.ipynb
    └── 01_mongodb_crud.ipynb
```

### 2. DB Utility (`utils/database.py`)
이 모듈은 다음 역할을 수행합니다.
*   `python-dotenv`를 사용하여 `.env` 로드
*   `pymongo.MongoClient` 생성 및 반환
*   연결 실패 시 에러 처리

### 3. Notebook Usage
노트북에서는 복잡한 설정 없이 다음과 같이 사용합니다.
```python
import sys
import os
sys.path.append(os.path.abspath('..')) # 부모 디렉토리 경로 추가

from utils.database import get_mongo_client

client = get_mongo_client()
```

### 4. Implementation Steps
1.  `docs/plans/PLAN_jupyter_environment.md` 승인 (현재 단계)
2.  `.gitignore` 설정
3.  `requirements.txt` 작성 및 `venv` 생성/설치
4.  `.env` 파일 생성
5.  `utils/database.py` 구현
6.  `notebooks/00_setup_check.ipynb` 생성 및 테스트

## Architecture Decisions
*   **Path Handling**: 노트북이 하위 폴더에 위치하므로, 상위의 `utils`를 임포트하기 위해 `sys.path`를 수정하는 방식을 사용합니다. (가장 간단하고 직관적인 방법)

## Verification Plan
### Automated Tests
*   `notebooks/00_setup_check.ipynb`를 실행하여 `utils.database` 모듈이 정상적으로 임포트되고 DB에 연결되는지 확인.
