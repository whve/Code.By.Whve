# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:15:39 2018

@author: heal_
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def whve00():
    x = np.random.rand(100).reshape(10,10)
    plt.imshow(x, cmap=plt.cm.hot, vmin=0, vmax=1)
    plt.colorbar()
    plt.show()
    return

def whve0000():
    x = np.random.rand(10, 10)
    plt.matshow(x, cmap = plt.cm.cool, vmin=0, vmax=1)
    plt.colorbar()
    plt.show()
    return

def whve0001():
    x = np.random.rand(10, 10)
    sns.heatmap(x, vmin=0, vmax=1, center=0)
    plt.show()
    return

def whve01():
    # pandas.core.frame.DataFrame
    flights = sns.load_dataset("flights")   
    flights = flights.pivot(index="month", columns="year",values="passengers")
    # flights.save_dataset('1.csv',index=False)
    print (flights)
    # Annotate each cell with the numeric value using integer formatting
    sns.heatmap(flights, annot=True, fmt="d")
    plt.show()

    return

def whve02():
    '''
    x = pd.read_csv('hotmap.csv',delimiter = ',')
    '''
    x = np.random.rand(10, 10)
    print(x)
    sns.heatmap(x, vmin=0, vmax=1, center=0)
    plt.show()
    return

def whve0301():
    # pandas.core.frame.DataFrame
    hotmap_whve = sns.load_dataset("hotmap_whve")   
    hotmap_whve = hotmap_whve.pivot(index="1", columns="2",values="passengers")
    # flights.save_dataset('1.csv',index=False)
    print (hotmap_whve)
    # Annotate each cell with the numeric value using integer formatting
    sns.heatmap(hotmap_whve)
    plt.savefig('heatmapwhve.png', dpi=100, bbox_inches='tight')
    plt.show()
    
    return
def whve03():
    # pandas.core.frame.DataFrame
    hotmap_whve = pd.read_csv("hotmap.csv", delimiter = ',')
    juvd01 = np.mat(hotmap_whve)
    ax = sns.heatmap(juvd01)
    print(ax)
    return
# whve03()
    
def whve04():
    data = pd.read_csv("hotmap_nonum.csv", delimiter = ',')
    data = data.corr()
    print(data)
    sns.heatmap(data)
    plt.show()
    return
whve04()