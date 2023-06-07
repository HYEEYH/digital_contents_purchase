
### digital_contents_purchase구매내역 앱 대시보드
### 데이터 분석 화면

### 사용 라이브러리 ----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import openpyxl

from PIL import Image

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 한글깨짐

import platform
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# --------------------------------------------



def run_app_eda():
    # st.title('디지털 컨텐츠 구매 내역 앱')
    st.header('디지털 컨텐츠 구매 내역 데이터 분석')


    #####
    st.subheader('▷ 데이터의 기본 정보 확인')
    
    # 데이터 가져오기
    df01 = pd.read_csv('data\CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202301.csv', 
                     encoding = 'utf-8')
    df02 = pd.read_csv('data\CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202302.csv', 
                     encoding = 'utf-8')
    df03 = pd.read_csv('data\CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202303.csv', 
                     encoding = 'utf-8')
    df_1 = pd.concat([df01,df02], ignore_index=True)
    df = pd.concat([df_1,df03], ignore_index=True)
    # 무응답 행 드롭하기
    index_no = df[ df['HSHLD_INCOME_DGREE_NM'] == '무응답' ].index
    df = df.drop(index_no)
    # 컬럼 정의서 불러오기
    col = pd.read_csv('data\구입 문화디지털 컨텐츠 종류_컬럼정의서.csv', encoding = 'utf-8')
    # 원본 데이터 컬럼 이름 변경하기

    
    # 화면에 표시하기
    st.dataframe( df )
    st.dataframe( col )

    st.markdown('원본 데이터 중 가구별 소득에 무응답한 가구의 데이터는 드롭하여 따로 저장 한 뒤 분석을 하였습니다.')

 


    ##### 성별에 따른 정보
    st.subheader('▷ 성별에 따른 디지털 컨텐츠 구매 정보')

    st.markdown(' ##### ◎ 전체 남 녀 온라인 오프라인 구매 수 ')
    fig = plt.figure()
    sns.countplot(x='PRCHS_MTH_NM',hue='SEXDSTN_FLAG_CD',data= df)
    plt.title('온라인 오프라인 구매 수')
    plt.xlabel('온라인 오프라인')
    plt.ylabel('구매 수')
    st.pyplot(fig)


    ### 남성 데이터
    st.markdown(' ##### ◎ 남성의 구매 내역')

    # 데이터 가져오기
    df_m = (df.loc[   df['SEXDSTN_FLAG_CD'] == 'M',  ]).iloc[ : , 2:]
    # print(df_m.columns)
    df_m_age = df_m.sort_values('AGRDE_FLAG_NM')

    ## 남성 나이대 분포
    st.markdown(' ###### ● 남성의 나이대 분포')
    fig = plt.figure()
    df_m_age['AGRDE_FLAG_NM'].hist()
    plt.title('남성의 나이대 분포 히스토그램')
    plt.xlabel('나이대')
    plt.ylabel('인원')
    st.pyplot(fig)


    ## 남성 데이터들
    df_m = df_m.iloc[ : , 2:]
    df_m = df_m.rename(  columns =  { 'ANSWRR_OC_AREA_NM':'거주 지역', 'HSHLD_INCOME_DGREE_NM':'가구 소득', 'PRCHS_MTH_NM': '구매방법',
                          'BOOK_DISC_DVD_PRCHS_AT': '서적음반DVD구매여부', 'PBLPRFR_DSPY_EXPRN_PRCHS_AT':'공연전시체험구매여부',
                          'GAME_PRCHS_AT': '게임구매여부', 'MUSIC_STRMNG_DWLD_VCH_PRCHS_AT':'음악스트리밍다운로드이용권구매여부',
                          'MVP_STRMNG_DWLD_VCH_PRCHS_AT': '동영상스트리밍다운로드이용권구매여부', 'CLTUR_DGTL_CNTNTS_ETC_PRCHS_AT': '기타구매여부'}  )
    df_m_col_list = df_m.columns.tolist()
    # print(df_m_col_list)


    st.markdown(' ###### ● 남성 온/오프라인 구매 현황')
    column1 = st.selectbox('원하시는 정보를 선택하세요', df_m_col_list)
    fig = plt.figure()
    sns.countplot(x = '구매방법', hue = column1, data= df_m)
    st.pyplot(fig)





    ##### 가장 많이 구매한 컨텐츠
    st.subheader('▷ 가장 많이 구매한 컨텐츠')
    st.markdown(' ##### ◎ 남/녀 디지털 콘텐츠 구매 비율')

    df_1 = (df.iloc[ : , 2: ]).rename(  columns =  {'SEXDSTN_FLAG_CD':'성별',
                                   'AGRDE_FLAG_NM':'나이대', 
                                   'ANSWRR_OC_AREA_NM':'거주 지역', 
                                   'HSHLD_INCOME_DGREE_NM':'가구 소득', 
                                   'PRCHS_MTH_NM': '구매방법',
                                   'BOOK_DISC_DVD_PRCHS_AT': '서적음반DVD구매여부', 
                                   'PBLPRFR_DSPY_EXPRN_PRCHS_AT':'공연전시체험구매여부',
                                   'GAME_PRCHS_AT': '게임구매여부', 
                                   'MUSIC_STRMNG_DWLD_VCH_PRCHS_AT':'음악스트리밍다운로드이용권구매여부',
                                   'MVP_STRMNG_DWLD_VCH_PRCHS_AT': '동영상스트리밍다운로드이용권구매여부', 
                                   'CLTUR_DGTL_CNTNTS_ETC_PRCHS_AT': '기타구매여부'}  )
    
    # print(df_1.columns)

    # 카운트플롯

    # 파이차트 그리기 순서 참고---------
    # df_book = df.loc[  df['BOOK_DISC_DVD_PRCHS_AT'] == 'Y',  ]
    # df_book_pie = df_book[['SEXDSTN_FLAG_CD']]
    # df_book_pie_m = df_book_pie.loc[ df_book_pie['SEXDSTN_FLAG_CD'] == 'M' , ]
    # [df_1['성별'] == 'M', ]
    # [df_1['성별'] == 'F', ]
    # df_1_pie_m = (df.loc[  df[df_1_list] == 'Y',  ][['성별']]).loc[ (df.loc[  df[df_1_list] == 'Y',  ][['성별']])['성별'] == 'M' , ]
    # df_1_pie_f = (df.loc[  df[df_1_list] == 'Y',  ][['성별']]).loc[ (df.loc[  df[df_1_list] == 'Y',  ][['성별']])['성별'] == 'F' , ]
    # df_1_pie_list = [df_1_pie_m.shape[0], df_1_pie_f.shape[0] ]
    # -------------------------------------------------------------

    a = df_1.iloc[ : , 5: ]
    b = a.columns
    df_1_list = b.tolist()

    columns2 = st.selectbox('원하시는 구매 내역을 선택 해 주세요', df_1_list )

    df_1_mf = df_1.loc[  df_1[columns2] == 'Y',  ]
    fig = plt.figure()
    sns.countplot(x='성별', data= df_1_mf)
    st.pyplot(fig)



    # 구매 내역 차트
    st.markdown(' ##### ◎ 구매 내역 차트')

    df_11 = df_1.iloc[ : , 1:4]
    df_111 = (df_11.columns).tolist()
    df_1_phse = df_1.loc[  df_1[columns2] == 'Y',  ]

    # 라디오버튼 수평으로 놓고 라디오 버튼 누르면 차트 나타나게 해보기
    










    st.subheader('▷ 데이터 출처')


    st.subheader('▷ 결론')
    st.text('  ')
    st.text('  ')

# 결론
# ** 는 && 와 관계가 있다
