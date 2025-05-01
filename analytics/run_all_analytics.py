import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

print("=== 분석 시작: 모든 그래프를 순차적으로 표시합니다 ===")

print("\n[1/5] 연령별 탈모 분석")
import analytics.age

print("\n[2/5] 유전 여부에 따른 탈모 분석")
import analytics.hereditary

print("\n[3/5] 스트레스 레벨별 탈모 분석")
import analytics.stress

print("\n[4/5] 흡연 여부에 따른 탈모 분석")
import analytics.smoking

print("\n[5/5] 변수 간 상관관계 분석")
import analytics.correlation
