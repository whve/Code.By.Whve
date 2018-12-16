# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:06:24 2018

@author: heal_

按列的值去重
new.pjs.and.OB.RNA22.A.csv
"""
import pandas as pd

a = pd.read_csv('new.pjs.and.OB.RNA22.csv',delimiter = ',')

b = pd.read_csv('new.PD.and.OBsnp22.csv',delimiter = ',')
'''
c = pd.read_csv('1.csv',delimiter = ',')
'''
def whve_re():
    a.drop_duplicates(subset='LncRNAID', keep='first', inplace=True)
    a.to_csv('',index=False)
    return

def whve_re01():
    b.drop_duplicates(subset='SNPID', keep='first', inplace=True)
    b.to_csv('new.PD.and.OBsnp22.A.csv',index=False)
    return
