# Plan: Standard MongoDB Learning Roadmap

## Goal Description
기존에 보유한 PDF 파일들의 내용에 얽매이지 않고, **가장 일반적이고 표준적인 MongoDB 학습 순서**에 맞춰 학습 자료(`Markdown`)와 실습 코드(`Python`)를 생성합니다.
입문자부터 실무 활용(Python 연동) 단계까지 체계적으로 학습할 수 있는 커리큘럼을 제공하는 것이 목표입니다.

## User Review Required
> [!IMPORTANT]
> 이 로드맵은 "표준 학습 커리큘럼"을 지향합니다. 사용자의 현재 수준이나 특별히 집중하고 싶은 분야(예: 데이터 분석 위주, 비동기 서버 개발 위주 등)가 있다면 피드백 부탁드립니다.

## Proposed Learning Path (Changes)

### Documentation Structure (`MongoDB/`)

#### [NEW] [README.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/README.md)
*   **Contents**: 전체 커리큘럼 소개 및 각 챕터별 링크 인덱스.

#### [NEW] [01_introduction.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/01_introduction.md)
*   **Topic**: MongoDB & NoSQL 이해
*   **Details**: RDBMS vs NoSQL, Document 지향 모델, JSON/BSON 구조, Collection/Document 개념.

#### [NEW] [02_setup.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/02_setup.md)
*   **Topic**: 환경 구축
*   **Details**: Docker를 이용한 로컬 MongoDB 설치 (권장), MongoDB Atlas(클라우드) 소개, GUI 도구(MongoDB Compass) 설치 및 연결.

#### [NEW] [03_crud.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/03_crud.md)
*   **Topic**: 기본 데이터 조작 (CRUD)
*   **Details**: `insertOne`, `find`, `updateOne`, `deleteOne`, 다양한 쿼리 연산자(`$gt`, `$in`, `$exists` 등).

#### [NEW] [04_python_driver.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/04_python_driver.md)
*   **Topic**: Python 연동 (`pymongo`)
*   **Details**: `pymongo` 설치, 커넥션 맺기, Python 딕셔너리를 이용한 데이터 삽입/조회 실습.

#### [NEW] [05_indexing_and_aggregation.md](file:///Users/bagjongman/dev/workspace/study/python/study_mongodb/study/05_indexing_and_aggregation.md)
*   **Topic**: 성능과 집계 (Advanced)
*   **Details**: 인덱스(Index)의 필요성과 생성, Aggregation Pipeline (`$match`, `$group`, `$sort`) 기초.

### Code Structure (`study/code/`)
각 학습 단계에 맞는 Python 실습 스크립트를 제공합니다.
*   `01_connection.py`: 접속 테스트
*   `02_crud_basics.py`: CRUD 함수 구현
*   `03_aggregation.py`: 집계 파이프라인 실습

## Architecture Decisions
*   **Docker First**: 로컬 설치의 번거로움을 피하기 위해 Docker 사용을 1순위로 가이드합니다.
*   **Python Centric**: 쉘 스크립트보다는 Python(`pymongo`)을 이용한 실습 비중을 높여 실무 활용도를 높입니다.

## Risk Assessment
*   **Risk**: Docker 미설치 환경.
    *   **Mitigation**: `setup.md`에 Docker 설치 간략 가이드 링크 또는 Atlas(무료 티어) 사용법을 대안으로 제시.

## Verification Plan
### Manual Verification
1.  모든 Markdown 문서 생성 확인.
2.  `code/` 디렉토리의 파이썬 스크립트가 로컬 MongoDB(또는 Docker 컨테이너)에 정상적으로 붙어서 동작하는지 `python 01_connection.py` 등으로 테스트.
