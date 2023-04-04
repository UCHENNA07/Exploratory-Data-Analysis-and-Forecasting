#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis Using Python Libraries

# For this project, we will be utilizing the Pandas, Numpy and Seaborn Python Libraries.

# ####  1. Understanding the Data

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


pwd


# In[3]:


df = pd.read_csv(r"C:\Users\MY-PC\Documents\food_prices_large.csv", encoding = ('ISO-8859-1'))
df


# In[4]:


df.shape


# In[5]:


df.sample(10)


# In[6]:


df.describe()


# In[7]:


df.columns


# In[8]:


df.nunique()


# In[9]:


df.dtypes


# In[4]:


df.info


# In[10]:


df.loc[1] #returns the row at index 1


# In[11]:


df.iloc[3] #returns the column at index 3


# In[12]:


df.iloc[2,1:4] #slicing can be performed on columns as well


# #### 2. Data Cleaning

# Removing null values 

# In[13]:


missing_values = ['N/a', 'na', np.nan]
df = pd.read_csv(r"C:\Users\MY-PC\Documents\food_prices_large.csv", encoding = ('ISO-8859-1'), na_values = missing_values)


# In[14]:


df.isnull().sum()


# In[15]:


df.isnull().any()


# In[16]:


df.dropna()


# Removing Outliers using Percentile method
# NOTE: Outliers are unusual data points which are very different from the rest of the observation. Lets say the numerical 
# representation of month which is normally 1 - 12 and you find out you are having 13 and 14 in the data set which is definitely
# an outlier. So I applied the method in case we have an error in our data set. 

# In[41]:


min_month = df['mp_month'].quantile(0.01)
min_month


# In[39]:


max_month = df['mp_month'].quantile(0.99)
max_month


# In[40]:


df[(df['mp_month'] < max_month) & (df['mp_month'] > min_month)]


# In[20]:


df.shape


# #### 3. Relationship Analysis

# In[33]:


correlation = df.corr()


# In[105]:


sns.heatmap(correlation, xticklabels = correlation.columns, yticklabels = correlation.columns, annot = True)


# In[22]:


sns.relplot(x = 'mp_year', y = 'mp_price', hue = 'pt_name', data = df)


# In[30]:


sns.distplot(df['mp_month'])


# In[28]:


sns.distplot(df['mp_year'])


# In[32]:


sns.catplot(x = 'mp_year', kind = 'box', data = df)


# In[34]:


sns.catplot(x = 'mp_month', kind = 'box', data = df)


# Thank You
