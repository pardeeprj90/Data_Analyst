# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:53:00 2019

@author: Pradeep Kumar
"""

import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
#print(df.head())
plt.xlabel('Length')
plt.ylabel('Width')
plt.title("Sepal length & Width representation in Scatter Plot",fontsize=10)
plt.scatter(df.sepal_length,df.sepal_width,color='red',marker='s',alpha=0.1)
plt.show()