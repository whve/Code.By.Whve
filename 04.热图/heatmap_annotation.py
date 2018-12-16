"""
Annotated heatmaps
==================

"""
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
sns.set()
'''
# Load the example flights dataset and conver to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")
'''
# 导入数据

data = pd.read_csv("hotmap_num.csv", delimiter = ',',index_col = 0,header = 0)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))

ax = sns.heatmap(data, cmap="Blues", yticklabels=True,vmin=0, vmax=100)
#  linewidths = 0.05, ax = ax, 加入空隙.cmap="YlGnBu"
plt.savefig('03.D.png', dpi=300, bbox_inches='tight')
"""
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
"""