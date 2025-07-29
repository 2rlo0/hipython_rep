# 🧩 멀티미디어 콘텐츠 크롤링 & DB 저장

Python을 활용해 **뉴스**, **영화**, **뮤지컬** 정보를 웹에서 크롤링하여 CSV로 저장하고,  
MySQL 데이터베이스에 자동 적재까지 완료한 데이터 수집 실습 프로젝트입니다.

---

## 🔍 주요 기능

### 📰 뉴스 기사 크롤링
- **크롤링 대상**: [SBS 뉴스 RSS](https://news.sbs.co.kr/news/rss.do)
- **수집 방식**: RSS 피드를 통해 최신 뉴스 수집
- **수집 항목**: 기사 제목, 내용
- **저장 파일**: `news.csv`

### 🎬 영화 순위 크롤링
- **크롤링 대상**: [무비차트 영화 실시간 순위](https://www.moviechart.co.kr/rank/realtime/index/image)
- **수집 항목**: 영화 제목, 사진 url
- **저장 파일**: `movie_list.csv`

### 🎭 뮤지컬 랭킹 크롤링
- **크롤링 대상**: [인터파크 티켓 – 뮤지컬 랭킹](https://tickets.interpark.com/contents/ranking?genre=MUSICAL)
- **수집 항목**: 순위, 제목, 공연 장소, 예매율
- **저장 파일**: `musical_ranking.csv`

---

## 🛠 사용 기술

- **Python**
- **라이브러리**: `requests`, `BeautifulSoup`, `pandas`
- **환경**: Jupyter Notebook (`.ipynb`)

---

## 💽 MySQL 연동

- **DBMS**: MySQL  
- **연결 도구**: `pymysql`
- **기능**:
  - 각 CSV 데이터를 대응 테이블에 저장
  - 중복 제거 및 데이터 정합성 유지
  - 커넥션 → INSERT 쿼리 → 커밋 → 종료 흐름

