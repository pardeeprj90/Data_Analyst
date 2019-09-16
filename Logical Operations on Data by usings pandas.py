# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:11:10 2019

@author: Pradeep Kumar
"""

import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#result=df.sepal_length==df.sepal_width
#result1 =df.sepal_length > df.sepal_width
#print(result1)

#result2 =df.sepal_length < df.sepal_width
#print(result2)

result3 =df.sepal_length != df.sepal_width
print(result3)