# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:11:44 2019

@author: Rozan
"""

#import library as helper
import pandas as pd


Train = r'data/TrainsetTugas1ML.csv' #initialization of file
dn = pd.read_csv(Train) #read dataset
us=dn.groupby('age')['income']
agetes=us.value_counts()/us.count()
def conprob(pd1,pd2,transpose=1):
    if transpose==0:
        table=pd.crosstab(pd1,pd2)
    else:
        table=pd.crosstab(pd2,pd1)
    cnames=table.columns.values
    weights=1/table[cnames].sum()
    out=table*weights #tanpa smoothing
    #out=(table+1)*(weights+3) #Menggunakan add one smoothing 
    #pc=table[cnames].sum()/table[cnames].sum().sum()
    table=table.transpose()
    cnames=table.columns.values
    p=table[cnames].sum()/table[cnames].sum().sum()
    out['p']=p
    return out


pi=(dn.income.value_counts())/(dn.income.count()) 
#pi=(dn.income.value_counts()+1)/(dn.income.count()+2) #add one smoothing
ae=conprob(dn.income,dn.age).T
wr=conprob(dn.income,dn.workclass).T
ed=conprob(dn.income,dn.education).T
ms=conprob(dn.income,dn["marital-status"]).T
on=conprob(dn.income,dn.occupation).T
rp=conprob(dn.income,dn.relationship).T
hk=conprob(dn.income,dn["hours-per-week"]).T

Test = r'data/TestsetTugas1ML.csv'
dt = pd.read_csv(Test)
X = dt.iloc[:,1:8].values

age=ae[X[:,0]].T
age=age.iloc[:,:].values
workclass=wr[X[:,1]].T
workclass=workclass.iloc[:,:].values
education=ed[X[:,2]].T
education=education.iloc[:,:].values
marital=ms[X[:,3]].T
marital=marital.iloc[:,:].values
occup=on[X[:,4]].T
occup=occup.iloc[:,:].values
rela=rp[X[:,5]].T
rela=rela.iloc[:,:].values
hour=hk[X[:,6]].T
hour=hour.iloc[:,:].values


#lebih50=hour[0]*rela[0]*occup[0]*marital[0]*education[0]*workclass[0]*age[0]*pi['>50K']

panjang=len(age)
kurang50=[]
lebih50=[]
income=[]
for i in range(panjang):
    kurang50.append(age[i,0]*workclass[i,0]*education[i,0]*marital[i,0]*occup[i,0]*rela[i,0]*hour[i,0]*pi['<=50K'])
    lebih50.append(age[i,1]*workclass[i,1]*education[i,1]*marital[i,1]*occup[i,1]*rela[i,1]*hour[i,1]*pi['>50K'])

income=[]
panjang2=len(lebih50)
for i in range(panjang2):
    if kurang50[i]>lebih50[i]:
        income.append("<=50K")
    else:
        income.append(">50K")
dt['income']=income
from sklearn.metrics import confusion_matrix
ylearn = dn.iloc[:,len(dn.iloc[0])-1].values
ytest = dt.iloc[:,len(dn.iloc[0])-1].values
acc=confusion_matrix(ylearn[:40], ytest[:40])
from sklearn.metrics import accuracy_score
acc2=accuracy_score(ylearn[:40], ytest[:40])*100
print("Akurasi = ",acc2,"%")


#dt.to_csv('TebakanTugas1ML.csv', index=False, header=None)


