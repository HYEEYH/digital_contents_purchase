
### digital_contents_purchase구매내역 앱 대시보드
### 메인 보드


### 사용 라이브러리 ----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from app_home import run_app_home
from app_eda import run_app_eda
# from app_ml import run_app_ml

# # 한글깨짐
# from matplotlib import font_manager, rc
# plt.rcParams['font.family'] = 'NanumGothic'

# --------------------------------------------


def main():

    ### 화면 만들기

    st.title('디지털 컨텐츠 구매 분석 앱')

    menu = ['Home', 'EDA', 'ML']

    st.sidebar.image('data/icon1.png')
    st.sidebar.title('메뉴')

    choice = st.sidebar.selectbox('원하는 페이지를 선택하세요', menu)


    if choice == menu[0] :
        run_app_home()


    elif choice == menu[1] :
        run_app_eda()


#     else :
#         run_app_ml()


if __name__ == '__main__' :
    main()
