from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/Suwani/Downloads/chromedriver')

url = 'https://www.bloomberg.com/search?query=Google'
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)



cont =soup.find ('section',{'class':'mainContent__b8b5cf5e'})
h1= cont.find('a',{'class':'headline__55bd5397'})
print(h1.text)
