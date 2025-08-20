import streamlit as st

# checkbox
active = st.checkbox('I agree')
if active:
    st.text('체크확인✔')
    
# 함수, on_change=checkbox_write
def checkbox_write():
    st.text('Welcome...✨')
st.checkbox('동의', on_change=checkbox_write) # 체크해제시에도 출력됨 -> true/false 사용

## 세션-상태 값에 저장
if 'checkbox_state' not in st.session_state:
    st.session_state.checkbox_state = False

def checkbox_write1():
    st.session_state.checkbox_state = True
    
if st.session_state.checkbox_state :
    st.write('응...')

st.checkbox('아니 근데 진짜???', on_change=checkbox_write1)

st.divider()

# 토글 버튼
selected = st.toggle('Turn on the switch!!')
if selected:
    st.text('turn on!')
else:
    st.text('turn off')
    
# selectbox 선택지
option = st.selectbox(
    '점심메뉴 고르기',
    options=['김밥','떡볶이','우동','쫄면'],
    index=None,
    placeholder='네개 중 하나만 골라봐'
)
st.text(f'오늘의 점심메뉴는 : {option}')

# radio
genre = st.radio(
    '무슨 영화를 좋아하세요', ['멜로','스릴러', '판타지'], # 자리차지 많이함(보통 선택지가 2개일 때 많이 사용)
    captions=['봄날은 간다', '트리거', '웬즈데이']
)
st.text(f'당신이 좋아하는 장르: {genre}')

# multiselect
menus = st.multiselect(
    '먹고 싶은 거 다 골라🐷', ['김밥','떡볶이','우동','쫄면'],
)
st.text(f'내가 선택한 메뉴는 : {menus}')

# slider
score = st.slider('내 점수 선택', 0, 100, 10) # start, end, init-value
st.text(f'score : {score}')

# 날짜, 시간에 많이 사용
from datetime import time
st_time, end_time = st.slider(
    '공부시간 선택',
    min_value = time(0), max_value=time(11), 
    value = (time(9), time(18)),
    format = 'HH:mm'
)
st.text(f'공부시간 : {st_time} ~ {end_time}')

# text_input
tx1 = st.text_input('영화제목', placeholder = '제목을 입력하세요')
tx2 = st.text_input('비밀번호', placeholder = '비밀번호를 입력하세요', type='password')
st.text(f'텍스트 입력 결과 : {tx1}, {tx2}')

# 파일업로더
# 업로드한 파일은 사용자의 세션에 있습니다. 화면을 갱신하면 사라집니다.
# 서버에 저장하려면 별도로 구현해야 합니다.
# 데이터베이스에 저장하는 로직도 구현할 수 있습니다.

import pandas as pd
file = st.file_uploader(
    '파일 선택', type='csv', # 파일 탐색기에 올라갈 파일 유형 조건
    accept_multiple_files = False
)
if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    with open(file.name, 'wb') as out:
        out.write(file.getbuffer())

# layout 요소
# columns 는 요소를 왼쪽 -> 오른쪽으로 배치할 수 있다

col1, col2, col3  = st.columns(3)

with col1:
    st.metric(
        '오늘의 날씨',
        value='35도',
        delta='+3'
    )
with col2:
    st.metric(
        '오늘의 미세먼지',
        value='좋음',
        delta='-30',
        delta_color='inverse'
    )
with col3:
    st.metric(
        '오늘의 습도',
        value='높음',
        delta='+20'
    )
    
## 
st.markdown('---')

data = {
    '이름' : ['홍길동', '김길동', '박길동'],
    '나이' : [10,20,30]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.divider()

st.table(df)

st.divider()

st.json(data)

st.divider()

# datafile.csv > load > table 출력 > px.box() > st.plotly_chart()
st.subheader('자동차 연비 및 CO2 배출량💨 데이터')
df_2 = pd.read_csv('./data/CO2_Emissions.csv')
df_co2 = pd.DataFrame(df_2)
st.table(df_co2.head(5))
st.dataframe(df_co2)

# plotly scatter
import plotly.express as px

fig = px.box(x = 'Cylinders', y = 'CO2 Emissions(g/km)', 
             data_frame = df_co2
)
fig.update_xaxes(showline=True, linecolor='black', linewidth=3 , mirror=True)
fig.update_yaxes( showline=True, linecolor='black', linewidth=3, mirror=True) # 매개변수로 설정
#fig.show()
fig.update_layout(
    margin=dict(l=50, r=50, t=50, b=50),
    title=dict(
        text="실린더 개수별 CO2 배출량",
        x=0.5,           # 가운데 정렬 (0: 왼쪽, 0.5: 중앙, 1: 오른쪽)
        xanchor='center'
    )
)

st.plotly_chart(fig, use_container_width=False)


# 위젯을 활용한 interactive 그래프 표현
df_2 = pd.read_csv('./data/CO2_Emissions.csv')
df_co2 = pd.DataFrame(df_2)
x_options = ['Make','Cylinders','Vehicle Class','Fuel Type']
y_options = ['CO2 Emissions(g/km)','Fuel Consumption Comb (mpg)']
hue_options = ['Cylinders','Vehicle Class']

x_option = st.selectbox(
    'Select X-axis',
    index=None,
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

hue_option = st.selectbox(
    'Select Hue',
    index=None,
    options=hue_options
)

if (x_option != None) & (y_option != None):
    if hue_option != None:
        fig2 = px.box(
            data_frame=df_co2, x=x_option, y=y_option,
            color=hue_option, width=500
        )
    else:
        fig2 = px.box(
            data_frame=df_co2, x=x_option, y=y_option,
            width=500
        )
    st.plotly_chart(fig2)