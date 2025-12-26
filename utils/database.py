import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

def get_mongo_client():
    """
    .env 파일에서 설정을 로드하여 MongoDB Client를 반환합니다.
    """
    # .env 파일 로드 (현재 디렉토리 또는 상위 디렉토리 탐색)
    # notebooks 폴더에서 실행될 경우를 대비하여 명시적 경로 지정 가능하나,
    # dotenv가 똑똑하게 찾아주므로 우선 기본 로드 시도
    
    # 만약 notebooks/ 내부에서 실행될 때 상위 폴더의 .env를 못 찾으면
    # 아래 코드로 명시적 경로 지정:
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    load_dotenv(dotenv_path=env_path)

    host = os.getenv("MONGO_HOST", "localhost")
    port = int(os.getenv("MONGO_PORT", 27017))
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")
    
    if user and password:
        # 인증이 필요한 경우
        # 특수문자가 있을 수 있으므로 urllib.parse.quote_plus 사용 권장되지만,
        # 여기서는 f-string으로 간단히 구성 (필요시 수정)
        uri = f"mongodb://{user}:{password}@{host}:{port}/"
    else:
        uri = f"mongodb://{host}:{port}/"
        
    try:
        client = MongoClient(uri)
        # 빠른 연결 확인을 위해 ping 명령 실행
        client.admin.command('ping')
        print(f"✅ MongoDB Connected: {host}:{port}")
        return client
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")
        return None

def get_db():
    """
    .env에 정의된 Default Database 객체를 반환합니다.
    """
    client = get_mongo_client()
    if client:
        db_name = os.getenv("MONGO_DB", "study_db")
        return client[db_name]
    return None
