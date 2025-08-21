import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import st_folium

st.title("츄러스미🍧")
img = Image.open('./steamlit/profile.png')
st.sidebar.image(img, use_container_width=True)

st.sidebar.header('가나디')
selected_menu = st.sidebar.selectbox(
    '메뉴선택', ['채팅', '병원', '음악', '대시보드']
)

if selected_menu == '대시보드':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 일일 사용량")
        df_day=pd.DataFrame({'day': ['Mon','Tue','Wed','Thu','Fri', 'Sat','Sun'], 'value':[0,0,3,6,3,4,1]})
        fig2 = px.line(df_day, x='day', y='value', markers=True)
        fig2.update_traces(line=dict(color="green"))
        fig2.update_layout(
            xaxis_title="요일",
            yaxis_title="사용량"
        )
        st.plotly_chart(fig2)
    
    with col2:
        st.subheader("🗺️ 병원 위치")
        m = folium.Map(location=[37.5667, 127.0012], zoom_start=12)

        # 2) 여러 개 마커 찍기
        locations = [
            {"name": "서울역", "lat": 37.5547, "lon": 126.9707},
            {"name": "시청", "lat": 37.5663, "lon": 126.9779},
            {"name": "강남역", "lat": 37.4979, "lon": 127.0276},
        ]

        for loc in locations:
            folium.Marker(
                [loc["lat"], loc["lon"]],
                popup=loc["name"],
                tooltip=loc["name"],
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(m)

        # 3) Streamlit에 표시
        st_data = st_folium(m, width=700, height=500)

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("🌈 감정 그래프")
        emotions = ["행복", "슬픔", "분노", "두려움", "놀람", "중립"]
        values = [0.7, 0.3, 0.5, 0.2, 0.6, 0.4]  # 0~1 사이 점수

        df_emo = pd.DataFrame(dict(
            Emotion = emotions,
            Score = values
        ))

        # 감정 그래프
        fig = px.line_polar(df_emo, r='Score', theta='Emotion', line_close=True)
        fig.update_traces(fill='toself')  # 안쪽 색 채우기
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0,1])),
            showlegend=False
        )
        st.plotly_chart(fig)
        
    
    with col4:
        st.subheader("🎵 음악 추천")
        img = Image.open('./steamlit/music.png')
        st.image(img, use_container_width=True, width=500)
        st.markdown("<h5 style='text-align: center;'>가수 - 노래제목</h5>", unsafe_allow_html=True)
        