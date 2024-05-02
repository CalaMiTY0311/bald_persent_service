# man_vs_talmo API
머신 러닝 모델을 사용해 8개의 질문으로 탈모확률을 예측하는 API입니다.

구축환경
```zsh
- os: window
- python: 3.9.17
- fastapi: 0.103.1
- scikit-learn: 1.3.0
```

## 시작 하기
1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. main.py 실행
```zsh
python main.py
```

## 포스트맨 테스트
![man_vs_talmo](https://github.com/CalaMiTY0311/Man_vs_Talmo-API/assets/64539279/a11d5fbd-151e-4213-b2bc-401d54338a67)

## 데이터셋
age = 정수형태의 나이 값을 받습니다.</br>
gender = 성별은 1과 0 값으로 받습니다. (1 = 남자 and 0 = 여자)</br>
is_married = 결혼 여부를 1과 0 값으로 받습니다. (1 = Yes and 0 = No)</br>
is_hereditary = 부모로 부터 탈모 유전의 유무 값을 받습니다. (1 = Yes and 0 = No)</br>
weight = 몸무게 값을 받습니다.(소수 첫번 쨰 자리까지)</br>
height = 키 값을 받습니다.(소수 첫번 째 자리까지)</br>
is_smoker = 흡연유무를 값으로 받습니다. (1 = Yes and 0 = No)</br>
stress = 본인이 상객하는 현재 받고있는 스트레스의 수치를 1(낮음) 부터 10(높음)까지 값으로 받습니다.

bald_prob = 현재 탈모 확률을 0부터 1사이의 범위로 표현합니다.
