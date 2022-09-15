# -*- coding: utf-8 -*-
"""Distribution Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KHYFu3BxfwGasF0vU6wQ9Rcfj6navtMa
"""

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline

tips = sns.load_dataset('tips')

tips.head()

sns.distplot(tips['total_bill'])

sns.distplot(tips['total_bill'],kde = False,bins=30)

sns.jointplot(x='total_bill',y='tip',data=tips)

sns.jointplot(x='total_bill',y='tip',data=tips,kind= 'hex')

sns.jointplot(x='total_bill',y='tip',data=tips,kind= 'reg')

sns.jointplot(x='total_bill',y='tip',data=tips,kind= 'kde')

sns.pairplot(tips)

sns.pairplot(tips,hue='sex',palette='coolwarm')

sns.rugplot(tips['total_bill'])

sns.distplot(tips['total_bill'],kde=False)
#kernel density estimation

