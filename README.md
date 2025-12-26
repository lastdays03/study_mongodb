# MongoDB 학습 로드맵 🍃

이 저장소는 MongoDB의 기초부터 Python 연동, 심화 기능까지 학습하기 위한 자료를 담고 있습니다.
아래 순서대로 학습을 진행하는 것을 권장합니다.

## 📚 학습 목차

### Phase 1: 기본 개념 및 환경 설정
MongoDB가 무엇인지 이해하고 실습 환경을 구축합니다.
*   [01. MongoDB 소개 및 NoSQL 이해](./study/01_introduction.md)
*   [02. 환경 구축 (Docker 권장)](./study/02_setup.md)

### Phase 2: 기본 조작
데이터베이스의 가장 기본인 CRUD 명령어를 익힙니다.
*   [03. 기본 데이터 조작 (CRUD)](./study/03_crud.md)

### Phase 3: 애플리케이션 연동
Python을 사용하여 실제 애플리케이션에서 MongoDB를 어떻게 사용하는지 배웁니다.
*   [04. Python 연동 (PyMongo)](./study/04_python_driver.md)
    *   [실습 코드 보기](./code/)

### Phase 4: Jupyter Notebook 실습 (New) 📓
가상환경과 주피터 노트북을 이용하여 대화형으로 실습할 수 있습니다.
1.  **가상환경 활성화**: `source .venv/bin/activate`
2.  **노트북 실행**: `jupyter notebook`
3.  `notebooks/00_setup_check.ipynb`를 실행하여 연결 확인

### Phase 5: 심화
성능 최적화와 복잡한 데이터 분석을 위한 기능을 학습합니다.
*   [05. 인덱싱과 집계 (Advanced)](./study/05_indexing_and_aggregation.md)

---

## 📂 디렉토리 구조
*   `code/`: Python 실습 예제 코드 (Root)
*   `notebooks/`: Jupyter Notebook 실습 (Root)
*   `utils/`: 공통 유틸리티 (Root)
*   `study/`: 학습 문서 및 PDF 자료

---

## 📂 디렉토리 구조
*   `code/`: Python 실습 예제 코드가 포함되어 있습니다.
*   `실습/`: (구) 실습 PDF 자료가 보관되어 있습니다.
