#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd


# In[9]:


response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')
#pd.dataframe(response.json()['results'])


# In[11]:


pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]


# In[57]:


df_list = []

for i in range(1,300):
    response = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    final = pd.DataFrame(response.json()['results'])[['id','title','overview','release_date','popularity','vote_average','vote_count']]
    df_list.append(final)

df = pd.concat(df_list, ignore_index=True)


# In[58]:


df


# In[61]:


df.to_csv('movies.csv')


# In[ ]:




