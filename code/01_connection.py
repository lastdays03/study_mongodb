import sys
import os

# 부모 디렉토리 경로 추가하여 utils 접근 가능하게 함
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir) 

from utils.database import get_mongo_client

if __name__ == "__main__":
    client = get_mongo_client()
    if client:
        # 연결된 데이터베이스 목록 출력
        print("\n📂 Database 목록:")
        print(client.list_database_names())
        client.close()
