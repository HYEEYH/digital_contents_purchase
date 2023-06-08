
### digital_contents_purchase구매내역 앱 대시보드
### 예측 화면

### 사용 라이브러리 ----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import joblib

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.cluster import KMeans

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# --------------------------------------------


def run_app_ml():
    st.header('디지털 컨텐츠 구매 예측')
    # st.subheader('▷ 사용 모델')

    ##### 상관관계 확인
    st.subheader('▷ 상관관계 확인')
    #
    # 데이터 불러오기
    df01 = pd.read_csv('data/CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202301.csv', 
                     encoding = 'utf-8')
    df02 = pd.read_csv('data/CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202302.csv', 
                     encoding = 'utf-8')
    df03 = pd.read_csv('data/CI_PRCHS_CLTUR_DGTL_CNTNTS_KND_INFO_202303.csv', 
                     encoding = 'utf-8')
    df_1 = pd.concat([df01,df02], ignore_index=True)
    df = pd.concat([df_1,df03], ignore_index=True)

    # 소득수준 무응답 행 드롭
    index_no = df[ df['HSHLD_INCOME_DGREE_NM'] == '무응답' ].index
    df = df.drop(index_no)

    # 컬럼명 한글로 변경
    df1 = (df.iloc[ : , 2: ]).rename(  columns =  {'SEXDSTN_FLAG_CD':'성별',
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

    # 데이터 숫자로 변환
    label_encoder = LabelEncoder()
    df_I = df1.copy()
    df_I
    # 성별 숫자로 변환
    df_I['성별'] = label_encoder.fit_transform(  df_I['성별']  )
    # 책 구매여부 숫자로 변환
    df_I['서적음반DVD구매여부'] = label_encoder.fit_transform(  df_I['서적음반DVD구매여부']  )
    # 공연구매 여부 숫자로 변환
    df_I['공연전시체험구매여부'] = label_encoder.fit_transform(  df_I['공연전시체험구매여부']  )
    # 게임 구매 여부 숫자로 변환
    df_I['게임구매여부'] = label_encoder.fit_transform(  df_I['게임구매여부']  )
    # 음악 스트리밍 구매 여부 숫자로 변환
    df_I['음악스트리밍다운로드이용권구매여부'] = label_encoder.fit_transform(  df_I['음악스트리밍다운로드이용권구매여부']  )
    # 동영상 구매 여부 숫자로 변환
    df_I['동영상스트리밍다운로드이용권구매여부'] = label_encoder.fit_transform(  df_I['동영상스트리밍다운로드이용권구매여부']  )
    # 기타 컨텐츠 구매 여부 숫자로 변환
    df_I['기타구매여부'] = label_encoder.fit_transform(  df_I['기타구매여부']  )
    # 온/오프라인 숫자로 변환 (온 1, 오프 0)
    df_I.replace({'구매방법': {'오프라인': 0}}, inplace = True)
    df_I.replace({'구매방법': {'온라인': 1}}, inplace = True)
    # 소득구간도 숫자로 바꿈
    # 나이대도 숫자로 바꿈

    # 필요한 컬럼만 가져오기
    df_IN = df_I.iloc[ : , 2: ]


    ### 상관계수 확인하기
    # st.markdown('#### ▶ 상관계수 확인')
    st.dataframe(df_IN.corr(numeric_only = True))
    if st.checkbox('상관계수를 히트맵으로 확인하기'):
        fig = plt.figure()
        sns.heatmap(data = df_IN.corr(numeric_only = True), 
                    annot = True, vmin = -1, vmax = 1, cmap = 'coolwarm')
        st.pyplot(fig)





    ##### 컨텐츠 구매 예측
    st.subheader('▷ 컨텐츠 구매 예측')
    st.markdown('이미 구매한 컨텐츠를 입력받아 앞으로 구매할 컨텐츠를 예측')
    st.markdown('##### 서적음반DVD를 구매할 가능성은 얼마나 될까? ')
    # 온/오프라인 구매 내역 입력 받기
    onoff = st.radio( '구매 방식', [  '온라인', '오프라인'  ]  ) 
    if onoff == '온라인' :
        onoff = 1      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        onoff = 0
    # # 책 구매내역 입력받기
    # book = st.radio( '서적음반DVD 구매여부', [  '없음', '있음'  ]  ) 
    # if book == '없음' :
    #     book = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    # else :
    #     book = 1
    # 공연 구매내역 입력받기
    play = st.radio( '공연전시체험 구매여부', [  '없음', '있음'  ]  ) 
    if play == '없음' :
        play = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        play = 1
    # 게임 구매 내역 입력받기
    game = st.radio( '게임 구매여부', [  '없음', '있음'  ]  ) 
    if game == '없음' :
        game = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        game = 1
    # 음악 스트리밍 구매 여부
    music = st.radio( '음악스트리밍다운로드이용권 구매여부', [  '없음', '있음'  ]  ) 
    if music == '없음' :
        music = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        music = 1
    # 동영상 스트리밍 구매 여부
    video = st.radio( '동영상스트리밍다운로드이용권 구매여부', [  '없음', '있음'  ]  ) 
    if video == '없음' :
        video = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        video = 1
    # 기타 컨텐츠 구매 여부
    ect = st.radio( '기타컨텐츠 구매여부', [  '없음', '있음'  ]  ) 
    if ect == '없음' :
        ect = 0      # 컴퓨터가 알아듣도록 성별을 숫자로 바꿔줌
    else :
        ect = 1   


    ### 예측하기
    if st.button('금액 예측'):

        # 입력받은 정보로 행렬 만들기
        new_data = np.array([onoff, play, game, music, video, ect])   # 1차원
        new_data = new_data.reshape(1, 6)  

        ### 예측하는 코드 작성
        regressor = joblib.load(  'model/regressor.pkl'  )
        y_pred = regressor.predict(new_data)
        
        percent = round(  y_pred[0], 2  )
        st.markdown('##### ▶ 컨텐츠 구매 예측 결과')
        st.text( '서적음반DVD 컨텐츠를 구매할 확률은' + str(percent * 100) + '% 입니다.')





    ##### K-MEANS
    st.subheader('▷ K-MEANS')

    # 데이터 학습하기
    X1 = df_I.iloc[ : , 0: ]
    X1 = X1[['성별', '구매방법', '공연전시체험구매여부', '게임구매여부', 
                    '음악스트리밍다운로드이용권구매여부', 
                    '동영상스트리밍다운로드이용권구매여부', '기타구매여부']]
    scaler = MinMaxScaler()
    X1_scaled = scaler.fit_transform(  X1  )


    ### 그룹 숫자 입력받아 그룹 가져오기
    # WCSS값 구하기
    wcss = []  # 비어있는 리스트 만들어놓고 반복문에서 나온 값들 넣어두기.
    for k in range(1, 10+1) :
        kmeans = KMeans(n_clusters= k , random_state = 5, n_init= 'auto')
        kmeans.fit(X1_scaled)
        wcss.append(kmeans.inertia_)    # wcss 리스트 안에 값을 하나씩 넣어라


    ### WCSS값을 그래프로 나타내기
    st.markdown('#### ▶ WCSS값 ')
    fig = plt.figure()
    x = np.arange(1, 10+1)
    plt.plot(x, wcss)

    plt.title(' The Elbow Method')
    plt.xlabel(' Number of Cluster' )
    plt.ylabel(' WCSS' )
    st.pyplot(fig)





    X2 = df_I.iloc[ : , 0: ]
    X2 = X2[['성별', '구매방법', '공연전시체험구매여부', '게임구매여부', 
                    '음악스트리밍다운로드이용권구매여부', 
                    '동영상스트리밍다운로드이용권구매여부', '기타구매여부']]
    scaler = MinMaxScaler()
    X2_scaled = scaler.fit_transform(  X2  )


    ### k개수 선택 옵션
    st.markdown('#### ▶  클러스터링 개수 선택 ')
    k = st.number_input('k 를 선택해주세요', 1, 10, value = 5)

    kmeans = KMeans(n_clusters = k, random_state = 5, n_init = 'auto')
    y_pred2 = kmeans.fit_predict(X2_scaled)
    df_IN['Group'] = y_pred2  # 그룹정보를 컬럼 하나 생성해서 넣어줌

    st.markdown('#### ▶ 그룹정보 추가한 데이터프레임 보기')
    st.dataframe(df_IN)



    ### 입력받은 그룹의 데이터를 데이터프레임으로 보여주기
    st.markdown('#### ▶ 보고싶은 그룹을 선택')
    group_number = st.number_input('그룹 번호 선택', 0, k-1)
    st.dataframe( df_IN.loc[ df_IN['Group'] == group_number ,  ] )

