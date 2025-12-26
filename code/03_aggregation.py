import sys
import os
import pprint

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from utils.database import get_mongo_client, get_db

def run_aggregation():
    db = get_db()
    if not db:
        return
        
    collection = db['orders']

    # 샘플 데이터 초기화
    collection.delete_many({})
    orders = [
        {"item": "book", "price": 10, "quantity": 2, "category": "stationery"},
        {"item": "pen", "price": 2, "quantity": 5, "category": "stationery"},
        {"item": "iPad", "price": 500, "quantity": 1, "category": "electronics"},
        {"item": "headphone", "price": 100, "quantity": 1, "category": "electronics"},
        {"item": "note", "price": 5, "quantity": 10, "category": "stationery"},
    ]
    collection.insert_many(orders)
    print("✅ 샘플 주문 데이터 생성 완료")

    # 집계 파이프라인: 카테고리별 총 매출액 계산
    pipeline = [
        # 1. 각 주문의 매출액(price * quantity) 계산하여 'total_sales' 필드 추가
        {
            "$addFields": {
                "total_sales": { "$multiply": ["$price", "$quantity"] }
            }
        },
        # 2. 카테고리별 그룹화 및 매출 합계 계산
        {
            "$group": {
                "_id": "$category",
                "category_revenue": { "$sum": "$total_sales" },
                "count": { "$sum": 1 }
            }
        },
        # 3. 매출액 기준 내림차순 정렬
        {
            "$sort": { "category_revenue": -1 }
        }
    ]

    print("\n📊 카테고리별 매출 통계:")
    results = list(collection.aggregate(pipeline))
    for result in results:
        pprint.pprint(result)

if __name__ == "__main__":
    try:
        run_aggregation()
    except Exception as e:
        print(f"오류 발생: {e}")
