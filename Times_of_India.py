from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("/Users/Suwani/Downloads/chromedriver")
url = 'https://timesofindia.indiatimes.com/topic/Sri-Lanka'

driver.get(url)

#driver = webdriver.Chrome("/Users/Suwani/Downloads/chromedriver")
f_dict = {}
count = 0


for i in range ( 1,21):    
    url = 'https://timesofindia.indiatimes.com/topic/Sri-Lanka/'+ str(i)
    print(url)
    driver.get(url)
    heading = driver.find_elements_by_xpath('//span[@class="title"]')
    date = driver.find_elements_by_xpath('//span[@class="meta"]')

    num_page_items = len(heading)

    for i in range(num_page_items):
        count += 1
        f_dict[count] = [heading[i].text,date[i].text]
        #print(heading[i].text + ':' + date[i].text)

    
times_of_india_df = pd.DataFrame.from_dict(f_dict, orient = 'index',columns = ['Heading','Date'])    

times_of_india_df.to_excel('/Users/Suwani/Desktop/Moodys Project/TimesOfIndia_data.xlsx')
    
    
   