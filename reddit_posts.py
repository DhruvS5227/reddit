#!/usr/bin/env python
# coding: utf-8

# In[1]:


from psaw import PushshiftAPI
from datetime import datetime as dt
import pandas as pd


# In[2]:


api = PushshiftAPI()


# In[3]:


start_epoch=int(dt(2019, 1, 1).timestamp()) 
end_epoch=int(dt(2021, 7, 8).timestamp())

while start_epoch < end_epoch + 86200:    
    api_request_generator =  api.search_submissions(subreddit='4kTV', after = start_epoch, before = start_epoch + 95000000) 
 
 # 86200 * duration of collection 
    tv_submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])
    tv_submissions['date'] = pd.to_datetime(tv_submissions['created_utc'], utc=True, unit='s')
    tv_central = tv_submissions[['title', 'score', 'num_comments', 'selftext', 'link_flair_text','date']]
    
    start_date = dt.fromtimestamp(start_epoch)
    dateStr = start_date.strftime("%Y %b %d")
    
    tv_central.to_csv(r"C:\\Users\\DELL\\Desktop\\hello.csv", index = False, header = True)
    
    start_epoch += 95000000 # 86000 * duration of collection


# In[ ]:




