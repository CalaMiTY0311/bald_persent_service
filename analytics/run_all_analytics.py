import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

print("\n[1/4] 연령별 탈모 분석")
import analytics.age

print("\n[2/4] 유전 여부에 따른 탈모 분석")
import analytics.hereditary

print("\n[3/4] 스트레스 레벨별 탈모 분석")
import analytics.stress

print("\n[4/4] 흡연 여부에 따른 탈모 분석")
import analytics.smoking

print("\n=== 분석 완료 ===")
