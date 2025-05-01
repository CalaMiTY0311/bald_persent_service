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

# 연령별 탈모 분석
df_age = df.groupby(['age', 'bald_prob']).size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(8,6),dpi=150)
barchart = sns.barplot(data=df_age, x='age', y='count', hue='bald_prob', ax=ax)
ax.set_frame_on(False)
ax.set_yticks([])
ax.legend().set_title('')
ax.legend().set_frame_on(False)
plt.xlabel('Age Range')
plt.ylabel('Total Person')
plt.title('Alopecia Cases by Age')

for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=6)
    
plt.tight_layout()  # 그래프 여백 자동 조정
plt.show()  # 그래프 표시