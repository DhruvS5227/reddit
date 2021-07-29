#!/usr/bin/env python
# coding: utf-8

# In[3]:


import praw
import pandas as pd
import datetime


# In[5]:


reddit = praw.Reddit(client_id='99HUPgR7vrbuag', client_secret='2NtnOA1WK-5NL-ncAex5tOhBB0JXxA', user_agent='tester1')


# In[6]:


subs = reddit.subreddit('4kTV').hot(limit=1)
for i in subs:
    print(dir(i))


# In[13]:


com = []
subs = reddit.subreddit('4kTV').hot(limit=1000)
for i in  subs:
    comments= i.comments
    for j in comments:
        com.append([i.title,j.body])
com=pd.DataFrame(com,columns= ['title','comments'])
com

    


# In[12]:


com.to_csv("C:\\Users\\DELL\\Desktop\\happy.csv")

