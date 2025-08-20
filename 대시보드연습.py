import streamlit as st
import plotly.express as px
import pandas as pd

# 가짜 감정 분류 결과 데이터
emotions = ["행복", "슬픔", "분노", "두려움", "놀람", "중립"]
values = [0.7, 0.3, 0.5, 0.2, 0.6, 0.4]  # 0~1 사이 점수

df = pd.DataFrame(dict(
    Emotion = emotions,
    Score = values
))

# Plotly Radar chart (polar chart)
fig = px.line_polar(df, r='Score', theta='Emotion', line_close=True)
fig.update_traces(fill='toself')  # 안쪽 색 채우기
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,1])),
    showlegend=False
)

st.plotly_chart(fig)
