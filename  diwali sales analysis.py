#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


diwali= pd.read_csv('Diwali Sales Data.csv',encoding='unicode escape')


# In[3]:


diwali.head()


# In[4]:


#data cleaning
diwali.isnull().sum()


# In[5]:


diwali.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[6]:


diwali.isnull().sum()


# In[7]:


diwali.dropna(inplace=True)


# In[8]:


diwali.isnull().sum()


# In[9]:


#changing datatype
diwali['Amount']=diwali['Amount'].astype('int')


# In[10]:


diwali['Amount'].dtypes


# Exploratory Data Analysis

# In[11]:


ax = sns.countplot(x='Gender',data=diwali)
for bars in ax.containers:
    ax.bar_label(bars)


# In[12]:


sales_gender=diwali.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Gender',y='Amount',data=sales_gender)


# Female have done more shopping than man

# In[13]:


ax=sns.countplot(data=diwali,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[14]:


sales_age=diwali.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_age
sns.barplot(x='Age Group',y='Amount',data=sales_age)


# Age group 26-35 have spent more amount.

# In[15]:


states= diwali.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = states,x='State',y='Orders')


# In[16]:


statea = diwali.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=statea,x='State',y='Amount')


# Most of the orders are from UP,MH and Karnataka, and also they have spent more amount of money as compared to another State.

# In[17]:


ax = sns.countplot(data=diwali, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


sales_st = diwali.groupby(['Marital_Status','Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data=sales_st,x='Marital_Status',y='Amount',hue='Gender')


# Through this graph we can conclude that married women have spent more money.

# In[19]:


sns.set(rc={'figure.figsize':(20,7)})
ax = sns.countplot(data = diwali,x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[20]:


Occ = diwali.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending = False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=Occ,x='Occupation',y='Amount')


# Most buyers are from IT sector, Healthcare and aviation industry.

# In[21]:


sns.set(rc={'figure.figsize':(25,10)})
ax = sns.countplot(data = diwali,x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[29]:


product = diwali.groupby(['Product_Category'],as_index = False)['Amount'].sum().sort_values(by = 'Amount',ascending = False).head(5)
sns.set(rc={'figure.figsize':(20,7)})
sns.barplot(data = product,x= 'Product_Category',y='Amount')


# These are the top 5 product categories.

# In[ ]:




