#!/usr/bin/env python
# coding: utf-8

# In[11]:


from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import os
from tqdm import tqdm
import time




def image_Search(keyword):
    url = 'https://search.naver.com/search.naver?where=image&section=blog&query=' + keyword+'&res_fr=786432&res_to=100000000&sm=tab_opt&color=&ccl=0&nso=so%3Ar%2Ca%3Aall%2Cp%3A1y&recent=0&datetype=5&startdate=0&enddate=0&gif=0&optStr=dr&nso_open=1'
    global driver
    driver = webdriver.Chrome('c:/pydata/chromedriver.exe')
    driver.get(url)
    time.sleep(2)
#     for i in range(5):
#         driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#         time.sleep(2)
    html_source=driver.page_source
    soup=bs(html_source, 'html.parser')
    img_soup=soup.find_all('div',class_='info_title')
    return img_soup

def image_url(img_soup):
    for i in img_soup:
        link=i.find('a')['href']
        driver.get(link)
        time.sleep(2)
        site_html_source=driver.page_source
        site_soup=bs(site_html_source, 'html.parser')
        real_url=site_soup.find('iframe')['src']
        real_url='https://blog.naver.com'+real_url
        driver.get(real_url)
        time.sleep(2)
        blog_html_source=driver.page_source
        blog_soup=bs(blog_html_source, 'html.parser')
        img_list = []
        img_resource=blog_soup.select('img.se-image-resource')
        for img_url in img_resource:
            img_list.append(img_url['src'])
        image_save(img_list)

def image_save(img_list):
    fDir = 'C:/Users/user1/Desktop/이미지/'
    fName = os.listdir(fDir)
   ### 저장할 폴더존재 여부 확인
    fName_dir = keyword
    cnt = 0
    while True:
        if fName_dir not in fName:
            os.makedirs(fDir + fName_dir)
            break
        break
        cnt += 1
        fName_dir = keyword + str(cnt)
    ### 검색 이미지 저장
    cnt=0
    cnt1=0
    iName=os.listdir(fDir+fName_dir)
    newName=keyword + str(cnt) + '.jpg'
    newGIF=keyword + str(cnt) + '.GIF'
    for img in tqdm(img_list):
        if (("JPEG" in img)==True):
            while True:
                if newName in iName:
                    cnt+=1
                    newName=keyword + str(cnt) + '.jpg'
                    continue
                break

            sfdir=fDir + fName_dir + '/' + keyword + str(cnt) + '.jpg'
            urllib.request.urlretrieve(img, sfdir)
            cnt+=1
        elif (("GIF" in img)==True):
            while True:
                if newGIF in iName:
                    cnt1+=1
                    newGIF=keyword + str(cnt1) + '.GIF'
                    continue
                break

            sfadir=fDir + fName_dir + '/' + keyword + str(cnt1) + '.GIF'
            urllib.request.urlretrieve(img, sfadir)
            cnt1+=1

    #driver.close()
    print('검색 이미지 저장 완료')

if __name__=='__main__':
    keyword = input('검색 이미지 검색어를 입력하세요.: ')
    img_soup=image_Search(keyword)
    img_list=image_url(img_soup)


# In[ ]:





# In[ ]:





# In[ ]:




