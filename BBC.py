from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import pandas as pd


#Getting the driver
driver = webdriver.Chrome("/Users/Suwani/Downloads/chromedriver")
driver.maximize_window()
url = 'https://www.bbc.co.uk/search?q=Sri+Lanka'
driver.get(url)
driver.implicitly_wait(200)

while True:
    try:
        element = driver.find_element(By.CSS_SELECTOR, "more").click()
        
        if element is None:
            break
    except NoSuchElementException:
        break
    except ElementClickInterceptedException:
        break

head = driver.find_elements_by_xpath('//h1[@itemprop="headline"]')
date = driver.find_elements_by_xpath('//time[@class="display-date"]')
hl = len(head)
dic = {}
conunt = 0
for i in range(hl):
    conunt += 1
    dic[conunt] = [head[i].text,[date[i].text]]
    

bbc_df = pd.DataFrame.from_dict(dic,orient = 'index',columns = ['Headline','Date'])

bbc_df.to_excel('/Users/Suwani/Desktop/Moodys Project/BBC_data.xlsx')
