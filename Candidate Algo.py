#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


n=pd.read_csv("play.csv")


# In[3]:


n


# In[4]:


conc=np.array(n)[:,:-1]


# In[5]:


conc


# In[6]:


tar=np.array(n)[:,-1:]


# In[7]:


tar


# In[9]:


def candidate(conc, tar): 
    spec = conc[0].copy()   
    
    print("\nInitialization of specific and genearal values")
    print("\nSpecific Boundary: ", spec)
    general = [["?" for i in range(len(spec))] for i in range(len(spec))]
    print("\nGeneric Boundary: ",general)  

    for i, h in enumerate(conc):
        print("\nInstance", i+1 , "is ", h)
        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(spec)): 
                if h[x]!= spec[x]:                    
                    spec[x] ='?'                     
                    general[x][x] ='?'
                   
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(spec)): 
                if h[x]!= spec[x]:                    
                    general[x][x] = spec[x]                
                else:                    
                    general[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", spec)         
        print("Generic Boundary after ", i+1, "Instance is ", general)
        print("\n")

    indices = [i for i, val in enumerate(general) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:   
        general.remove(['?', '?', '?', '?', '?', '?']) 
    return spec, general

s_final, g_final = candidate(conc, tar)

print("Final Specific_h: ", s_final, sep="\n")
print("Final General_h: ", g_final, sep="\n")


# In[ ]:




