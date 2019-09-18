# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:38:58 2019

@author: Pradeep Kumar
"""
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
from matplotlib import pyplot as plt
url="https://raw.githubusercontent.com/pardeeprj90/CSV_File_For_Data_Analysis/master/mtcars.csv"
df=pd.read_csv(url,sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, 
               prefix=None, mangle_dupe_cols=True, dtype=None, engine='python', converters=None, true_values=None, false_values=None, 
               skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, 
               verbose=False, skip_blank_lines=False, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, 
               dayfirst=False,iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, 
               quotechar='"', quoting=0, doublequote=False, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=False, warn_bad_lines=False, 
               delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
#print(df.head())
plt.hist(df.mpg)
plt.show()
