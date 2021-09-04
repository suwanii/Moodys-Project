from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


#Getting the driver
driver = webdriver.Chrome("/Users/Suwani/Downloads/chromedriver")
driver.maximize_window()
url = 'https://www.reuters.com/search/news?blob=Sri+Lanka&sortBy=relevance&dateRange=pastYear'
driver.get(url)
driver.implicitly_wait(500)

while True:
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".search-result-more-txt").click()
        
        if element is None:
            break
    except NoSuchElementException:
        break
    except ElementClickInterceptedException:
        break
    
    
#Passing driver for bs   
soup = BeautifulSoup(driver.page_source, 'html')  





cont =soup.find ('div',{'class':'column1 col col-10'})
articles = cont.find('div',{'class':'search-result-indiv'})
'''
headline= articles.find('h3',{'class':'search-result-title'})
print(headline.text)
date = articles.find('h5',{'class':'search-result-timestamp'})
print(date.text)
'''
link = articles.find('h3',{'class':'search-result-title'}).find('a').get('href')
print(link)

h = {}
ar_n = 0 #to count the number of articles we scrape

for article in articles:
    headline = article.find('h3',{'class':'search-result-title'}).text
    date = article.find('h5',{'class':'search-result-timestamp'}).text
    ar_n += 1
    h[ar_n] = [headline,date]
    
df = pd.DataFrame.from_dict(h,orient = 'index', columns = ['Headline','Date'] )