#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("goals.csv")


# In[2]:


df.head()


# In[3]:


1. Datenbereinigung hier
2. Datenexport pd.to_cvs("neuefilename") und dann download
3. Import in DB (DB Struktur muss zuerst da sein)
4. Daten aus DB lesen mittels Python und Streamlit
5. Daten visualisieren


# In[4]:


df.tail()


# In[5]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.size


# In[9]:


del df ['right_foot']


# In[ ]:





# In[10]:


df.head()


# In[11]:


del df ['left_foot']


# In[12]:


del df ['headers']


# In[13]:


del df ['others']


# In[14]:


del df ['inside_area']
del df ['outside_areas']


# In[15]:


df.head()


# In[16]:


df.size


# In[18]:


pd.to_cvs("UCL_Gools")


# In[ ]:





# In[19]:


pd.to_cvs ("UCLGools")


# In[ ]:




