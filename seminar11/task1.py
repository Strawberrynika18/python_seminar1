#!/usr/bin/env python
# coding: utf-8

# In[1]:


#f(x) = -12x^4 - 18x^3+5x^2 + 10x - 30

#Определить корни

#Найти интервалы, на которых функция возрастает

#Найти интервалы, на которых функция убывает

#Построить график

#Вычислить вершину

#Определить промежутки, на котором f > 0

#Определить промежутки, на котором f < 0


# In[5]:


import math
from sympy import *
from sympy.plotting import plot
from numpy import *

x=symbols ('x')
fx=-12*x**4 - 18*x**3+5*x**2 + 10*x - 30
print (solve(fx))


# In[ ]:


sqrt_1, sqrt_2 = solve (fx)
print (sqrt_1, sqrt_2)


# In[9]:


pr=diff(fx)
print (pr)


# In[6]:


#Найти интервалы, на которых функция возрастает 
solve(diff(fx)>0)


# In[7]:


#Найти интервалы, на которых функция убывает
solve(diff(fx)<0)


# In[10]:


#Построить график
p=plot(fx,(x,-20,20))


# In[11]:


#вершина
apex=solve(diff(fx)) [0]


# In[12]:


#Определить промежутки, на котором f > 0
solve(fx>0)


# In[13]:


#Определить промежутки, на котором f < 0
solve(fx<0)

