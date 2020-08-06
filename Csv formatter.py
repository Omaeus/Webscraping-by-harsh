#!/usr/bin/env python
# coding: utf-8

# In[181]:


import csv
import pandas as pd
from collections import defaultdict
import numpy
title=[]
desc=[]
duration=[]
lcase=[]
idd=[]
atts=[]
source=[]
sub=[]
cat=[]
dura2=[]
divisionResults=[]
lang=[]
year=[]
columns = defaultdict(list) 

with open('result.csv') as f:#add the excel sheet in the same folder as this code. Change the result.csv as needed.
    reader = csv.DictReader(f) 
    for row in reader: 
        for (k,v) in row.items():  
            columns[k].append(v) 
                                 
#edit this part according to the column-name only the part inside the 'text'
title = columns['title']
desc=columns['description']
duration=columns['duration']
idd=columns['contentId']
cat=columns['assetType']
sub=columns['genre/0']
lang=columns['lang/0']
year=columns['year']
#-----------------------------------------------------------


# In[182]:


#these are main items for our final sheet-------------------
dictionary={'Title':title,'Description':desc,'Duration':duration,'id':idd} 

df=pd.DataFrame.from_dict(dictionary)
df
#-----------------------------------------------------------


# In[183]:


#you will have to manually edit some broken url in final csv
titledf= df.Title.str.lower()
Iddf=df.id
title2= titledf.str.replace(" ", "-")

att = 'https://www.hotstar.com/in/movies/'+ title2 +'/' + Iddf +'/watch'#change only the attribute according to the format of the url.
atts.extend(att)
att
durl={'URS':atts}

dfu=pd.DataFrame.from_dict(durl)
durl
#----------------------------------------------------


# In[184]:


#don't touch this part--------------------------------
dura=df.Duration
time=[]
time2=[]
time3=[]
time=dura.astype(int)
def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec)
for n in time:
    time2=convert(n)
    time3.append(time2)    
time3
#-----------------------------------------------------


# In[185]:


#final format for our csv----------------------------------
dictionary={'title':title,'language_id':lang,'category_id':cat,'subcategory_id':sub,'year':year,'duration':time3,'description':desc,'url':atts}

df=pd.DataFrame.from_dict(dictionary)
df.insert(1,'source_id','hotstar')#change the hotstar with any source you want to add.
df.insert(5,'subcategory1_id','')
df.insert(6,'subcategory2_id','')
df.insert(7,'tags','')
df.insert(9,'starring','')
df.insert(10,'rating','')
df.insert(11,'dubbed','')
df.insert(12,'foreign_language','')
df['tags'] = df[['source_id', 'subcategory_id']].apply(lambda x: ','.join(x), axis=1)
df


# In[186]:


#run this to get the excel sheet-----------------------------------------------------
df.to_csv(r'C:\Users\hgupt\OneDrive\Desktop\testscrape\hotstar.csv', index = False)#give path to get output
#------------------------------------------------------------------------------------


# In[ ]:





# In[ ]:





# In[ ]:




