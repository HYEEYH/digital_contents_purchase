![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Digital%20ContentsPurchase&fontSize=70)

# digital_contents_purchase
개인 프로젝트2 - 디지털컨텐츠 구매 내역
<br/><br/><br/>

* 디지털 컨텐츠를 구매한 사람들이 다른 디지털 컨텐츠를 구매할 확률은 얼마나 되는지 예측하는 앱 대시보드 입니다.<br/>
<a href= "https://drive.google.com/file/d/1EpSEvDHnr5raoCZTjBcQpefPYu9loMBb/view?usp=drive_link">[시연 영상 보러 가기]</a><br/>
<img src="https://github.com/bopool/aws-hellokids-api/assets/130967557/65ea1f81-0585-42a1-b4ab-3b7a2f4aa3d8"  width="700" height="439" /><br/><br/>

## 사용 툴
<div align=center>
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white"/>
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat&logo=googlecolab&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>
</div>

## 사용한 기술
### Back-ends
#### Visual Studio Code (Python)
##### Streamlit
- 데이터를 불러오고, 불러온 데이터를 데이터 프레임과 차트로 표현
- 라디오 버튼과 드롭다운박스를 이용하여 유저에게 원하는 구매 예측을 원하는 항목(컬럼)을 입력 받음.
- 유저에게 입력 받은 정보를 가지고 regressor 사용하여 구매 예측 실행
#### AWS
- AWS EC2를 서버로 활용해 앱 대시보드 제작

#### 데이터 분석 - 구글 코랩(Google Colab)
##### 데이터 전처리
- 기본 데이터의 크기가 크면 EC2가 다운되기 때문에 데이터 범위를 축소 (1달치 구매내역 -≫ 2주치 구매내역)
- 소득 수준에 무 응답한 행을 드롭
- 영어 줄임말로 되어있는 컬럼 이름을 보기 쉽게 한글로 바꿈
- matplotlib을 이용하여 데이터를 그래프로 표현
- Y(Yes)/N(No) 또는 M(Men)/W(Women)으로 표시되어있는 정보를 숫자로 바꾸어 상관 관계를 분석할 수 있도록 함.
- Numfy와 Pandas를 이용해 데이터 통계 처리
- sklearn을 사용하여 상관 계수를 확인 
##### 인공지능 학습
- sklearn을 사용하여 트레이닝 데이터와 테스트 데이터를 나누고, 테스트 데이터에 예측치를 넣어 테스트 실행
- sklearn을 사용하여 비어있는 변수에 데이터를 학습시켜 regressor를 만듦.
- KMeans를 이용해 WCSS값 차트를 그려 클러스터 개수를 정하고, 그 개수 대로 그룹을 만듦.



##### 
<br/><br/><br/>
