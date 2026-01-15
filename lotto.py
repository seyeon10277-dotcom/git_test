import streamlit as st
import random
import datetime

st.title('🍀 로또 번호 생성기 🍀')
st.subheader('버튼을 누를 때마다 새로운 행운이 추가됩니다!')

# 1. session_state 초기화 (번호를 저장할 리스트가 없으면 생성)
if 'lotto_history' not in st.session_state:
    st.session_state['lotto_history'] = []

def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randrange(1, 46)
        lotto.add(number)
    return sorted(list(lotto))

# 2. 번호 생성 버튼
if st.button('번호 생성 🎲'):
    new_numbers = generate_lotto()
    # 생성된 번호를 기록 리스트의 맨 앞에 추가 (최신 번호가 위로 오게)
    st.session_state['lotto_history'].insert(0, new_numbers)

# 3. 초기화 버튼 (기록 삭제)
if st.button('기록 초기화 🧹'):
    st.session_state['lotto_history'] = []
    st.rerun() # 화면 새로고침

st.divider()

# 4. 저장된 번호들 출력
if st.session_state['lotto_history']:
    for idx, numbers in enumerate(st.session_state['lotto_history']):
        # 가장 최근 번호는 강조해서 표시
        if idx == 0:
            st.success(f"🌟 이번 추천 번호: {numbers}")
        else:
            st.write(f"📜 이전 추천 번호: {numbers}")
else:
    st.info("버튼을 눌러 번호를 생성하세요!")

st.sidebar.write(f'📅 마지막 확인: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')