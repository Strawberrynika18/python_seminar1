#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sb


# In[7]:


formulaa = pd.read_csv('/content/california_housing_test.csv.csv')


# In[8]:


print(formulaa)


# In[11]:


sb.scatterplot(data=formulaa, x="population", y="households")

