# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:49:00 2018

@author: heal_
"""
''' 源数据去重'''
import pandas as pd

def whve_gsh():
    tnb01 = pd.read_csv('metadata.LincSNP 2.0_mellitus_SNP.csv',delimiter = ',')
    tnb02 = pd.read_csv('metadata.LincSNP 2.0_mellitus_LncRNA.csv',delimiter = ',')
    OB001 = pd.read_csv('metadata.OB_SNP.csv',delimiter = ',')
    OB002 = pd.read_csv('metadata.OB_LncRNA.csv',delimiter = ',')
    pjs01 = pd.read_csv('metadata.Parkinson_SNP.csv',delimiter = ',')
    pjs02 = pd.read_csv('metadata.Parkinson_LncRNA.csv',delimiter = ',')
    
    tnb01.drop_duplicates(subset=None, keep='first', inplace=True)
    tnb02.drop_duplicates(subset=None, keep='first', inplace=True)
    OB001.drop_duplicates(subset=None, keep='first', inplace=True)
    OB002.drop_duplicates(subset=None, keep='first', inplace=True)
    pjs01.drop_duplicates(subset=None, keep='first', inplace=True)
    pjs02.drop_duplicates(subset=None, keep='first', inplace=True)
    
    tnb01.to_csv('1.csv',index=False)
    tnb02.to_csv('2.csv',index=False)
    OB001.to_csv('3.csv',index=False)
    OB002.to_csv('4.csv',index=False)
    pjs01.to_csv('5.csv',index=False)
    pjs02.to_csv('6.csv',index=False)
    return

tnb = pd.read_csv('1.csv',delimiter = ',')
tnb2 = pd.read_csv('2.csv',delimiter = ',')
OB01 = pd.read_csv('3.csv',delimiter = ',')
OB02 = pd.read_csv('4.csv',delimiter = ',')
pjs01 = pd.read_csv('5.csv',delimiter = ',')
pjs02 = pd.read_csv('6.csv',delimiter = ',')




def whvedelnnn():
    c = [11,12,21,22,31,32]
    a = ['tnb','tnb2','OB01','OB02','pjs01','pjs02']
    for i in range(6):
        print(a[i],c[i])        
        b = eval(a[i]).drop_duplicates(subset=None, keep='first', inplace=False)
        b.to_csv(str(c[i])+'.csv',index=False)
        
        """
        '''(1)指定列,默认所有(2)(3)true在原数据上修改.'''
        写入文件的三种方法
        b.to_csv(str(c[0])+'.csv',index=False)
        b.to_csv('%s.csv' % str(c[1]),index=False)
        b.to_csv('{}.csv'.format(str(c[2])),index=False)
        """    
    return
    
def ceui_whve():
    
    print('我%d岁了' % 26)
    return