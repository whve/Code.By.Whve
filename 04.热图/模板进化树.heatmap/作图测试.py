# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:52:40 2019

@author: Lenovo
"""

def iris_whve():
    
    import seaborn as sns; sns.set(color_codes=True)
    iris = sns.load_dataset("iris")
    species = iris.pop("species")
    g = sns.clustermap(iris)
    
    return
# iris_whve()
    
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
import os
# 路径设置,读取或保存的的修改路径.
os.chdir(r'D:\L.临时文件\Z.张珺')

data = pd.read_excel("vj.VP1.xlsx", delimiter = ',',index_col = 0,header = 0)

# 增加指向
sns.set_style("ticks")
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(18, 12))

ax = sns.heatmap(data, cmap="Blues", yticklabels=True, xticklabels=True,vmin=0, vmax=100)
#  linewidths = 0.05, ax = ax, 加入空隙.cmap="YlGnBu"
plt.savefig('vj.VP1.xlsx.png', dpi=300, bbox_inches='tight')
"""
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)