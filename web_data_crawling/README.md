# 📰🎬🎭 멀티미디어 웹 크롤링 프로젝트

Python을 활용해 뉴스, 영화, 뮤지컬 정보를 웹에서 자동으로 수집한 크롤링 실습 프로젝트입니다.  
실시간 콘텐츠를 기반으로 데이터를 정제하고 `.csv`로 저장하여 추후 분석에 활용할 수 있도록 구성했습니다.

---

## 🔍 주요 기능

### 📰 뉴스 기사 크롤링
- **크롤링 대상**: [SBS 뉴스 RSS](https://news.sbs.co.kr/news/rss.do)
- **수집 방식**: RSS 피드를 통해 최신 뉴스 수집
- **수집 항목**: 기사 제목, 링크, 발행일
- **저장 파일**: `news.csv`

### 🎬 영화 순위 크롤링
- **크롤링 대상**: [무비차트 영화 실시간 순위](https://www.moviechart.co.kr/rank/realtime/index/image)
- **수집 항목**: 영화 제목, 순위, 개봉일, 평점 등
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

## 💻 실행 방법

1. 라이브러리 설치:
```bash
pip install requests beautifulsoup4 pandas
