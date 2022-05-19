#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[2]:


n=pd.read_csv("play.csv")


# In[3]:


n


# In[7]:


conc=np.array(n)[:,:-1]


# In[8]:


conc


# In[15]:


tar=np.array(n)[:,-1:]


# In[16]:


tar


# In[48]:


def finds(tar,conc):
    for i,val in enumerate(tar):
        if val=='yes':
            spec=conc[i].copy()
            break
            
            
    for i,val in enumerate(conc):
        if tar[i]=='yes':
            for x in range (len(spec)):
                if val[x]!=spec[x]:
                    spec[x]='?'
                else:
                    pass
        print('THE MAXIMALLY SPECIFIC HYPOTHESIS',i) 
        print(spec)           
print(finds(tar,conc))


# In[ ]:




