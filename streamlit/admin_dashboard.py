import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------
# 기본 설정
# -------------------------------------------------
st.set_page_config(page_title="관리자 대시보드", page_icon="📊", layout="wide")
rng = np.random.default_rng(42)

# -------------------------------------------------
# 사이드바
# -------------------------------------------------
with st.sidebar:
    st.header("🏠 관리자 메뉴")
    menu = st.radio("메뉴", ["사용자 통계", "고객 평가", "서비스 설정", "수익 관리", "로그아웃"], index=0)
    st.caption("© 2025 츄러스미 운영콘솔")

# -------------------------------------------------
# 상단 타이틀 & 안내
# -------------------------------------------------
st.title("관리자 대시보드")
st.info("여기는 관리자 접근할 수 있는 영역입니다.")
st.subheader("사용자 통계")

# -------------------------------------------------
# KPI 메트릭 (기본 위젯)
# -------------------------------------------------
kpi = {
    "하루 방문자 수": {"value": 541, "delta": "+51"},
    "가입자 수": {"value": 12345, "delta": "+300"},
    "평균 사용 시간(분)": {"value": 63, "delta": "+30.45"},
    "평균 이용 빈도(회)": {"value": 5, "delta": "+7.00"},
    "평균 나이(세)": {"value": 31, "delta": "-6.00"},
}
c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    st.date_input("날짜 선택", value=date.today(), format="MM/DD/YYYY")

with c2:
    st.metric("하루 방문자 수",
              f"{kpi['하루 방문자 수']['value']:,}명",
              kpi['하루 방문자 수']['delta'])

with c3:
    st.metric("가입자 수",
              f"{kpi['가입자 수']['value']:,}명",
              kpi['가입자 수']['delta'])

with c4:
    st.metric("평균 사용 시간",
              f"{kpi['평균 사용 시간(분)']['value']}분",
              kpi['평균 사용 시간(분)']['delta'])

with c5:
    st.metric("평균 이용 빈도",
              f"{kpi['평균 이용 빈도(회)']['value']}회",
              kpi['평균 이용 빈도(회)']['delta'])

with c6:
    st.metric("평균 나이",
              f"{kpi['평균 나이(세)']['value']}세",
              kpi['평균 나이(세)']['delta'])
st.write("")
# 그래프 4개를 한 행에 배치
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("#### 가입 추이")
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    signups = [45, 38, 60, 52, 70, 68, 50]
    df_signups = pd.DataFrame({"요일": days, "가입자수": signups})
    fig_line = px.line(df_signups, x="요일", y="가입자수", markers=True,
                       labels={"가입자수":"가입자 수"}, height=280)
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.markdown("#### 성별 비율")
    age_group = st.selectbox("연령대", ["10대", "20대", "30대", "40대", "50대+"], index=1)
    gender_map = {"10대": (0.52, 0.48), "20대": (0.65, 0.35),
                  "30대": (0.58, 0.42), "40대": (0.55, 0.45),
                  "50대+": (0.50, 0.50)}
    male, female = gender_map[age_group]
    df_gender = pd.DataFrame({"성별": ["남성","여성"], "비율": [male, female]})
    fig_donut = go.Figure(data=[go.Pie(labels=df_gender["성별"], values=df_gender["비율"],
                                       hole=0.6, textinfo="label+percent")])
    fig_donut.update_layout(height=280, margin=dict(l=10,r=10,t=30,b=10))
    st.plotly_chart(fig_donut, use_container_width=True)

with col3:
    st.markdown("#### 나이대 분포")
    ages = ["10대","20대","30대","40대","50대+"]
    counts = [120, 320, 260, 110, 46]
    df_age = pd.DataFrame({"나이대": ages, "인원수": counts})
    fig_bar = px.bar(df_age, x="나이대", y="인원수", height=280)
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    st.markdown("#### 감정 트렌드")
    emo_labels = ["분노","기쁨","슬픔","상처","당황","불안"]
    emo_values = [rng.integers(10,100) for _ in emo_labels]
    df_emo = pd.DataFrame({"감정": emo_labels, "건수": emo_values})
    fig_emo = px.bar(df_emo, x="감정", y="건수", height=280)
    st.plotly_chart(fig_emo, use_container_width=True)


st.write("")

