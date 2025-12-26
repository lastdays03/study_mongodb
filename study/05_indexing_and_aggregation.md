# 05. 인덱싱과 집계 (Advanced)

대용량 데이터를 처리하기 위해 필수적인 인덱싱(Indexing)과 복잡한 데이터 분석을 위한 집계 파이프라인(Aggregation Pipeline)을 학습합니다.

## 1. 인덱스 (Indexing)
인덱스가 없으면 MongoDB는 쿼리를 수행할 때 컬렉션의 모든 문서를 스캔(Collection Scan)해야 하므로 성능이 매우 느려집니다. 자주 조회되는 필드에는 인덱스를 생성해야 합니다.

```javascript
// name 필드에 오름차순(1) 인덱스 생성
// 내림차순은 -1
db.users.createIndex({ name: 1 })
```

인덱스 확인:
```javascript
db.users.getIndexes()
```

## 2. 집계 파이프라인 (Aggregation Framework)
`find`만으로는 해결하기 어려운 복잡한 데이터 가공, 통계 등을 처리할 때 사용합니다. 여러 단계(Stage)를 거쳐 데이터를 변환합니다.

주요 Stage:
*   `$match`: 문서 필터링 (SQL의 WHERE)
*   `$group`: 그룹화 (SQL의 GROUP BY)
*   `$sort`: 정렬 (SQL의 ORDER BY)
*   `$project`: 출력 필드 지정 (SQL의 SELECT)

### 예제: 나이별 사용자 수 구하기
```javascript
db.users.aggregate([
  // 1단계: 나이가 20살 이상인 사람만 필터링
  { $match: { age: { $gte: 20 } } },
  
  // 2단계: 나이(age)별로 그룹화하고 카운트(count) 계산
  { 
    $group: { 
      _id: "$age", 
      count: { $sum: 1 } 
    } 
  },
  
  // 3단계: 나이( _id ) 내림차순 정렬
  { $sort: { _id: -1 } }
])
```
이 파이프라인 개념은 데이터 분석 시 매우 강력하게 사용됩니다.
