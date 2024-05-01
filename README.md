# man_vs_talmo API
머신 러닝으로 만든 모델로 8개의 질문을 통해 탈모확률을 예측하는 API입니다.

## 개발 환경
운영 체제 : 윈도우</br>
언어 : Python v3.9</br>
프레임워크 : FastAPI</br>

## 시작 하기
1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. main.py 실행
```zsh
python main.py
```

## 
age = 정수형태의 나이 값을 받습니다.
gender = 성별은 1과 0 값으로 받습니다. (1 = 남자 and 0 = 여자)
is_married = 결혼 여부를 1과 0 값으로 받습니다. (1 = Yes and 0 = No)
is_hereditary = 부모로 부터 탈모 유전의 유무 값을 받습니다. (1 = Yes and 0 = No)
weight = 몸무게 값을 받습니다.(소수 첫번 쨰 자리까지)
height = 키 값을 받습니다.(소수 첫번 째 자리까지)
is_smoker = 흡연유무를 값으로 받습니다. (1 = Yes and 0 = No)
stress = 본인이 상객하는 현재 받고있는 스트레스의 수치를 1(낮음) 부터 10(높음)까지 값으로 받습니다.

;;

bald_prob = 현재 탈모 확률을 0부터 1사이의 범위로 표현합니다.

;;
