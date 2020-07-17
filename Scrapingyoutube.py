#line1
#can't scrape more than 29 vids
from selenium import webdriver
import pandas as pd

u=[]
v=[]
t=[]#store all titles
w=[]

path= r"C:\Users\hgupt\OneDrive\Desktop\chromedriver.exe"

url='https://www.youtube.com/c/SomeOrdinaryGamers/videos?view=0&sort=dd&flow=grid'#change url according to ur need. prefered to extract data directly from channels video section
driver = webdriver.Chrome(path)
driver.get(url)
videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    t.append(title)
    url = video.find_element_by_tag_name('a').get_attribute('href')
    u.append(url)
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    v.append(views)
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    w.append(when)
    print(title,url,views,when)

#line2
dictionary={'Title':t,'Link':u,'Views':v,'Time':w}
dictionary
#line3
df=pd.DataFrame.from_dict(dictionary)
#line4
df.to_excel(r'C:\Users\hgupt\OneDrive\Desktop\testscrape\youtube.xlsx', index = False)
