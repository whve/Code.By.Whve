# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:46:56 2018

@author: heal_
"""

import pandas as pd

tnb = pd.read_csv('new.tnbsnp.csv',delimiter = ',')
tnb2 = pd.read_csv('new.tnbrna.csv',delimiter = ',')
OB01 = pd.read_csv('new.OBsnp.csv',delimiter = ',')
OB02 = pd.read_csv('new.OBrna.csv',delimiter = ',')
pjs01 = pd.read_csv('new.pjssnp.csv',delimiter = ',')
pjs02 = pd.read_csv('new.pjsrna.csv',delimiter = ',')


# Common SNP
for i in range(len(tnb)):
    if tnb['SNPID'][i] not in list(OB01['SNPID']):
        tnb.drop(i,inplace=True)
    else:
        pass
    
for i in range(len(tnb)):
    if tnb['SNPID'][i] not in list(pjs01['SNPID']):
        tnb.drop(i,inplace=True)
    else:
        pass
   
# Common RNA
for i in range(len(tnb2)):
    if tnb2['SNPID'][i] not in list(OB02['SNPID']):
        tnb2.drop(i,inplace=True)
    else:
        pass
    
for i in range(len(tnb2)):
    if tnb2['SNPID'][i] not in list(pjs02['SNPID']):
        tnb2.drop(i,inplace=True)
    else:
        pass
