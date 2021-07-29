#!/usr/bin/env python
# coding: utf-8

# In[3]:


import praw
import pandas as pd
import datetime


# In[5]:


reddit = praw.Reddit(client_id='', client_secret='', user_agent='')


# In[6]:


subs = reddit.subreddit('#subreddit_name').hot(limit=1)
for i in subs:
    print(dir(i))


# In[13]:


com = []
subs = reddit.subreddit('#subreddit_name').hot(limit=n) # n = number of posts
for i in  subs:
    comments= i.comments
    for j in comments:
        com.append([i.title,j.body])
com=pd.DataFrame(com,columns= ['title','comments'])
com

    


# In[12]:


com.to_csv("#folder_loaction  .csv")

