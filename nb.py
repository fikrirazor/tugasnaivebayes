# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:11:44 2019

@author: Rozan
"""

import pandas as pd

file = r'data/TrainsetTugas1ML.csv'
df = pd.read_csv(file)
print(df)

peluangincome= df.income.value_counts()/df.income.count()
#usia=df.groupby("age").income.value_counts()
usia=df.groupby('age')['income'].value_counts()/df.groupby('age')['income'].count()
#workclass=df.groupby("workclass").income.value_counts()
workclass=df.groupby("workclass")['income'].value_counts()/df.groupby('workclass')['income'].count()
education=df.groupby("education").income.value_counts()
maritalstatus=df.groupby("marital-status").income.value_counts()
occupation=df.groupby("occupation").income.value_counts()
relationship=df.groupby("relationship").income.value_counts()
hoursperweek=df.groupby("hours-per-week").income.value_counts()

#frequensi age