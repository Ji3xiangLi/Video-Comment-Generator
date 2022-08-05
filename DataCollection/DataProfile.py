from config import *
import pandas as pd
from matplotlib import pyplot as plt

# 绘制数据集中每个tag数量的饼图
infos = pd.read_csv(INFO_PATH)
tags = infos['tag'].value_counts()
plt.pie(tags, labels=tags.index, autopct='%1.1f%%')
# plt.legend()
plt.show()
