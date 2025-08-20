import streamlit as st
import pandas as pd
import plotly.express as px

# datafile.csv > load > table 출력 > px.box() > st.plotly_chart()
st.subheader('자동차 연비 및 CO2 배출량💨 데이터')
df_2 = pd.read_csv('./data/CO2_Emissions.csv')
df_co2 = pd.DataFrame(df_2)
st.table(df_co2.head(5))
st.dataframe(df_co2)

# plotly scatter
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