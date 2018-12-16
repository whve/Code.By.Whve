# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:02:00 2018

@author: heal_
"""

# 导入snp csv,生成ndarry数组
import numpy as np
import pandas as pd

tnb = pd.read_csv('metadata.LincSNP 2.0_mellitus_SNP.csv',delimiter = ',')
tnb2 = pd.read_csv('metadata.LincSNP 2.0_mellitus_LncRNA.csv',delimiter = ',')
OB01 = pd.read_csv('metadata.OB_SNP.csv',delimiter = ',')
OB02 = pd.read_csv('metadata.OB_LncRNA.csv',delimiter = ',')
pjs01 = pd.read_csv('metadata.Parkinson_SNP.csv',delimiter = ',')
pjs02 = pd.read_csv('metadata.Parkinson_LncRNA.csv',delimiter = ',')

# 筛选出P>10**(-5),drop()
for i in range(len(tnb)):
    if tnb['P value'][i] < 10**(-5):
        tnb.drop(i,inplace=True)
    else:
        pass

# 对比SNPID,如果lncRNASNP不在SNP中,drop it.
for i in range(len(tnb2)):
    if tnb2['SNPID'][i] not in list(tnb['SNPID']):
        tnb2.drop(i,inplace=True)
    else:
        pass

# 筛选出P>10**(-5),drop()
for i in range(len(OB01)):
    if OB01['P value'][i] < 10**(-5):
        OB01.drop(i,inplace=True)
    else:
        pass
# 对比SNPID,如果lncRNASNP不在SNP中,drop it.
for i in range(len(OB02)):
    if OB02['SNPID'][i] not in list(OB01['SNPID']):
        OB02.drop(i,inplace=True)
    else:
        pass

# 筛选出P>10**(-5),drop()
for i in range(len(pjs01)):
    if pjs01['P value'][i] < 10**(-5):
        pjs01.drop(i,inplace=True)
    else:
        pass
# 对比SNPID,如果lncRNASNP不在SNP中,drop it.
for i in range(len(pjs02)):
    if pjs02['SNPID'][i] not in list(pjs01['SNPID']):
        pjs02.drop(i,inplace=True)
    else:
        pass


OB01.to_csv('new.OBsnp.csv',index=False)
OB02.to_csv('new.OBrna.csv',index=False)
pjs01.to_csv('new.pjssnp.csv',index=False)
pjs02.to_csv('new.pjsrna.csv',index=False)