import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import util.config as gConfig

config = gConfig.Config()
path = gConfig.csvPath

df = pd.read_csv(path)

# 흡연자 탈모 분포 분석
df_smoking = df.groupby(['is_smoker', 'bald_prob']).size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(8,6))
barchart = sns.barplot(data=df_smoking, x='is_smoker', y='count', hue='bald_prob', order=['Yes', 'No'], ax=ax)
ax.set_frame_on(False)
ax.set_yticks([])
ax.legend().set_title('')
ax.legend().set_frame_on(False)
plt.xlabel('Smoking')
plt.ylabel('Total Person')
plt.title('Alopecia Cases by Smoking')

for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=6)

plt.tight_layout()  # 그래프 여백 자동 조정
plt.show()  # 그래프 표시