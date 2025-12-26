import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from utils.database import get_db

def run_crud_basics():
    db = get_db()
    if not db:
        return

    collection = db['users']

    # 1. 초기화 (기존 데이터 삭제)
    collection.delete_many({})
    print("🧹 기존 데이터 삭제 완료")

    # 2. Create (생성)
    user_data = [
        {"name": "Alice", "age": 25, "role": "User"},
        {"name": "Bob", "age": 30, "role": "Admin"},
        {"name": "Charlie", "age": 35, "role": "User"}
    ]
    result = collection.insert_many(user_data)
    print(f"✅ {len(result.inserted_ids)}명의 사용자 생성 완료")

    # 3. Read (조회)
    print("\n🔍 30세 이상 사용자 조회:")
    for user in collection.find({"age": {"$gte": 30}}):
        print(f"- {user['name']} ({user['age']}세, {user['role']})")

    # 4. Update (수정)
    update_result = collection.update_one(
        {"name": "Alice"},
        {"$set": {"age": 26}}
    )
    print(f"\n✏️ {update_result.modified_count}명의 사용자 정보 수정 (Alice 나이 +1)")

    # 5. Delete (삭제)
    delete_result = collection.delete_one({"name": "Charlie"})
    print(f"🗑️ {delete_result.deleted_count}명의 사용자 삭제 (Charlie)")

    # 최종 결과 확인
    print("\n📋 최종 사용자 목록:")
    for user in collection.find():
        print(user)

if __name__ == "__main__":
    try:
        run_crud_basics()
    except Exception as e:
        print(f"오류 발생: {e}")
