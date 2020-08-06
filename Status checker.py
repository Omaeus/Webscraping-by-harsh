#!/usr/bin/env python
# coding: utf-8

# In[49]:


import csv
import pandas as pd
from collections import defaultdict
import requests
from bs4 import BeautifulSoup 
u=[]

columns = defaultdict(list)
with open('hotstar.csv') as f:#add the excel sheet in the same folder as this code. Change the result.csv as needed.
    reader = csv.DictReader(f) 
    for row in reader: 
        for (k,v) in row.items():  
            columns[k].append(v) 
u= columns['url']
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
r2=[]
r3=[]
counter = 0
for i in u:
    r = requests.get(u[counter],headers=headers)
    r2=r.status_code
    r3.append(r2)
    counter = counter + 1
d={'status':r3}
df=pd.DataFrame.from_dict(d)
df


# In[50]:


df.to_csv(r'C:\Users\hgupt\OneDrive\Desktop\testscrape\status.csv', index = False)#change the path where u wish to export


# In[ ]:





# In[ ]:





# In[ ]:




