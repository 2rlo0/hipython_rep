import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import folium
from streamlit_folium import st_folium

# st.set_page_config(page_title="츄러스미", layout="wide") # 페이지 와이드 모드

st.title("츄러스미🍧")
img = Image.open('./streamlit/image/profile.png')

tab_menu, tab_settings = st.sidebar.tabs(["메뉴", "⚙️ 설정"])

with tab_menu:
    st.image(img, use_container_width=True)
    st.header('가나디')
    selected_menu = st.selectbox('메뉴선택', ['메인','채팅', '병원', '음악'])

with tab_settings:
    st.subheader("설정")
    with st.form("settings_form", border=True):
        theme = st.selectbox("테마", ["Auto", "Light", "Dark"], index=0)
        lang = st.selectbox("언어", ["한국어", "English"], index=0)
        notif = st.toggle("알림 받기", value=True)
        submitted = st.form_submit_button("저장")
        if submitted:
            st.session_state["theme"] = theme
            st.session_state["lang"] = lang
            st.session_state["notif"] = notif
            st.success("설정이 저장되었습니다.")


##### 대시보드 창
if selected_menu == '메인':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 일일 사용량")
        df_day=pd.DataFrame({'day': ['Mon','Tue','Wed','Thu','Fri', 'Sat','Sun'], 'value':[0,0,3,6,3,4,1]})
        fig2 = px.line(df_day, x='day', y='value', markers=True)
        fig2.update_traces(line=dict(color="green"))
        fig2.update_layout(
            xaxis_title="요일",
            yaxis_title="사용량",
            width=400,
            height=300
        )
        st.plotly_chart(fig2, use_container_width=False)
    
    with col2:
        st.subheader("🗺️ 병원 위치")
        m = folium.Map(location=[37.5667, 127.0012], zoom_start=12)

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

        st_data = st_folium(m, width=400, height=300)

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
            showlegend=False,
            height=300
        )
        st.plotly_chart(fig)
        
    with col4:
        st.subheader("🎵 음악 추천")
        img = Image.open('./streamlit/image/music.png')
        st.image(img, width=300)
        st.markdown("<h5 style='text-align: center;'>가수 - 노래제목</h5>", unsafe_allow_html=True)

###### 채팅 창
if selected_menu == '채팅':
    st.header("💬 심리 상담")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # 대화 출력
    for sender, msg in st.session_state["messages"]:
        role = "user" if sender == "나" else "assistant"
        with st.chat_message(role):
            st.markdown(f"**{sender}**<br>{msg}", unsafe_allow_html=True)

    # 입력창
    if prompt := st.chat_input("메시지를 입력하세요:"):
        st.session_state["messages"].append(("나", prompt))
        with st.chat_message("user"):
            st.markdown(f"**나**<br>{prompt}", unsafe_allow_html=True)

        # 상담사
        response = f"'{prompt}' 라는 말씀 잘 들었습니다."
        st.session_state["messages"].append(("상담사", response))
        with st.chat_message("assistant"):
            st.markdown(f"**상담사**<br>{response}", unsafe_allow_html=True)

        
 ###### 병원 창       
if selected_menu == '병원':        
    st.subheader("🗺️ 병원 위치")
    m = folium.Map(location=[37.5667, 127.0012], zoom_start=12)

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
    
    st_data = st_folium(m, width=700, height=500)
    
    st.markdown("### 🏥 병원 정보 리스트")
    df = pd.read_csv('./streamlit/hospital_location.csv')
    df_hospital = pd.DataFrame(df)
    st.dataframe(df_hospital[["Unnamed: 0", "요양기관명_x", "주소", "병원홈페이지", "전화번호"]], use_container_width=True)
    
###### 음악 창
if selected_menu == '음악': 
    st.subheader("🎵 음악 추천")

    # 추천 음악 목록 (이미지 경로 + 제목)
    music_list = [
        {"img": "./streamlit/image/babyshark.png", "title": "상어 - 아기상어"},
        {"img": "./streamlit/image/music.png", "title": "노래2 - 제목2"},
        {"img": "./streamlit/image/profile.png", "title": "노래3 - 제목3"},
    ]

    # 여러 곡 출력
    st.markdown("---")
    for music in music_list:
        img = Image.open(music["img"])
        st.image(img, width=200)
        st.markdown(
            f"<h5 style='text-align: center;'>{music['title']}</h5>",
            unsafe_allow_html=True
        )
        st.markdown("---")