# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:40:11 2019

@author: Pradeep Kumar
"""

import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#print(df.head())
plt.bar(df.species,df.sepal_width,label='sepal_width')
plt.bar(df.species,df.sepal_length,bottom=df.sepal_width,label='sepal_length')
plt.title('Data Representation and comparison using BAR Plots',fontsize=10)
plt.xlabel('species')
plt.ylabel('sepal_width')
plt.legend()
plt.show()