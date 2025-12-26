# 02. 환경 구축 (Setup)

MongoDB를 학습하기 위해 로컬 환경에 데이터베이스를 설치하거나 클라우드 버전을 사용할 수 있습니다. 여기서는 가장 간편하고 깔끔한 **Docker** 방식을 권장합니다.

## 방법 1: Docker로 설치하기 (권장)
PC에 Docker가 설치되어 있다면 아래 명렁어 한 줄로 MongoDB를 실행할 수 있습니다.

```bash
# 최신 버전의 MongoDB 컨테이너 실행
# -d: 백그라운드 실행
# -p 27017:27017: 호스트와 컨테이너 포트 연결
# --name my-mongo: 컨테이너 이름 지정
docker run -d -p 27017:27017 --name my-mongo mongo:latest
```

실행 확인:
```bash
docker ps
```
`STATUS`가 `Up` 상태라면 정상적으로 실행된 것입니다.

---

## 방법 2: MongoDB Atlas (Cloud)
설치가 번거롭거나 외부에서 접속해야 한다면 [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 무료 티어(Shared)를 추천합니다.
1. 회원 가입 및 Cluster 생성 (FREE 선택)
2. Database Access(유저 생성) 및 Network Access(IP 허용) 설정
3. Connection String 복사 (Python 연동 시 필요)

---

## 방법 3: 로컬 직접 설치
운영체제(Mac, Windows)에 직접 설치하려면 공식 문서를 참고하세요.
* [Install on macOS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
* [Install on Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

---

## GUI 도구 설치: MongoDB Compass
데이터를 시각적으로 확인하고 관리하기 위해 공식 GUI 도구인 **Compass**를 설치하는 것이 좋습니다.
* [Download MongoDB Compass](https://www.mongodb.com/try/download/compass)

설치 후 연결 문자열(Connection String)에 다음을 입력하여 접속합니다:
* Docker/로컬 설치 시: `mongodb://localhost:27017`
