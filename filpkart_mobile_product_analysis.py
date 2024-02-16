# -*- coding: utf-8 -*-
"""filpkart_mobile_product_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14GTmvsMoxm6GrUZinwj8h1BOBs09rZ89
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

df = pd.read_csv('Flipkart_Mobiles.csv')

df.shape

#print first 5 rows of the dataset
df.head()

# prompt: Using dataframe df: bar plot

import altair as alt
alt.Chart(df).mark_bar().encode(x='Brand', y='count()').properties(height=400, width=800)

#print last 5 rows of the dataset
df.tail()

# prompt: Using dataframe df: bar plot

import altair as alt
alt.Chart(df).mark_bar().encode(x='Brand', y='count()').properties(height=400, width=800)

#fillna values
df.fillna(0).iloc[:11]

#distribution of data
df.describe().T

#check for data types
df.dtypes

#visualize missing numbers in the dataset
msno.bar(df,figsize=(6,3),color='magenta')

df['Brand'].groupby(df['Brand']).count().sort_values(ascending=False)

df['Brand'].groupby(df['Memory']).count().sort_values(ascending=False)

sns.set_style("white")
sns.pairplot(df, hue='Brand')

df.keys()

sns.displot(df, x= 'Selling Price',bins=[5000,10000,15000,20000,25000,30000,35000,40000,50000,60000,80000], aspect=1.2,color='#fd6c9e')

sns.displot(df, x='Original Price',bins=[5000,10000,15000,20000,25000,30000,35000,40000,50000,60000,80000], aspect=1.2,color='#ff8243')

#brandwise mobile phone price segments
sns.displot(df, x='Selling Price',bins=5, hue='Brand',aspect=1.2)

fig, ax = plt.subplots(figsize=(15,3))
ax=sns.countplot(x="Brand", data=df)

fig, ax = plt.subplots(figsize=(15,3))
ax = sns.stripplot(y="Rating", x="Brand", data=df)

fig, ax = plt.subplots(figsize=(15,3))
ax = sns.stripplot(y="Selling Price", x="Brand", data=df)

fig, ax = plt.subplots(figsize=(15,3))
ax = sns.stripplot(y="Original Price", x="Brand", data=df)

fig, ax = plt.subplots(figsize=(15,6))
ax = sns.boxplot(x="Brand", y="Selling Price", data=df)

# prompt: best sell product ascending wise and plot the graph

# Best selling product ascending wise
best_selling_product = df['Brand'].groupby(df['Brand']).count().sort_values(ascending=True)

# Plot the graph
best_selling_product.plot(kind='bar')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.title('Best Selling Product (Ascending)')
plt.show()