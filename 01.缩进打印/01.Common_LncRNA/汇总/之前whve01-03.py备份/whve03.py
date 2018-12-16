# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:22:21 2018

@author: heal_
"""

import pandas as pd

# P值前
tnb = pd.read_csv('metadata.LincSNP 2.0_mellitus_SNP.csv',delimiter = ',')
tnb2 = pd.read_csv('metadata.LincSNP 2.0_mellitus_LncRNA.csv',delimiter = ',')
OB01 = pd.read_csv('metadata.OB_SNP.csv',delimiter = ',')
OB02 = pd.read_csv('metadata.OB_LncRNA.csv',delimiter = ',')
pjs01 = pd.read_csv('metadata.Parkinson_SNP.csv',delimiter = ',')
pjs02 = pd.read_csv('metadata.Parkinson_LncRNA.csv',delimiter = ',')

'''
# P值后
tnb = pd.read_csv('new.tnbsnp.csv',delimiter = ',')
tnb2 = pd.read_csv('new.tnbrna.csv',delimiter = ',')
OB01 = pd.read_csv('new.OBsnp.csv',delimiter = ',')
OB02 = pd.read_csv('new.OBrna.csv',delimiter = ',')
pjs01 = pd.read_csv('new.pjssnp.csv',delimiter = ',')
pjs02 = pd.read_csv('new.pjsrna.csv',delimiter = ',')



tnb = pd.read_csv('new.tnb.and.OBsnp.csv',delimiter = ',')
tnb2 = pd.read_csv('new.tnb.and.OBRNA.csv',delimiter = ',')

pjs01 = pd.read_csv('new.pjssnp.csv',delimiter = ',')
pjs02 = pd.read_csv('new.pjsrna.csv',delimiter = ',')


for i in range(len(tnb)):
    if tnb['SNPID'][i] not in list(pjs01['SNPID']):
        tnb.drop(i,inplace=True)
    else:
        pass
       
for i in range(len(tnb2)):
    if tnb2['SNPID'][i] not in list(pjs02['SNPID']):
        tnb2.drop(i,inplace=True)
    else:
        pass
    
tnb.to_csv('new.tnb.and.OB.and.pjssnp.csv',index=False)
tnb2.to_csv('new.tnb.and.OB.and.pjsRNA.csv',index=False)
'''