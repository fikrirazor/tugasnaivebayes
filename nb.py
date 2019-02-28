# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:11:44 2019

@author: Rozan
"""

import pandas as pd

Train = r'data/TrainsetTugas1ML.csv'
dn = pd.read_csv(Train)
print(dn)

peluangincome= dn.income.value_counts()/dn.income.count()
#usia=dn.groupby("age").income.value_counts()
us=dn.groupby('age')['income']
usia=us.value_counts()/us.count()
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