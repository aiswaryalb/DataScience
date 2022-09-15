# -*- coding: utf-8 -*-
"""Regression Plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13JPizl7i7MrgVCUsp4d2qkLY62Q-nNia
"""

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline
tips = sns.load_dataset('tips')

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,hue ='sex',
           markers=['o','v'])

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,
           col='sex',row='time')

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,
           col='day',hue='sex',aspect=0.6,size=8)

