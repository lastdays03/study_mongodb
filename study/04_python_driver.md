# 04. Python 연동 (PyMongo)

Python에서 MongoDB를 사용하기 위해 가장 널리 사용되는 드라이버인 `pymongo`를 학습합니다.

## 1. 설치
```bash
pip install pymongo
```

## 2. 연결 (Connection)
`MongoClient`를 사용하여 MongoDB 인스턴스에 연결합니다.

```python
from pymongo import MongoClient

# 로컬 MongoDB 연결 (기본 포트 27017)
# Docker 사용 시에도 동일 (포트 포워딩 된 경우)
client = MongoClient('mongodb://localhost:27017/')

# Atlas 클라우드 연결 시
# client = MongoClient('mongodb+srv://<username>:<password>@cluster0.example.mongodb.net/')

# 데이터베이스 선택 (없으면 자동 생성)
db = client['example_db']

# 컬렉션 선택 (없으면 자동 생성)
collection = db['users']
```

## 3. Python에서의 CRUD
MongoDB 쉘 명령어와 매우 유사하지만, 카멜 케이스(camelCase) 대신 스네이크 케이스(snake_case)를 주로 사용합니다.

### 데이터 삽입 (Insert)
```python
# code/02_crud_basics.py 참조
user_data = {"name": "Jongman", "age": 30}
result = collection.insert_one(user_data)
print(f"Inserted ID: {result.inserted_id}")
```

### 데이터 조회 (Find)
```python
# 한 건 조회
user = collection.find_one({"name": "Jongman"})
print(user)

# 여러 건 조회
for doc in collection.find({"age": {"$gte": 20}}):
    print(doc)
```

### 데이터 수정 (Update)
```python
collection.update_one(
    {"name": "Jongman"},
    {"$set": {"age": 31}}
)
```

### 데이터 삭제 (Delete)
```python
collection.delete_one({"name": "Jongman"})
```
