# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:11:44 2019

@author: Rozan
"""


'''
X = dn.iloc[:,0:8].values
y = dn.iloc[:,len(dn.iloc[0])-1].values
'''
'''
peluangincome= dn.income.value_counts()/dn.income.count()
#usia=dn.groupby("age").income.value_counts()
us=dn.groupby('age')['income']
age=us.value_counts()/us.count()
#workclass=dn.groupby("workclass").income.value_counts()
wr=dn.groupby("workclass")['income']
workclass=wr.value_counts()/wr.count()
#education=dn.groupby("education").income.value_counts()
ed=dn.groupby("education")['income']
education=ed.value_counts()/ed.count()
#maritalstatus=dn.groupby("marital-status").income.value_counts()
ms=dn.groupby("marital-status")['income']
education=ms.value_counts()/ms.count()
#occupation=dn.groupby("occupation").income.value_counts()
oc=dn.groupby("occupation")['income']
occupation=oc.value_counts()/oc.count()
#relationship=dn.groupby("relationship").income.value_counts()
re=dn.groupby("relationship")['income']
relationship=re.value_counts()/re.count()
#hoursperweek=dn.groupby("hours-per-week").income.value_counts()
ho=dn.groupby("hours-per-week")['income']
hoursperweek=ho.value_counts()/ho.count()

Test = r'data/TestsetTugas1ML.csv'
dt = pd.read_csv(Test)

#P(>50k|X)
abc=dt[:1]
peluangincome['>50K']
   
#P(<=50k|X)
peluangincome['<=50K']
'''

#import library as helper
import pandas as pd


Train = r'data/TrainsetTugas1ML.csv' #initialization of file
dn = pd.read_csv(Train) #read dataset
#conditional probability
#usia=dn.groupby("age").income.value_counts()
us=dn.groupby('age')['income']
agetes=us.value_counts()/us.count()
def conprob(pd1,pd2,transpose=1):
    if transpose==0:
        table=pd.crosstab(pd1,pd2)
    else:
        table=pd.crosstab(pd2,pd1)
    cnames=table.columns.values
    weights=1/table[cnames].sum()
    out=table*weights
    pc=table[cnames].sum()/table[cnames].sum().sum()
    table=table.transpose()
    cnames=table.columns.values
    p=table[cnames].sum()/table[cnames].sum().sum()
    out['p']=p
    return out


#probability of income
pi=dn.income.value_counts()/dn.income.count()
#conditional probability
#idd=conprob(dn.id,dn.income)
ae=conprob(dn.age,dn.income)
wr=conprob(dn.workclass,dn.income)
ed=conprob(dn.education,dn.income)
ms=conprob(dn["marital-status"],dn.income)
on=conprob(dn.occupation,dn.income)
rp=conprob(dn.relationship,dn.income)
hk=conprob(dn["hours-per-week"],dn.income)

Test = r'data/TestsetTugas1ML.csv'
dt = pd.read_csv(Test)
X = dn.iloc[:,1:8].values

'''
age=ae[X[0,0]]
workclass=wr[X[0,1]]
education=ed[X[0,2]]
marital=ms[X[0,3]]
occup=on[X[0,4]]
rela=rp[X[0,5]]
hour=hk[X[0,6]]
#P(>50k|X)
lebih50=hour[0]*rela[0]*occup[0]*marital[0]*education[0]*workclass[0]*age[0]*pi['>50K']
#P(<=50k|X)
kurang50=hour[1]*rela[1]*occup[1]*marital[1]*education[1]*workclass[1]*age[1]*pi['>50K']

if lebih50>kurang50:
    income=">50K"
else: income="<=50K"

print(income)
'''
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
for i in range(panjang):
    kurang50.append(age[i,0]*workclass[i,0]*education[i,0]*marital[i,0]*occup[i,0]*rela[i,0]*hour[i,0]*pi['<=50K'])
    lebih50.append(age[i,1]*workclass[i,1]*education[i,1]*marital[i,1]*occup[i,1]*rela[i,1]*hour[i,1]*pi['>50K'])
    
kurantes= age[4,0]*workclass[4,0]*education[4,0]*marital[4,0]*occup[4,0]*rela[4,0]*hour[4,0]*pi['<=50K']    
lebihtes=age[4,1]*workclass[4,1]*education[4,1]*marital[4,1]*occup[4,1]*rela[4,1]*hour[4,1]*pi['>50K']

kurang52=[]
lebih52=[]
income=[]
for i in range(panjang):
    kurang52.append(kurang50[i]/(kurang50[i]+lebih50[i]))
    lebih52.append(lebih50[i]/(lebih50[i]+kurang50[i]))
    if kurang52[i]<=lebih52[i]:
        income.append("<=50K")
    else:
        income.append.append(">50K")
'''
income=[]
panjang2=len(lebih50)
for i in range(panjang2):
    if kurang50[i]<=lebih50[i]:
        income.append("<=50K")
    else:
        income.append(">50K")
'''
'''
dt['income']=income
from sklearn.metrics import confusion_matrix
ylearn = dn.iloc[:,len(dn.iloc[0])-1].values
ytest = dt.iloc[:,len(dn.iloc[0])-1].values
acc=confusion_matrix(ylearn[:40], ytest[:40])
from sklearn.metrics import accuracy_score
acc2=accuracy_score(ylearn[:40], ytest[:40])*100
print("Akurasi = ",acc2,"%")
'''



