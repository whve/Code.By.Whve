# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:09:35 2018

@author: heal_
"""

'''
文档说明:
whve(01)筛选出P>10**(-5)后的文件列表:new.OBrna.csv
whve(02)找到的common snps:new.tnb.and.OBsnp22.csv
whve(03)

'''
import pandas as pd

def whve01():
    '''筛选P值'''
    return
""" 数据去重
tnb = pd.read_csv('metadata.LincSNP 2.0_mellitus_SNP.csv',delimiter = ',')
tnb2 = pd.read_csv('metadata.LincSNP 2.0_mellitus_LncRNA.csv',delimiter = ',')
OB01 = pd.read_csv('metadata.OB_SNP.csv',delimiter = ',')
OB02 = pd.read_csv('metadata.OB_LncRNA.csv',delimiter = ',')
pjs01 = pd.read_csv('metadata.Parkinson_SNP.csv',delimiter = ',')
pjs02 = pd.read_csv('metadata.Parkinson_LncRNA.csv',delimiter = ',')
"""
tnb = pd.read_csv('1.csv',delimiter = ',')
tnb2 = pd.read_csv('2.csv',delimiter = ',')
OB01 = pd.read_csv('3.csv',delimiter = ',')
OB02 = pd.read_csv('4.csv',delimiter = ',')
pjs01 = pd.read_csv('5.csv',delimiter = ',')
pjs02 = pd.read_csv('6.csv',delimiter = ',')
def whve02():
    '''find tnb&OB common SNPs'''
    for i in range(len(tnb)):
        if tnb['SNPID'][i] not in set(OB01['SNPID']):
            tnb.drop(i,inplace=True)
        else:
            pass
    tnb.to_csv('new.tnb.and.OBsnp22.csv',index=False)
    
    return

def whve0201():
    '''find PD&OB common SNPs'''
    for i in range(len(pjs01)):
        if pjs01['SNPID'][i] not in set(OB01['SNPID']):
            pjs01.drop(i,inplace=True)
        else:
            pass
    pjs01.to_csv('new.PD.and.OBsnp22.csv',index=False)
    
    return

def whve03():
    '''find common lncRNA '''

    for i in range(len(OB02)):
        if OB02['LncRNAID'][i] not in set(pjs02['LncRNAID']):
            OB02.drop(i,inplace=True)
        else:
            pass
    OB02.to_csv('new.OB.and.pjs.RNA22.csv',index=False)
    return

def whve0301():
    '''find common lncRNA '''

    for i in range(len(pjs02)):
        if pjs02['LncRNAID'][i] not in set(OB02['LncRNAID']):
            pjs02.drop(i,inplace=True)
        else:
            pass
    pjs02.to_csv('new.pjs.and.OB.RNA22.csv',index=False)
    return

def whve04():
    '''验证'''
    a = set(tnb['SNPID'])
    b = set(OB01['SNPID'])
    c = set(pjs01['SNPID'])
    
    a2 = set(tnb2['SNPID'])
    b2 = set(OB02['SNPID'])
    c2 = set(pjs02['SNPID'])
    
    a22 = set(tnb2['LncRNAID'])
    b22 = set(OB02['LncRNAID'])
    c22 = set(pjs02['LncRNAID'])
    
    print(len(a),len(b),len(c),len(a&b),len(a&c),len(b&c),len(a&b&c))
    print(len(a2),len(b2),len(c2),len(a2&b2),len(a2&c2),len(b2&c2),len(a2&b2&c2))
    print(len(a22),len(b22),len(c22),len(a22&b22),len(a22&c22),len(b22&c22),len(a22&b22&c22))

    return