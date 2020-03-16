#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


corona = pd.read_excel('covid.xlsx')


# In[47]:


corona.head()


# In[48]:


x = corona['Week']
y = corona['China']


# In[49]:


p1 = np.poly1d(np.polyfit(x,y,2))
p1


# In[50]:


p2 = np.poly1d(np.polyfit(x,y,3))
p3 = np.poly1d(np.polyfit(x,y,4))
p4 = np.poly1d(np.polyfit(x,y,5))


# In[51]:


xp = np.linspace(0, 11, 100)

xp


# In[52]:


plt.scatter(x,y)


# In[53]:


plt.plot(xp, p1(xp), c='r', label='2nd degree')


# In[54]:


plt.plot(xp, p2(xp), c='g', label='3rd degree')
plt.plot(xp, p2(xp), c='b', label='4th degree')
plt.plot(xp, p2(xp), c='y', label='5th degree')


# In[55]:


yi = corona['India']
yi.dropna(inplace=True)
xi = x[:yi.shape[0]]


# In[56]:


plt.scatter(xi,yi,color='cyan', label='India')


# In[57]:


plt.legend(loc='upper left')


# In[58]:


plt.show()


# In[ ]:




