# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:23:01 2019

@author: Pradeep Kumar
"""

import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#To Analyse top 10 rows we use head() method of dataframes
#print(df.head(10)) 

#To see the column's name we use info() method of dataframes
print(df.info()) 

#To analyse the data column wise by two different ways:-

#sepal_length=df['sepal_length']
#sepal_length=df.sepal_length
#print(sepal_length.head())