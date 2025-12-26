# 03. 기본 데이터 조작 (CRUD)

MongoDB의 핵심적인 CRUD(Create, Read, Update, Delete) 연산을 학습합니다. 이 명령어들은 `mongosh` (MongoDB Shell) 또는 Compass의 Shell 기능에서 입력할 수 있습니다.

## 1. Create (데이터 삽입)
`insertOne` (단건) 또는 `insertMany` (다건)를 사용합니다.

```javascript
// users 컬렉션에 한 명 추가
db.users.insertOne({
  name: "Kim",
  age: 30,
  email: "kim@example.com"
})

// 여러 명 추가
db.users.insertMany([
  { name: "Lee", age: 25 },
  { name: "Park", age: 35 }
])
```

## 2. Read (데이터 조회)
`find` 메소드를 사용합니다.

```javascript
// 전체 조회
db.users.find()

// 특정 조건 조회 (이름이 "Kim"인 사람)
db.users.find({ name: "Kim" })

// 조건 + 원하는 필드만 조회 (Projetion)
// _id는 기본 포함, 0으로 제외 가능
db.users.find({ name: "Kim" }, { name: 1, age: 1, _id: 0 })
```

### 비교 연산자
*   `$eq`: 같음 (`=`)
*   `$gt` / `$gte`: 초과 / 이상 (`>`, `>=`)
*   `$lt` / `$lte`: 미만 / 이하 (`<`, `<=`)
*   `$ne`: 같이 않음 (`!=`)
*   `$in`: 배열 내 값 중 하나 (`IN`)

```javascript
// 나이가 30살 이상인 사람
db.users.find({ age: { $gte: 30 } })
```

## 3. Update (데이터 수정)
`updateOne` (하나만), `updateMany` (매칭되는 모두)를 사용합니다. **`$set` 연산자**를 사용해야 특정 필드만 수정됩니다. (사용하지 않으면 문서 전체가 교체될 수 있음 주의)

```javascript
// Lee의 나이를 26으로 변경
db.users.updateOne(
  { name: "Lee" },       // 조건
  { $set: { age: 26 } }  // 변경 내용
)
```

## 4. Delete (데이터 삭제)
`deleteOne`, `deleteMany`를 사용합니다.

```javascript
// Park 삭제
db.users.deleteOne({ name: "Park" })
```
