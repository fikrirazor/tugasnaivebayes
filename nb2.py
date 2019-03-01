# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 23:27:01 2019

@author: Rozan
"""

import pandas as pd
import numpy as np

Train = r'data/TrainsetTugas1ML.csv' #initialization of file
Test = r'data/TestsetTugas1ML.csv'
dn = pd.read_csv(Train) #read dataset
dt = pd.read_csv(Test)
x_train=dn.iloc[:,1:8].values
y_train=dn.iloc[:,len(dn.iloc[0])-1].values
x_test=dt.iloc[:,1:8].values
y_test=dt.iloc[:,len(dn.iloc[0])-1].values

p=len(dn)
jumlahlebih50k=0
jumlahkurang50k=0
for i in range(p):
    if(y_train[i]=='>50K'):
        jumlahlebih50k=jumlahlebih50k+1
    else:
        jumlahkurang50k=jumlahkurang50k+1
    plebih50k=jumlahlebih50k/p
    pkurang50k=jumlahkurang50k/p

adultl50k=0
oldl50k=0
youngl50k=0
for i in range(p):
    if(x_train[i,0]=="adult" and y_train[i]=='>50K'):
        adultl50k=adultl50k+1
    elif(x_train[i,0]=="old" and y_train[i]=='>50K'):
        oldl50k=oldl50k+1
    elif(x_train[i,0]=="young" and y_train[i]=='>50K'):
        youngl50k=youngl50k+1

adultl50k=adultl50k/jumlahlebih50k
    