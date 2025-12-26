# 01. MongoDB 소개 및 NoSQL 이해

## 1. NoSQL이란?
NoSQL(Not Only SQL)은 전통적인 관계형 데이터베이스(RDBMS)의 한계를 극복하기 위해 등장한 데이터베이스의 총칭입니다. 고정된 스키마가 없고, 확장성이 뛰어나며, 대량의 분산 데이터를 처리하는 데 적합합니다.

### RDBMS vs NoSQL
| 특징 | RDBMS (MySQL, PostgreSQL) | NoSQL (MongoDB, Redis) |
| :--- | :--- | :--- |
| **데이터 구조** | 테이블(Table), 행(Row), 열(Column) | 문서(Document), 키-값(Key-Value) 등 다양함 |
| **스키마** | 엄격함 (사전에 정의 필요) | 유연함 (Dynamic Schema) |
| **확장성** | 수직적 확장 (Scale-Up) 중심 | 수평적 확장 (Scale-Out) 용이 |
| **쿼리 언어** | SQL (Structured Query Language) | 제품별 고유 API 또는 쿼리 언어 |

---

## 2. MongoDB 특징
MongoDB는 **Document-Oriented(문서 지향)** NoSQL 데이터베이스입니다.

*   **JSON 스타일 (BSON)**: 데이터를 JSON과 유사한 BSON(Binary JSON) 형태로 저장합니다. 개발자에게 매우 직관적입니다.
*   **Schemaless**: 컬렉션(테이블에 해당) 내의 문서는 서로 다른 필드를 가질 수 있습니다.
*   **고가용성 & 확장성**: Replica Set(복제)과 Sharding(분산 저장)을 기본적으로 지원합니다.
*   **강력한 쿼리**: SQL만큼 강력한 검색 및 집계(Aggregation) 기능을 제공합니다.

---

## 3. 핵심 용어 비교
| RDBMS | MongoDB | 설명 |
| :--- | :--- | :--- |
| Database | **Database** | 데이터 저장소의 물리적/논리적 단위 |
| Table | **Collection** | 문서(Document)들의 집합 |
| Row / Record | **Document** | 하나의 데이터 레코드 (JSON 객체) |
| Column | **Field** | 문서 내의 키(Key) |
| Primary Key | **_id** | 각 문서를 식별하는 고유 ID (자동 생성됨) |

---

## 4. 데이터 구조 예시 (JSON/BSON)
```json
{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "홍길동",
  "age": 25,
  "skills": ["Python", "MongoDB", "Django"],
  "address": {
    "city": "Seoul",
    "zip": "12345"
  }
}
```
위와 같이 배열(`skills`)이나 중첩된 객체(`address`)를 하나의 문서에 자연스럽게 저장할 수 있는 것이 MongoDB의 가장 큰 장점입니다.
