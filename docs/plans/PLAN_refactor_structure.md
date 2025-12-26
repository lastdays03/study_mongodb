# Plan: Project Structure Refactoring (Env Root / Docs Study)

## Goal Description
프로젝트 구조를 **실행 환경(Environment)**과 **학습 자료(Documentation)**로 명확히 분리합니다.
*   **Root (`./`)**: 프로젝트 실행을 위한 `README`, 설정 파일, 코드, 노트북, 유틸리티, 가상환경.
*   **Study (`./study/`)**: 학습 단계별 Markdown 문서 및 참고 자료(PDF).

## User Review Required
> [!NOTE]
> *   `study/` 폴더에는 **Markdown(`*.md`)**과 **PDF(`실습/`)** 자료가 남습니다.
> *   실습용 Python 스크립트(`code/`)는 실행 환경이므로 **Root**로 이동합니다. (문서 내 링크 수정 필요)

## Proposed Changes

### 1. File Movements
#### To Root (`./`)
*   `study/README.md` -> `./README.md` (메인 엔트리 포인트)
*   `study/.env` -> `./.env`
*   `study/.venv/` -> `./.venv/`
*   `study/.gitignore` -> `./.gitignore`
*   `study/requirements.txt` -> `./requirements.txt`
*   `study/utils/` -> `./utils/`
*   `study/notebooks/` -> `./notebooks/`
*   `study/code/` -> `./code/` (Python 실습 스크립트)

#### Keep in (`./study/`)
*   `01_introduction.md` ~ `05_indexing_and_aggregation.md`
*   `실습/` (PDF 파일들)

### 2. Documentation Updates
*   **`./README.md`**: 링크 경로 수정 (예: `./01_introduction.md` -> `./study/01_introduction.md`)
*   **`./study/*.md`**: 코드 참조 경로 수정 (예: `./code/` -> `../code/`)

### 3. Configuration Updates
*   **Imports**: `notebooks`와 `code`가 Root로 이동하므로, `utils` 임포트 경로가 단순해지거나 유지됩니다. (`sys.path.append(os.path.abspath('..'))` -> `sys.path.append(os.path.abspath('.'))` 등으로 조정 필요할 수 있음)

## Verification Plan
### Manual Verification
1.  **File Structure**: 루트에 `README.md`, `requirements.txt`, `.env` 존재 확인. `study/`에 `.md` 파일 존재 확인.
2.  **Link Check**: `README.md`에서 각 챕터 링크 클릭 시 정상 이동 확인.
3.  **Execution Check**: `notebooks/00_setup_check.ipynb` 실행 확인.
