#line1
#this code will scrape recommended movies section of mxplayer
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages=[]
categories=[]
atts=[]
titles=[]#store all titles
urlss=[]

pages_to_scrape=1 #decide the number of pages you want to scrape

for i in range(1,pages_to_scrape+1):
    url =("https://www.mxplayer.in/list/0c75825ce16815a6b1d395205f8ea374?sectionName=Today%27s+Recommendations&sectionStyle=grid_vertical").format(i)#give the url of the website to scrape and for next page check the schema to work on this loop
    pages.append(url)
for item in pages:
    page = requests.get(item)
    soup = bs4(page.text,'html.parser')
    #print(soup.prettify())#prettify to add relationships
    #the loops below are for text data to be extracted
for i in soup.findAll('div',class_='text-overflow card-header'):
    ttl=i.getText()#to get the text value
    titles.append(ttl)#all titles will be stored in titles
for j in soup.findAll('div',class_='text-overflow card-subheader'):#anytime you call class you got to have _ otherwise it will interpret as class which we don't want
    cat=j.getText()
    categories.append(cat)
for s in soup.findAll('a', href=True):
    if s.text:
        att='https://www.mxplayer.in'+str(s['href'])
        atts.append(att)
#line 2
dictionary={'Title':titles,'Categories':categories,}#dictionary with title as key and rest values

dictionary
#line3
durl={'URS':atts}

dfu=pd.DataFrame.from_dict(durl)
durl
#line4
df=pd.DataFrame.from_dict(dictionary)
#line5
df.to_excel(r'C:\Users\hgupt\OneDrive\Desktop\testscrape\mxplayer.xlsx', index = False)
#line6
dfu.to_excel(r'C:\Users\hgupt\OneDrive\Desktop\testscrape\mxplayerurl.xlsx', index = False)
