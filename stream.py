import streamlit as st
import numpy as np #수학 계산에 유용, 소수점 계산도 잘함   
import pandas as pd#엑셀 자료를 잘 처리함, 그래프 그리기에 유용
from datetime import datetime as dt
import datetime

st.title("이것이 타이틀이다")
st.header("이것이 헤더이다")
st.subheader("이것이 서브헤더이다")
st.text("이것이 일반 텍스트이다")

st.title("스마일:😊")

st.caption("스마일은 영어로 Smile")
#st.markdown("마크다운 문법도 지원합니다 **굻게**, *기울임*,~~취소선~~")
st.markdown("**박세연**, *박세연*,~~박세연~~")

# 코드
sample_code='''
def hello()
    print('hello, world')
'''
st.code(sample_code, language='python')

#마크다운 문법 지원
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 :blue[**파란색**] 볼드체로 설정 할 수 있따")
st.markdown(":green[$\sqrt{x^2 + y^2} = 1$]과 같은 수식도 지원한다.")
st.latex(r"\sqrt{x^2 + y^2} = 1")

st.title("데이터프레임 출력하기")

# dataframe생성
dataframe=pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
})
st.dataframe(dataframe) #움직일 수 있음, 표의형태를 

# 테이블 출력
st.table(dataframe) #고정된 표

#메트릭
st.metric(label="기온", value="25°C", delta="1.2°C")

#삼성전자 주가
st.metric(label="삼성전자", value="140,000원", delta="+3,700원")

#컬럼으로 영역 나누기 표기
col1, col2, col3 = st.columns(3)
col1.metric("달러USD", value="1471", delta="+30원")
col2.metric("유로EUR", value="1711", delta="+15원")
col3.metric("엔JPY", value="1,050원", delta="-5원")

# 버튼 클릭
button=st.button("버튼을 눌러주세요")
if button:
    st.write(":blue[버튼]이 눌렸습니다!")

agree=st.checkbox("체크박스를 눌러주세요🅱")
if agree:
    st.write(":green[체크박스]가 눌렸습니다!✅")  

mbti=st.radio(
    "당신의 MBTI는?",
    ("ENFP", "INFP", "INTP", "ISTJ"),
    index=2)
#라디오 버튼은 디폴트 값으로 첫번쨰 것이 선택되어 있음
if mbti=='INTJ':
    st.write("당신은 :red[INTJ]입니다!")
elif mbti=='ENFP':
    st.write("당신은 :orange[ENFP]입니다!")
elif mbti=='INFP':
    st.write("당신은 :green[INFP]입니다!")
else:
    st.write("당신은 :blue[ISTJ]입니다!")

# 셀렉트박스
favorite_color = st.selectbox(
    '당신이 가장 좋아하는 색깔은 무엇인가요?',
    ('빨강', '파랑', '초록', '노랑', '보라')
)
st.write(f'당신이 가장 좋아하는 색깔은 {favorite_color}입니다!')

# 멀티셀렉트박스
hobbies = st.multiselect(
    '당신의 취미를 선택하세요:',
    ['독서', '여행', '요리', '운동', '음악 감상']
)
st.write(f'당신의 취미는: {", ".join(hobbies)}입니다!')

# 슬라이더
age = st.slider('당신의 나이는 몇 살인가요?', 0, 100, 25)
# 최소값, 최대값, 디폴트값(25)
st.write(f'당신의 나이는 {age}살입니다!')

value = st.slider(
    "범위의 값을 다음과 같은 범위로 설정하세요", 0.0, 100.0, (25.0, 75.0)
)

st.write(f'선택한 값의 범위는 :blue[{value}]입니다!')

# 날짜 선택
start_time = st.slider("언제 약속을 잡을래?", 
                       value=(dt(2026, 1, 1, 9, 30), dt(2026, 1, 3, 10, 30)),
                       format="MM/DD/YY - HH:mm")

start_time = st.slider("언제 약속을 잡을래?", 
                       min_value=dt(2026, 1, 1, 9, 30), 
                       max_value = dt(2026, 2, 28, 10, 30),
                       value=dt(2026, 1, 15, 10, 0),
                       step=datetime.timedelta(hours=1),# 1시간 단위로
                       format="yyyy/MM/DD - HH:mm")

st.write(f'약속 시간은 :blue[{start_time}]입니다!')

# 텍스트 입력
title =st.text_input(
    label = '여행지 후보군',
    placeholder='예: 제주도, 영국, 이탈리아, 스위스' # 미리보기처럼 나오는 것
)
st.write(f'당신이 입력한 여행지 후보군은 :blue[{title}]입니다!')

# 숫자 입력
people = st.number_input(
    label='함께 여행하는 인원은 몇 명인가요?',
    min_value=1,
    max_value=20,
    value=2,
    step=1
)
st.write(f'함께 여행하는 인원은 :blue[{people}]명입니다!')

# 파일 다운로드 버튼
st.download_button(
    label = 'csv 파일 다운로드',
    data = dataframe.to_csv().encode('utf-8'), # 위에 만들어 놓은 데이터프레임을 csv확장자로 잡을 것임!
    file_name = 'dataframe.csv',
    mime='text/csv'
)
#csv-> 콤마로 구분된 값을 , 용량이 적음.