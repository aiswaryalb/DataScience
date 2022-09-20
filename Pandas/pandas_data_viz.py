# -*- coding: utf-8 -*-
"""Pandas Data Viz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ICWI4-0xrQIHdGFNA00JDBVXWu5jOwP
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
# %matplotlib inline
import seaborn as sns

df1 = pd.read_csv('df1',index_col=0)

df1.head()

df2 = pd.read_csv('df2')

df2.head()

df1['A'].hist(bins = 10)

df1['A'].plot(kind = 'hist')

df2.head()

df2.plot.area()

df2.plot.area(alpha = 0.3)

df2.plot.bar()

df1['A'].plot.hist()

df1.plot.scatter(x='A',y='B',cmap='coolwarm')

df2.plot.box()

df2['a'].plot.kde()

df2.plot.density()