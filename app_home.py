
### digital_contents_purchase구매내역 앱 대시보드
### 홈 화면

### 사용 라이브러리 ----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# from PIL import Image

# --------------------------------------------


# def run_app_home():
#     # st.title('디지털 컨텐츠 구매 내역 앱')

#     st.subheader('디지털컨텐츠 구매내역 앱에 오신걸 환영합니다.')
#     img = Image.open('data/image1.PNG')
#     st.image(img)
    
#     st.markdown(' #### ▶ 목 차 ')
#     st.markdown(' ##### ◎ EDA ')
#     st.markdown(' → 문화 디지털 컨텐츠 구매 내역을 분석하여 제공합니다 ')

#     st.markdown(' ##### ◎ ML ')
#     st.markdown(' → 문화 디지털 컨텐츠 구매 데이터를 분석하여 다른 디지털 컨텐츠 구매 예측을 할 수 있습니다 ')
    

#     st.markdown('#### ▶ 데이터 출처')
#     st.markdown('#####  문화 빅데이터 플랫폼')

#     if st.checkbox('데이터의 출처를 표시합니다') :
#         img = Image.open('data/homepagecapture.PNG')
#         st.image(img, use_column_width = True)

#         st.markdown('###### : 구입 문화/디지털 컨텐츠 종류(202301), 구입 문화/디지털 컨텐츠 종류(202302), 구입 문화/디지털 컨텐츠 종류(202303)')
#         st.markdown('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=7f2c9fb0-eb98-11ec-a6e8-cdf27550dc0d')



#     # st.image(img_url)
#     # img_url = 'https://www.motorgraph.com/news/photo/201905/22564_72789_5839.jpg'